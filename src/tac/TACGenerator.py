# Arquivo: src/tac/TACGenerator.py

from antlr4.tree.Tree import ParseTreeVisitor
from grammar.generated.AraraParser import AraraParser

class TACOperand:
    """Representa um operando em uma instrução TAC."""
    def __init__(self, type, value):
        self.type = type # Tipos: 'ID', 'TEMP', 'LITERAL', 'LABEL'
        self.value = value

    def __str__(self):
        return str(self.value)

    def is_literal(self):
        return self.type == 'LITERAL'

    def is_id(self):
        return self.type == 'ID'

    def is_temp(self):
        return self.type == 'TEMP'

    def is_label(self):
        return self.type == 'LABEL'

class TACInstruction:
    """Representa uma instrução de Código de Três Endereços (TAC)."""
    def __init__(self, opcode, result=None, arg1=None, arg2=None):
        self.opcode = opcode # Operador (ex: ASSIGN, ADD, SUB, IF_FALSE_GOTO, GOTO, LABEL, READ, WRITE)
        self.result = result # Operando de destino (TACOperand)
        self.arg1 = arg1     # Primeiro operando de argumento (TACOperand)
        self.arg2 = arg2     # Segundo operando de argumento (TACOperand)

    def __str__(self):
        if self.opcode == "LABEL":
            return f"{self.result.value}:"
        elif self.opcode == "ASSIGN":
            if self.arg1.is_literal() and self.arg2 is None:
                return f"{self.result.value} = {self.arg1.value}"
            return f"{self.result.value} = {self.arg1.value}"
        elif self.opcode in ["ADD", "SUB", "MUL", "DIV", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR"]:
            return f"{self.result.value} = {self.arg1.value} {self._get_symbol(self.opcode)} {self.arg2.value}"
        elif self.opcode == "NOT":
            return f"{self.result.value} = ! {self.arg1.value}"
        elif self.opcode == "IF_FALSE_GOTO":
            return f"IF_FALSE {self.arg1.value} GOTO {self.result.value}"
        elif self.opcode == "GOTO":
            return f"GOTO {self.result.value}"
        elif self.opcode == "READ":
            return f"READ {self.result.value}"
        elif self.opcode == "WRITE":
            return f"WRITE {self.result.value}"
        else:
            return f"{self.opcode} {self.result} {self.arg1} {self.arg2}"

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
        return ""

class TACGenerator(ParseTreeVisitor):
    def __init__(self):
        self.tac_instructions = []
        self.temp_count = 0
        self.label_count = 0
        self.scope_manager = {} # Para rastrear variáveis e seus tipos, se necessário para TAC específico de tipo

    def next_temp(self):
        self.temp_count += 1
        return TACOperand('TEMP', f'_t{self.temp_count-1}')

    def next_label(self):
        self.label_count += 1
        return TACOperand('LABEL', f'L{self.label_count-1}')

    def get_tac_code(self):
        return [str(instr) for instr in self.tac_instructions]

    # Visitadores para comandos
    def visitPrograma(self, ctx: AraraParser.ProgramaContext):
        for comando in ctx.comando():
            self.visit(comando)
        return None

    def visitComandoLeia(self, ctx: AraraParser.ComandoLeiaContext):
        var_name = ctx.ID().getText()
        self.tac_instructions.append(TACInstruction('READ', TACOperand('ID', var_name)))
        return None

    def visitComandoEscreva(self, ctx: AraraParser.ComandoEscrevaContext):
        # Visita a expressão para obter o operando do resultado
        expr_result_operand = self.visit(ctx.expressao())
        self.tac_instructions.append(TACInstruction('WRITE', expr_result_operand))
        return None

    def visitComandoAtrib(self, ctx: AraraParser.ComandoAtribContext):
        var_name = ctx.ID().getText()
        expr_result_operand = self.visit(ctx.expressao())
        self.tac_instructions.append(TACInstruction('ASSIGN', TACOperand('ID', var_name), expr_result_operand))
        return None

    def visitDeclaracao(self, ctx: AraraParser.DeclaracaoContext):
        # A declaração de variáveis geralmente não gera TAC diretamente,
        # mas pode ser usada para atualizar informações no gerenciador de escopo
        # se o TAC precisar de informações de tipo para alocação.
        # Por enquanto, não gera instrução TAC.
        return None
    
    def visitCondicional(self, ctx: AraraParser.CondicionalContext):
        # Gera rótulos para o salto condicional e o final da estrutura
        label_else = self.next_label()
        label_fimse = self.next_label()

        # Visita a expressão da condição
        condition_operand = self.visit(ctx.expressao())

        # IF_FALSE_GOTO para o label_else se a condição for falsa
        self.tac_instructions.append(TACInstruction('IF_FALSE_GOTO', label_else, condition_operand))

        # Visita o bloco THEN
        self.visit(ctx.bloco()) # Alterado de ctx.bloco(0) para ctx.bloco()

        # Se houver um bloco SENAO, salta para o FIMSE após o THEN
        if ctx.cond_opc().SENAO():
            self.tac_instructions.append(TACInstruction('GOTO', label_fimse))

        # Rótulo para o bloco ELSE (ou fim do IF se não houver ELSE)
        self.tac_instructions.append(TACInstruction('LABEL', label_else))

        # Se houver um bloco SENAO, visita-o
        if ctx.cond_opc().SENAO():
            self.visit(ctx.cond_opc().bloco()) # Alterado de ctx.bloco(1) para ctx.cond_opc().bloco()

        # Rótulo para o final da estrutura SE
        self.tac_instructions.append(TACInstruction('LABEL', label_fimse))
        return None

    def visitRepeticao(self, ctx: AraraParser.RepeticaoContext):
        # Gera rótulos para o início do loop e o final do loop
        label_loop_start = self.next_label()
        label_loop_end = self.next_label()

        # Adiciona o rótulo de início do loop
        self.tac_instructions.append(TACInstruction('LABEL', label_loop_start))

        # Visita a expressão da condição do loop
        condition_operand = self.visit(ctx.expressao())

        # IF_FALSE_GOTO para o final do loop se a condição for falsa
        self.tac_instructions.append(TACInstruction('IF_FALSE_GOTO', label_loop_end, condition_operand))

        # Visita o bloco do loop
        self.visit(ctx.bloco())

        # GOTO para o início do loop para reavaliar a condição
        self.tac_instructions.append(TACInstruction('GOTO', label_loop_start))

        # Rótulo para o final do loop
        self.tac_instructions.append(TACInstruction('LABEL', label_loop_end))
        return None


    # Visitadores para expressões
    def visitExpressao(self, ctx: AraraParser.ExpressaoContext):
        return self.visit(ctx.logica())

    def visitLogica(self, ctx: AraraParser.LogicaContext):
        left_operand = self.visit(ctx.comparacao())
        if ctx.logica_suf() and ctx.logica_suf().OPLOG():
            op = ctx.logica_suf().OPLOG().getText()
            right_operand = self.visit(ctx.logica_suf().comparacao())
            temp = self.next_temp()
            if op == '&&':
                self.tac_instructions.append(TACInstruction('AND', temp, left_operand, right_operand))
            elif op == '||':
                self.tac_instructions.append(TACInstruction('OR', temp, left_operand, right_operand))
            return temp
        return left_operand

    def visitComparacao(self, ctx: AraraParser.ComparacaoContext):
        left_operand = self.visit(ctx.soma())
        if ctx.comparacao_suf() and ctx.comparacao_suf().OPCOMP():
            op = ctx.comparacao_suf().OPCOMP().getText()
            right_operand = self.visit(ctx.comparacao_suf().soma())
            temp = self.next_temp()
            tac_op = ""
            if op == '==': tac_op = "EQ"
            elif op == '!=': tac_op = "NEQ"
            elif op == '<': tac_op = "LT"
            elif op == '<=': tac_op = "LE"
            elif op == '>': tac_op = "GT"
            elif op == '>=': tac_op = "GE"
            self.tac_instructions.append(TACInstruction(tac_op, temp, left_operand, right_operand))
            return temp
        return left_operand

    def visitSoma(self, ctx: AraraParser.SomaContext):
        result_operand = self.visit(ctx.termo())
        return self._handle_arithmetic_suf(ctx.soma_suf(), result_operand)

    def visitar_soma_suf(self, ctx: AraraParser.Soma_sufContext, current_operand: TACOperand):
        if ctx.getChildCount() == 0:
            return current_operand

        op = ctx.OPSUM().getText()
        next_operand = self.visit(ctx.termo())
        temp = self.next_temp()
        if op == '+':
            self.tac_instructions.append(TACInstruction('ADD', temp, current_operand, next_operand))
        elif op == '-':
            self.tac_instructions.append(TACInstruction('SUB', temp, current_operand, next_operand))
        # Continua visitando o sufixo com o novo temporário como operando atual
        return self.visitar_soma_suf(ctx.soma_suf(), temp)

    def visitTermo(self, ctx: AraraParser.TermoContext):
        result_operand = self.visit(ctx.fator())
        return self._handle_arithmetic_suf(ctx.termo_suf(), result_operand)

    def visitar_termo_suf(self, ctx: AraraParser.Termo_sufContext, current_operand: TACOperand):
        if ctx.getChildCount() == 0:
            return current_operand

        op = ctx.OPMULT().getText()
        next_operand = self.visit(ctx.fator())
        temp = self.next_temp()
        if op == '*':
            self.tac_instructions.append(TACInstruction('MUL', temp, current_operand, next_operand))
        elif op == '/':
            self.tac_instructions.append(TACInstruction('DIV', temp, current_operand, next_operand))
        return self.visitar_termo_suf(ctx.termo_suf(), temp)

    def _handle_arithmetic_suf(self, ctx, initial_operand):
        if isinstance(ctx, AraraParser.Soma_sufContext):
            return self.visitar_soma_suf(ctx, initial_operand)
        elif isinstance(ctx, AraraParser.Termo_sufContext):
            return self.visitar_termo_suf(ctx, initial_operand)
        return initial_operand


    def visitFator(self, ctx: AraraParser.FatorContext):
        if ctx.INT():
            return TACOperand('LITERAL', int(ctx.INT().getText()))
        elif ctx.STRING():
            return TACOperand('LITERAL', ctx.STRING().getText())
        elif ctx.ID():
            return TACOperand('ID', ctx.ID().getText())
        elif ctx.expressao():
            return self.visit(ctx.expressao())
        elif ctx.NOT():
            operand = self.visit(ctx.fator())
            temp = self.next_temp()
            self.tac_instructions.append(TACInstruction('NOT', temp, operand))
            return temp
        return TACOperand('LITERAL', 'None')