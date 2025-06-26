# Arquivo: src/main.py

import os
import sys
import subprocess
import logging
import argparse # Importa o módulo argparse para lidar com argumentos de linha de comando

from antlr4 import InputStream, CommonTokenStream

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.semantico.analisador_semantico import AnalisadorSemantico, CustomSemanticErrorListener
from grammar.generated.AraraLexer import AraraLexer
from grammar.generated.AraraParser import AraraParser
from src.error_handler import CustomErrorListener
from src.ast_generator import ASTDotVisitor
from src.tac.TACGenerator import TACGenerator # Importa o TACGenerator
from src.llvm_generator import LLVMGenerator # Importa o LLVMGenerator

# Configura o logging uma vez para todo o programa, incluindo semântico
logging.basicConfig(filename="analisador.log", filemode='w', encoding="utf-8", level=logging.WARNING,
                    format="%(levelname)s: %(message)s")

def analisar_arquivo(caminho, gerar_tac=False, gerar_llvm=False):
    with open(caminho, encoding="utf-8") as f:
        entrada = f.read()
        
    print("-"*40)
    print("Código de entrada:\n" + "-"*40)
    print(entrada)
    print("-"*40)

    # Resetar listeners de erro para cada análise de arquivo
    lexer = AraraLexer(InputStream(entrada))
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    print("Tokens reconhecidos:\n" + "-"*40)
    token_stream_temp = CommonTokenStream(lexer)
    token_stream_temp.fill()
    for token in token_stream_temp.tokens:
        token_name = lexer.symbolicNames[token.type] if token.type < len(lexer.symbolicNames) else str(token.type)
        print(f"<{token_name}, {token.text}, Linha {token.line}, Coluna {token.column}>;")

    # Recria lexer e parser para análise sintática
    lexer = AraraLexer(InputStream(entrada))
    lexer.removeErrorListeners()
    lexer.addErrorListener(CustomErrorListener())

    token_stream = CommonTokenStream(lexer)
    parser = AraraParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    # Gera a árvore de análise sintática
    arvore = parser.programa()

    # Análise semântica
    semantico_listener = CustomSemanticErrorListener()
    semantico = AnalisadorSemantico(semantico_listener)
    semantico.visit(arvore)

    # Verifica se houve erros léxicos/sintáticos antes de continuar
    if CustomErrorListener.has_errors:
        print("❌ Erros léxicos ou sintáticos encontrados. Interrompendo a análise.")
        return

    # Verifica se houve erros semânticos
    if semantico_listener.has_errors:
        print("❌ Erros semânticos encontrados. Interrompendo a análise.")
        return

    print("-"*40)
    print("ARVORE:")
    print("-"*40)
    print(">>> Root node do programa:\n", arvore.toStringTree(recog=parser))
    print("-"*40)

    # Gerar AST
    visitor = ASTDotVisitor()
    visitor.visit(arvore)

    dot_output = visitor.get_dot()

    os.makedirs("docs", exist_ok=True)
    with open("docs/ast.dot", "w", encoding="utf-8") as f:
        f.write(dot_output)

    print("Arquivo docs/ast.dot gerado.")
    print("Gerando imagem com Graphviz...")

    result = subprocess.run(["dot", "-Tpng", "docs/ast.dot", "-o", "docs/ast.png"], capture_output=True, text=True)

    if result.returncode != 0:
        print("❌ Erro ao gerar imagem do AST:")
        print(result.stderr)
    else:
        print("✅ AST gerada com sucesso como 'docs/ast.png'!\n")

    print("-"*40)

    tac_code = [] # Inicializa tac_code como uma lista vazia
    # Geração de Código Intermediário (TAC)
    if gerar_tac:
        print("Iniciando a geração de Código de Três Endereços (TAC)...")
        tac_generator = TACGenerator()
        try:
            tac_generator.visit(arvore)
            tac_code = tac_generator.get_tac_code() # Atribui o TAC gerado

            output_filename = os.path.splitext(os.path.basename(caminho))[0] + ".tac"
            output_filepath = os.path.join(os.path.dirname(caminho), output_filename) # Salva no mesmo diretório do fonte

            with open(output_filepath, "w", encoding="utf-8") as f:
                for instruction in tac_code:
                    f.write(instruction + "\n")
            print(f"✅ Código TAC gerado com sucesso em '{output_filepath}'!")
            print("\nCódigo TAC gerado:\n" + "-"*40)
            for instruction in tac_code:
                print(instruction)
            print("-"*40)

        except Exception as e:
            print(f"❌ Erro na geração do código intermediário (TAC): {e}")
            logging.error(f"Erro na geração de TAC: {e}")
            sys.exit(1) # Sai com código de erro

    # Geração de Código Final (LLVM IR)
    if gerar_llvm and tac_code: # Garante que TAC foi gerado se essa opção estiver ativa
        print("Iniciando a geração de Código Final (LLVM IR)...")
        llvm_generator = LLVMGenerator()
        try:
            # Passa as instruções TAC para o gerador de LLVM IR
            llvm_ir_code = llvm_generator.generate_llvm_ir(tac_code, semantico.tabela_simbolos)

            output_filename = os.path.splitext(os.path.basename(caminho))[0] + ".ll"
            output_filepath = os.path.join(os.path.dirname(caminho), output_filename)

            with open(output_filepath, "w", encoding="utf-8") as f:
                f.write(llvm_ir_code)
            print(f"✅ Código LLVM IR gerado com sucesso em '{output_filepath}'!")
            print("\nCódigo LLVM IR gerado:\n" + "-"*40)
            print(llvm_ir_code)
            print("-"*40)

        except Exception as e:
            print(f"❌ Erro na geração do código final (LLVM IR): {e}")
            logging.error(f"Erro na geração de LLVM IR: {e}")
            sys.exit(1) # Sai com código de erro
    elif gerar_llvm and not tac_code:
        print("⚠️ Aviso: A geração de LLVM IR foi solicitada, mas o Código de Três Endereços (TAC) não foi gerado ou está vazio. Certifique-se de usar --gerar-tac.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compilador Arara - Análise Léxica, Sintática, Semântica, Geração de TAC e LLVM IR.")
    parser.add_argument("arquivo", help="Caminho para o arquivo .arara a ser compilado.")
    parser.add_argument("--gerar-tac", action="store_true", help="Ativa a geração do Código de Três Endereços (TAC).")
    parser.add_argument("--gerar-llvm", action="store_true", help="Ativa a geração do Código Final (LLVM IR). Requer --gerar-tac.")


    args = parser.parse_args()

    # Resetar o estado de erros antes de cada execução, caso o script seja chamado múltiplas vezes
    CustomErrorListener.has_errors = False
    CustomSemanticErrorListener.has_errors = False

    analisar_arquivo(args.arquivo, args.gerar_tac, args.gerar_llvm)