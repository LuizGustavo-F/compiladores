# Arquivo: src/tac/TACGenerator.py

from antlr4.tree.Tree import ParseTreeVisitor
from grammar.generated.AraraParser import AraraParser

# Classe TACOperand: Representa operandos (valores, variáveis, temporários ou rótulos) usados nas instruções TAC.
class TACOperand:
    """Representa um operando em uma instrução TAC."""
    def __init__(self, type, value):

        # Tipo do operando ('ID', 'TEMP', 'LITERAL', 'LABEL')
        self.type = type 
        # Valor do operando (nome da variável, valor literal, nome do temporário, nome do rótulo)
        self.value = value

    # Método para representação em string do operando
    def __str__(self):
        return str(self.value)

    # Métodos de verificação de tipo
    def is_literal(self):
        return self.type == 'LITERAL'

    def is_id(self):
        return self.type == 'ID'

    def is_temp(self):
        return self.type == 'TEMP'

    def is_label(self):
        return self.type == 'LABEL'

# Classe TACInstruction: Representa uma instrução TAC, com um opcode (como ADD, ASSIGN, IF_FALSE_GOTO)
class TACInstruction:
    """Representa uma instrução de Código de Três Endereços (TAC)."""
    def __init__(self, opcode, result=None, arg1=None, arg2=None):
        # O código da operação (ex: 'ASSIGN', 'ADD', 'READ', 'WRITE', 'IF_FALSE_GOTO', 'LABEL')
        self.opcode = opcode 
        # Operando de destino/resultado da instrução (um objeto TACOperand)
        self.result = result 
        # Primeiro operando de argumento (um objeto TACOperand)
        self.arg1 = arg1 
        # Segundo operando de argumento (um objeto TACOperand)
        self.arg2 = arg2 

    # Método para representação em string da instrução (usado para imprimir o TAC formatado)
    def __str__(self):
        # Formato para rótulos (LABEL)
        if self.opcode == "LABEL":
            return f"{self.result.value}:"
        # Formato para atribuições (ASSIGN)
        elif self.opcode == "ASSIGN":
            if self.arg1.is_literal() and self.arg2 is None:
                return f"{self.result.value} = {self.arg1.value}"
            return f"{self.result.value} = {self.arg1.value}"
        # Formato para operações binárias (ADD, SUB, MUL, DIV, EQ, etc.)
        elif self.opcode in ["ADD", "SUB", "MUL", "DIV", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR"]:
            # Usa um método auxiliar para obter o símbolo do operador (ex: "+" para "ADD")
            return f"{self.result.value} = {self.arg1.value} {self._get_symbol(self.opcode)} {self.arg2.value}"
        # Formato para operação NOT
        elif self.opcode == "NOT":
            return f"{self.result.value} = ! {self.arg1.value}"
        # Formato para salto condicional (IF_FALSE_GOTO)
        elif self.opcode == "IF_FALSE_GOTO":
            return f"IF_FALSE {self.arg1.value} GOTO {self.result.value}"
        # Formato para salto incondicional (GOTO)
        elif self.opcode == "GOTO":
            return f"GOTO {self.result.value}"
        # Formato para leitura (READ)
        elif self.opcode == "READ":
            return f"READ {self.result.value}"
        # Formato para escrita (WRITE)
        elif self.opcode == "WRITE":
            return f"WRITE {self.result.value}"
        # Formato genérico para outros opcodes não especificados
        else:
            return f"{self.opcode} {self.result} {self.arg1} {self.arg2}"

    # Método auxiliar para obter o símbolo de um operador aritmético/lógico/comparação
    def _get_symbol(self, opcode):
        if opcode == "ADD": return "+"
        if opcode == "SUB": return "-"
        if opcode == "MUL": return "*"
        if opcode == "DIV": return "/"
        if opcode == "EQ": return "=="
        if opcode == "NEQ": return "!="
        if opcode == "LT": return "<"
        if opcode == "LE": return "<="
        if opcode == "GT": return ">"
        if opcode == "GE": return ">="
        if opcode == "AND": return "&&"
        if opcode == "OR": return "||"
        return "" # Retorna vazio se o opcode não tiver um símbolo direto

# Classe TACGenerator: Gera o Código de Três Endereços (TAC) a partir da AST
class TACGenerator(ParseTreeVisitor):
    # Construtor da classe
    def __init__(self):
        self.tac_instructions = [] # Lista para armazenar as instruções TAC geradas
        self.temp_count = 0        # Contador para gerar nomes únicos para variáveis temporárias (_t0, _t1, ...)
        self.label_count = 0       # Contador para gerar nomes únicos para rótulos (L0, L1, ...)
        # self.scope_manager = {}    # Gerenciador de escopo (útil para análise semântica, mas não diretamente para TAC aqui)

    # Gera um novo operando temporário único
    def next_temp(self):
        self.temp_count += 1
        return TACOperand('TEMP', f'_t{self.temp_count-1}')

    # Gera um novo operando de rótulo único
    def next_label(self):
        self.label_count += 1
        return TACOperand('LABEL', f'L{self.label_count-1}')

    # Retorna a lista de instruções TAC como strings formatadas
    def get_tac_code(self):
        return [str(instr) for instr in self.tac_instructions]

    # --- Métodos Visitadores da Árvore Sintática (AST) ---
    # Estes métodos são chamados automaticamente pelo ANTLR Visitor
    # para percorrer a AST e gerar as instruções TAC correspondentes.

    # Visita o nó raiz 'programa'
    def visitPrograma(self, ctx: AraraParser.ProgramaContext):
        # Percorre todos os comandos dentro do programa
        for comando in ctx.comando():
            self.visit(comando) # Visita cada comando recursivamente
        return None

    # Visita o comando 'leia(ID)'
    def visitComandoLeia(self, ctx: AraraParser.ComandoLeiaContext):
        var_name = ctx.ID().getText() # Obtém o nome da variável a ser lida
        # Adiciona uma instrução TAC 'READ'
        self.tac_instructions.append(TACInstruction('READ', TACOperand('ID', var_name)))
        return None

    # Visita o comando 'escreva(expressao)'
    def visitComandoEscreva(self, ctx: AraraParser.ComandoEscrevaContext):
        # Visita a expressão para obter o operando resultante (pode ser literal, ID, temporário)
        expr_result_operand = self.visit(ctx.expressao())
        # Adiciona uma instrução TAC 'WRITE'
        self.tac_instructions.append(TACInstruction('WRITE', expr_result_operand))
        return None

    # Visita o comando de atribuição 'ID <- expressao'
    def visitComandoAtrib(self, ctx: AraraParser.ComandoAtribContext):
        var_name = ctx.ID().getText() # Obtém o nome da variável de destino
        # Visita a expressão para obter o operando resultante da expressão
        expr_result_operand = self.visit(ctx.expressao())
        # Adiciona uma instrução TAC 'ASSIGN'
        self.tac_instructions.append(TACInstruction('ASSIGN', TACOperand('ID', var_name), expr_result_operand))
        return None

    # Visita o comando 'declaracao' (inteiro ID; real ID;)
    def visitDeclaracao(self, ctx: AraraParser.DeclaracaoContext):
        # A declaração de variáveis geralmente não gera instruções TAC diretamente,
        # pois o TAC foca nas operações e não na definição de tipo ou alocação (que é feita no LLVM IR).
        # As informações de tipo são usadas na análise semântica e na alocação do LLVM IR.
        return None
    
    # Visita o comando condicional 'se (expressao) entao bloco [senao bloco] fimse'
    def visitCondicional(self, ctx: AraraParser.CondicionalContext):
        # Gera rótulos para o salto condicional (para o bloco ELSE) e para o final da estrutura (FIMSE)
        label_else = self.next_label()
        label_fimse = self.next_label()

        # Visita a expressão da condição para obter seu resultado booleano
        condition_operand = self.visit(ctx.expressao())

        # Adiciona instrução TAC 'IF_FALSE_GOTO': se a condição for falsa, salta para o label_else
        self.tac_instructions.append(TACInstruction('IF_FALSE_GOTO', label_else, condition_operand))

        # Visita o bloco THEN (bloco(0) na gramática)
        self.visit(ctx.bloco()) 

        # Se houver um bloco SENAO, adiciona um GOTO para pular o bloco ELSE após o THEN
        if ctx.cond_opc().SENAO():
            self.tac_instructions.append(TACInstruction('GOTO', label_fimse))

        # Adiciona o rótulo para o início do bloco ELSE
        self.tac_instructions.append(TACInstruction('LABEL', label_else))

        # Se houver um bloco SENAO, visita-o (bloco(1) na gramática)
        if ctx.cond_opc().SENAO():
            self.visit(ctx.cond_opc().bloco()) 

        # Adiciona o rótulo para o final da estrutura SE (FIMSE)
        self.tac_instructions.append(TACInstruction('LABEL', label_fimse))
        return None

    # Visita o comando de repetição 'enquanto (expressao) faca bloco fimenquanto'
    def visitRepeticao(self, ctx: AraraParser.RepeticaoContext):
        # Gera rótulos para o início do loop e o final do loop
        label_loop_start = self.next_label()
        label_loop_end = self.next_label()

        # Adiciona o rótulo de início do loop
        self.tac_instructions.append(TACInstruction('LABEL', label_loop_start))

        # Visita a expressão da condição do loop
        condition_operand = self.visit(ctx.expressao())

        # Adiciona instrução TAC 'IF_FALSE_GOTO': se a condição for falsa, salta para o final do loop
        self.tac_instructions.append(TACInstruction('IF_FALSE_GOTO', label_loop_end, condition_operand))

        # Visita o bloco de comandos do loop
        self.visit(ctx.bloco())

        # Adiciona um GOTO para voltar ao início do loop para reavaliar a condição
        self.tac_instructions.append(TACInstruction('GOTO', label_loop_start))

        # Adiciona o rótulo para o final do loop (FIMENQ)
        self.tac_instructions.append(TACInstruction('LABEL', label_loop_end))
        return None

    # Visita expressões
    def visitExpressao(self, ctx: AraraParser.ExpressaoContext):
        return self.visit(ctx.logica()) # Expressão é uma expressão lógica

    # Visita expressões lógicas (com &&, ||)
    def visitLogica(self, ctx: AraraParser.LogicaContext):
        left_operand = self.visit(ctx.comparacao()) # Visita o lado esquerdo (comparação)
        # Se houver um operador lógico e um lado direito
        if ctx.logica_suf() and ctx.logica_suf().OPLOG():
            op = ctx.logica_suf().OPLOG().getText() # Obtém o operador lógico (&& ou ||)
            right_operand = self.visit(ctx.logica_suf().comparacao()) # Visita o lado direito
            temp = self.next_temp() # Gera um temporário para o resultado da operação lógica
            # Adiciona a instrução TAC correspondente (AND ou OR)
            if op == '&&':
                self.tac_instructions.append(TACInstruction('AND', temp, left_operand, right_operand))
            elif op == '||':
                self.tac_instructions.append(TACInstruction('OR', temp, left_operand, right_operand))
            return temp # Retorna o temporário com o resultado
        return left_operand # Se não houver operador lógico, retorna o operando esquerdo

    # Visita expressões de comparação (com ==, !=, <, <=, >, >=)
    def visitComparacao(self, ctx: AraraParser.ComparacaoContext):
        left_operand = self.visit(ctx.soma()) # Visita o lado esquerdo (soma)
        # Se houver um operador de comparação
        if ctx.comparacao_suf() and ctx.comparacao_suf().OPCOMP():
            op = ctx.comparacao_suf().OPCOMP().getText() # Obtém o operador de comparação
            right_operand = self.visit(ctx.comparacao_suf().soma()) # Visita o lado direito
            temp = self.next_temp() # Gera um temporário para o resultado da comparação
            
            # Mapeia o operador de comparação para o opcode TAC
            tac_op = ""
            if op == '==': tac_op = "EQ"
            elif op == '!=': tac_op = "NEQ"
            elif op == '<': tac_op = "LT"
            elif op == '<=': tac_op = "LE"
            elif op == '>': tac_op = "GT"
            elif op == '>=': tac_op = "GE"
            
            # Adiciona a instrução TAC de comparação
            self.tac_instructions.append(TACInstruction(tac_op, temp, left_operand, right_operand))
            return temp # Retorna o temporário com o resultado booleano
        return left_operand # Se não houver operador de comparação, retorna o operando esquerdo

    # Visita expressões de soma/subtração (OPSUM: +, -)
    def visitSoma(self, ctx: AraraParser.SomaContext):
        result_operand = self.visit(ctx.termo()) # Visita o primeiro termo
        # Chama um método auxiliar para lidar com as operações de soma/subtração em cadeia
        return self.visitar_soma_suf(ctx.soma_suf(), result_operand)

    # Método auxiliar para visitar sufixos de soma/subtração recursivamente
    def visitar_soma_suf(self, ctx: AraraParser.Soma_sufContext, current_operand: TACOperand):
        if ctx.getChildCount() == 0: # Caso base da recursão: não há mais operadores de soma/subtração
            return current_operand

        op = ctx.OPSUM().getText() # Obtém o operador (+ ou -)
        next_operand = self.visit(ctx.termo()) # Visita o próximo termo
        temp = self.next_temp() # Gera um temporário para o resultado da operação
        
        # Adiciona a instrução TAC (ADD ou SUB)
        if op == '+':
            self.tac_instructions.append(TACInstruction('ADD', temp, current_operand, next_operand))
        elif op == '-':
            self.tac_instructions.append(TACInstruction('SUB', temp, current_operand, next_operand))
        
        # Continua a visita recursiva com o novo temporário como o operando atual
        return self.visitar_soma_suf(ctx.soma_suf(), temp)

    # Visita termos (multiplicação/divisão - OPMULT: *, /)
    def visitTermo(self, ctx: AraraParser.TermoContext):
        result_operand = self.visit(ctx.fator()) # Visita o primeiro fator
        # Chama um método auxiliar para lidar com as operações de multiplicação/divisão em cadeia
        return self._handle_arithmetic_suf(ctx.termo_suf(), result_operand)

    # Método auxiliar para visitar sufixos de termo recursivamente
    def visitar_termo_suf(self, ctx: AraraParser.Termo_sufContext, current_operand: TACOperand):
        if ctx.getChildCount() == 0: # Caso base da recursão
            return current_operand

        op = ctx.OPMULT().getText() # Obtém o operador (* ou /)
        next_operand = self.visit(ctx.fator()) # Visita o próximo fator
        temp = self.next_temp() # Gera um temporário para o resultado
        
        # Adiciona a instrução TAC (MUL ou DIV)
        if op == '*':
            self.tac_instructions.append(TACInstruction('MUL', temp, current_operand, next_operand))
        elif op == '/':
            self.tac_instructions.append(TACInstruction('DIV', temp, current_operand, next_operand))
        
        # Continua a visita recursiva
        return self.visitar_termo_suf(ctx.termo_suf(), temp)

    # Método auxiliar genérico para lidar com a recursão à direita de expressões aritméticas
    def _handle_arithmetic_suf(self, ctx, initial_operand):
        if isinstance(ctx, AraraParser.Soma_sufContext):
            return self.visitar_soma_suf(ctx, initial_operand)
        elif isinstance(ctx, AraraParser.Termo_sufContext):
            return self.visitar_termo_suf(ctx, initial_operand)
        return initial_operand

    # Visita fatores (números, strings, IDs, expressões entre parênteses, NOT)
    def visitFator(self, ctx: AraraParser.FatorContext):
        if ctx.INT(): # Se for um inteiro
            return TACOperand('LITERAL', int(ctx.INT().getText()))
        elif ctx.STRING(): # Se for uma string
            return TACOperand('LITERAL', ctx.STRING().getText())
        elif ctx.ID(): # Se for um identificador
            return TACOperand('ID', ctx.ID().getText())
        elif ctx.expressao(): # Se for uma expressão entre parênteses
            return self.visit(ctx.expressao())
        elif ctx.NOT(): # Se for uma operação NOT
            operand = self.visit(ctx.fator()) # Visita o fator após o NOT
            temp = self.next_temp() # Gera um temporário para o resultado do NOT
            self.tac_instructions.append(TACInstruction('NOT', temp, operand)) # Adiciona instrução TAC 'NOT'
            return temp
        return TACOperand('LITERAL', 'None') # Caso padrão, se nenhum tipo de fator for encontrado