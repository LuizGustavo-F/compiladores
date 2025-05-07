from antlr4 import *
from generated.AraraParser import AraraParser
from generated.AraraVisitor import AraraVisitor
from src.error_handler import RuntimeErrorException

class Interpreter(AraraVisitor):
    def __init__(self):
        self.memory = {}  # Armazena as variáveis e seus valores
        self.functions = {}  # Para futura implementação de funções
        self.logger = logging.getLogger('Interpreter')

    def visitPrograma(self, ctx: AraraParser.ProgramaContext):
        self.logger.info("Iniciando interpretação do programa")
        try:
            for cmd in ctx.comando():
                self.visit(cmd)
        except RuntimeErrorException as e:
            self.logger.error(f"Erro em tempo de execução: {e}")
            raise

    def visitComando(self, ctx: AraraParser.ComandoContext):
        if ctx.getChildCount() == 0:
            return
        
        self.logger.debug(f"Visitando comando: {ctx.getText()}")
        
        if ctx.leia():
            self.visitLeia(ctx.leia())
        elif ctx.escreva():
            self.visitEscreva(ctx.escreva())
        elif ctx.atribuicao():
            self.visitAtribuicao(ctx.atribuicao())
        elif ctx.condicional():
            self.visitCondicional(ctx.condicional())
        elif ctx.repeticao():
            self.visitRepeticao(ctx.repeticao())

    def visitLeia(self, ctx: AraraParser.LeiaContext):
        var_name = ctx.ID().getText()
        try:
            value = input("> ")  # Lê entrada do usuário
            try:
                # Tenta converter para inteiro se possível
                self.memory[var_name] = int(value)
            except ValueError:
                # Se não for número, armazena como string (sem as aspas)
                self.memory[var_name] = value.strip('"')
            self.logger.info(f"Leitura: {var_name} = {self.memory[var_name]}")
        except Exception as e:
            raise RuntimeErrorException(f"Erro na leitura da variável {var_name}: {str(e)}")

    def visitEscreva(self, ctx: AraraParser.EscrevaContext):
        try:
            value = self.visitExpressao(ctx.expressao())
            print(value)
            self.logger.info(f"Escrita: {value}")
        except Exception as e:
            raise RuntimeErrorException(f"Erro ao escrever: {str(e)}")

    def visitAtribuicao(self, ctx: AraraParser.AtribuicaoContext):
        var_name = ctx.ID().getText()
        try:
            value = self.visitExpressao(ctx.expressao())
            self.memory[var_name] = value
            self.logger.info(f"Atribuição: {var_name} = {value}")
        except Exception as e:
            raise RuntimeErrorException(f"Erro na atribuição de {var_name}: {str(e)}")

    def visitCondicional(self, ctx: AraraParser.CondicionalContext):
        try:
            condition = self.visitExpressao(ctx.expressao())
            self.logger.debug(f"Condicional: condição = {condition}")
            
            if condition:
                self.visitBloco(ctx.bloco(0))
            elif ctx.cond_opc().senao():
                self.visitBloco(ctx.bloco(1))
        except Exception as e:
            raise RuntimeErrorException(f"Erro na condicional: {str(e)}")

    def visitRepeticao(self, ctx: AraraParser.RepeticaoContext):
        try:
            while self.visitExpressao(ctx.expressao()):
                self.logger.debug("Executando iteração do loop")
                self.visitBloco(ctx.bloco())
        except Exception as e:
            raise RuntimeErrorException(f"Erro no loop: {str(e)}")

    def visitBloco(self, ctx: AraraParser.BlocoContext):
        for cmd in ctx.comando():
            self.visit(cmd)

    def visitExpressao(self, ctx: AraraParser.ExpressaoContext):
        return self.visitLogica(ctx.logica())

    def visitLogica(self, ctx: AraraParser.LogicaContext):
        left = self.visitComparacao(ctx.comparacao())
        if ctx.logica_suf().OPLOG():
            op = ctx.logica_suf().OPLOG().getText()
            right = self.visitLogica_suf(ctx.logica_suf())
            if op == '&&':
                return left and right
            elif op == '||':
                return left or right
        return left

    def visitLogica_suf(self, ctx: AraraParser.Logica_sufContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visitComparacao(ctx.comparacao())

    def visitComparacao(self, ctx: AraraParser.ComparacaoContext):
        left = self.visitSoma(ctx.soma())
        if ctx.comparacao_suf().OPCOMP():
            op = ctx.comparacao_suf().OPCOMP().getText()
            right = self.visitSoma(ctx.comparacao_suf().soma())
            if op == '==':
                return left == right
            elif op == '!=':
                return left != right
            elif op == '<':
                return left < right
            elif op == '<=':
                return left <= right
            elif op == '>':
                return left > right
            elif op == '>=':
                return left >= right
        return left

    def visitSoma(self, ctx: AraraParser.SomaContext):
        left = self.visitTermo(ctx.termo())
        if ctx.soma_suf().OPSUM():
            op = ctx.soma_suf().OPSUM().getText()
            right = self.visitSoma_suf(ctx.soma_suf())
            if op == '+':
                # Concatenação de strings
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            elif op == '-':
                return left - right
        return left

    def visitSoma_suf(self, ctx: AraraParser.Soma_sufContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visitTermo(ctx.termo())

    def visitTermo(self, ctx: AraraParser.TermoContext):
        left = self.visitFator(ctx.fator())
        if ctx.termo_suf().OPMULT():
            op = ctx.termo_suf().OPMULT().getText()
            right = self.visitTermo_suf(ctx.termo_suf())
            if op == '*':
                return left * right
            elif op == '/':
                if right == 0:
                    raise RuntimeErrorException("Divisão por zero")
                return left / right
        return left

    def visitTermo_suf(self, ctx: AraraParser.Termo_sufContext):
        if ctx.getChildCount() == 0:
            return None
        return self.visitFator(ctx.fator())

    def visitFator(self, ctx: AraraParser.FatorContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove as aspas
        elif ctx.ID():
            var_name = ctx.ID().getText()
            if var_name in self.memory:
                return self.memory[var_name]
            else:
                raise RuntimeErrorException(f"Variável '{var_name}' não definida")
        elif ctx.expressao():
            return self.visit(ctx.expressao())
        elif ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '!':  # Operador de negação
            return not self.visitFator(ctx.fator(0))
        else:
            raise RuntimeErrorException("Expressão inválida")