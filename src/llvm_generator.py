# Arquivo: src/llvm_generator.py

import json 
from src.tac.TACGenerator import TACOperand, TACInstruction 

class LLVMGenerator:
    # Construtor da classe LLVMGenerator
    def __init__(self, semantic_table={}): 
        self.module_header_lines = [
            '; ModuleID = "arara_program"',
            'source_filename = "arara.arara"',
            'target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"',
            'target triple = "x86_64-pc-linux-gnu"'
        ]

        # Lista para armazenar as definições de strings globais
        self.global_strings_defs = []

        # Lista para armazenar as declarações de funções externas (printf, scanf)
        self.function_declarations = [
            'declare i32 @printf(i8*, ...)', # Declaração da função printf
            'declare i32 @scanf(i8*, ...)' # Declaração da função scanf
        ]

        # Lista para armazenar os blocos básicos da função main
        self.main_function_blocks = [] 

        # Dicionário para mapear IDs de variáveis Arara para seus ponteiros e tipos LLVM IR
        self.var_map = {}  
        # Dicionário para mapear temporários TAC (_tX) para seus registradores e tipos LLVM IR
        self.temp_map = {} 
        # Dicionário para mapear rótulos TAC (LX) para seus nomes de blocos LLVM IR
        self.label_map = {} 

        # Contador para gerar nomes únicos de registradores temporários LLVM (ex: %temp0, %temp1)
        self.llvm_temp_counter = 0 

        # Contador para gerar nomes únicos para strings globais (@.str.0, @.str.1)
        self.string_count = 0

        # Contador para gerar nomes únicos para rótulos de blocos (ex: b0, b1)
        self.label_count = 0

        # Lista de instruções para o bloco básico atualmente em construção
        self.current_block_instructions = [] 

        # Nome do bloco básico atual que está sendo construído
        self.current_block_name = "entry" 

        # Dicionário para armazenar strings literais que já foram processadas, evitando duplicação
        self.string_literals = {} 

        # Tabela de símbolos semântica, passada do analisador semântico para inferência de tipos
        self.semantic_table = semantic_table 

    # Adiciona uma instrução LLVM ao bloco atual.
    def _add_instruction(self, instruction_line):
        self.current_block_instructions.append(f'  {instruction_line}')

    def _start_new_block(self, block_name):
        if self.current_block_instructions: 
            if not self.current_block_instructions[-1].strip().startswith(('br ', 'ret ')):
                 self._add_instruction(f'br label %{block_name}')

            self.main_function_blocks.append(f'{self.current_block_name}:')
            self.main_function_blocks.extend(self.current_block_instructions) 
            
        self.current_block_name = block_name
        self.current_block_instructions = []
        self.main_function_blocks.append(f'{block_name}:')

    # Retorna o tipo LLVM IR correspondente ao tipo Arara
    def _get_llvm_type(self, arara_type):
        return {
            "inteiro": "i32", # Inteiro de 32 bits
            "real": "float", # Ponto flutuante de 32 bits
            "booleano": "i1" # Booleano (1 bit)
        }.get(arara_type, "i8*") # Retorna ponteiro para byte (para strings) se o tipo não for encontrado

    # Adiciona uma string literal como uma constante global LLVM IR
    def _add_string_literal(self, s_content):
        if s_content not in self.string_literals:
            raw_bytes = s_content.encode('utf-8') + b'\x00'
            llvm_escaped_bytes = "".join(f"\\{b:02X}" for b in raw_bytes)
            byte_array_len = len(raw_bytes) 
            
            name = f"@.str.{self.string_count}"
            self.string_count += 1
            llvm_string = f'{name} = private unnamed_addr constant [{byte_array_len} x i8] c"{llvm_escaped_bytes}", align 1'
            
            self.global_strings_defs.append(llvm_string)
            self.string_literals[s_content] = (name, byte_array_len)
        return self.string_literals[s_content] # Retorna (nome, comprimento) da string processada

    # Gera nomes únicos para registradores LLVM (ex: %temp0).
    def next_llvm_reg(self):
        self.llvm_temp_counter += 1
        return f'%temp{self.llvm_temp_counter - 1}'

    # Gera nomes únicos para blocos LLVM (ex: block_0).
    def next_llvm_label_name(self):
        return f'block_{self.llvm_temp_counter}'

    # Traduz um operando TAC (literal, variável, temporário, rótulo) para um valor LLVM (registrador, literal, ou nome de rótulo).
    def _get_llvm_operand_value(self, tac_operand: 'TACOperand', target_llvm_type=None):
        val = tac_operand.value # O valor real do operando (ex: "a", 10, "_t0", "L1")

        if tac_operand.type == 'LITERAL':
            # Se for um literal numérico
            if isinstance(val, int) or str(val).isdigit(): 
                if target_llvm_type == "i1":
                    return "true" if int(val) != 0 else "false" 
                return str(val)
            
            # Se for um literal de string
            elif isinstance(val, str) and val.startswith('"'): 
                stripped_val = val.strip('"') 
                name, length = self._add_string_literal(stripped_val)
                string_ptr_reg = self.next_llvm_reg()
                self._add_instruction(f'  {string_ptr_reg} = getelementptr inbounds i8, [{length} x i8]* {name}, i64 0, i64 0')
                return string_ptr_reg

        # Se for um identificador
        elif tac_operand.type == 'ID': 
            var_name = val
            ptr_reg, actual_llvm_type = self.var_map[var_name] 
            load_reg = self.next_llvm_reg()
            self._add_instruction(f'  {load_reg} = load {actual_llvm_type}, {actual_llvm_type}* {ptr_reg}, align 4')
            
            if actual_llvm_type != target_llvm_type and target_llvm_type is not None:
                if actual_llvm_type == "i32" and target_llvm_type == "i1":
                    bool_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {bool_reg} = icmp ne i32 {load_reg}, 0')
                    return bool_reg
            return load_reg
        
        # Se for um temporário TAC (ex: _t0)
        elif tac_operand.type == 'TEMP': 
            temp_name = val
            val_reg, actual_llvm_type = self.temp_map.get(temp_name, (f"%{temp_name}", "i32"))
            
            # Conversão de tipo se necessário (i32 para i1)
            if actual_llvm_type != target_llvm_type and target_llvm_type is not None:
                if actual_llvm_type == "i32" and target_llvm_type == "i1":
                    bool_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {bool_reg} = icmp ne i32 {val_reg}, 0')
                    return bool_reg
            return val_reg
        
        # Se for um rótulo (Label)
        elif tac_operand.type == 'LABEL': 
            return tac_operand.value

        return "ERROR_OPERAND"
    
    # Método principal para gerar o código LLVM IR a partir das instruções TAC
    def generate(self, tac_instructions: list['TACInstruction']): 
        # Reinicializa o estado do gerador para cada nova chamada, mantendo a tabela de símbolos
        self.__init__(self.semantic_table) 

        # --- FASE DE PRÉ-PROCESSAMENTO: Coleta de Strings e Mapeamento de Rótulos ---
        # Percorre as instruções TAC para identificar strings literais e rótulos usados
        for instr in tac_instructions:
            # Se for um comando WRITE com string literal
            if instr.opcode == "WRITE":
                if instr.result and instr.result.type == 'LITERAL' and isinstance(instr.result.value, str) and instr.result.value.startswith('"'):
                    # Adiciona uma quebra de linha à string para impressão (ex: "Hello\n")
                    string_content_with_newline = instr.result.value.strip('"') + "\n"
                    self._add_string_literal(string_content_with_newline)
                # Adiciona formatos padrão para printf (números com quebra de linha)
                self._add_string_literal("%d\n") 
            # Se for um comando READ, adiciona formato para scanf (números sem quebra de linha)
            elif instr.opcode == "READ":
                 self._add_string_literal("%d") 
            
            # Se for uma instrução LABEL, mapeia o rótulo TAC para o nome do bloco LLVM
            if instr.opcode == "LABEL": 
                label_name = instr.result.value 
                self.label_map[label_name] = label_name 

        # --- FASE DE GERAÇÃO DA FUNÇÃO main ---
        # Inicia a definição da função main
        self.main_function_blocks.append('define i32 @main() {')
        # Inicia o bloco de entrada (entry)
        self._start_new_block("entry") 
        
        # Coleta todas as variáveis a serem alocadas (IDs que são resultado, arg1 ou arg2)
        variables_to_allocate = set()
        for instr in tac_instructions:
            if instr.opcode == "DECL" or instr.opcode == "READ":
                variables_to_allocate.add(instr.result.value)
            elif instr.opcode == "ASSIGN":
                if instr.result.type == 'ID':
                    variables_to_allocate.add(instr.result.value)

        # Aloca memória para cada variável no bloco de entrada
        for var_name in sorted(list(variables_to_allocate)):
            # Tenta pegar o tipo da tabela semântica, senão assume "inteiro"
            arara_type = self.semantic_table.get(var_name, "inteiro") 
            llvm_type = self._get_llvm_type(arara_type) # Converte para tipo LLVM
            ptr_reg = f'%{var_name}_ptr' # Gera nome de registrador para o ponteiro
            self._add_instruction(f'  {ptr_reg} = alloca {llvm_type}, align 4') # Aloca memória
            self.var_map[var_name] = (ptr_reg, llvm_type) # Mapeia variável para seu ponteiro e tipo
        
        # Garante que o bloco de entrada (entry) ramifique para o primeiro bloco de código real
        first_code_label = "start_code_block"
        if tac_instructions and tac_instructions[0].opcode == "LABEL":
            first_code_label = tac_instructions[0].result.value
        else:
            # Insere uma instrução LABEL no início do TAC se não houver, para ter um destino de branch
            tac_instructions.insert(0, TACInstruction("LABEL", TACOperand("LABEL", first_code_label)))
            self.label_map[first_code_label] = first_code_label # Garante que o label está mapeado


        self._add_instruction(f'  br label %{first_code_label}') # Ramifica do entry para o primeiro bloco de código

        # --- FASE DE TRADUÇÃO PRINCIPAL: Processa cada instrução TAC ---
        for i, instr in enumerate(tac_instructions):
            op = instr.opcode
            result_operand = instr.result
            arg1_operand = instr.arg1
            arg2_operand = instr.arg2

            # TRADUÇÃO DE ASSIGN (Atribuição: DEST = FONTE)
            if op == "ASSIGN": 
                dest_operand = result_operand
                src_operand = arg1_operand
                
                assign_llvm_type = "i32" # Tipo padrão para atribuição
                # Infere o tipo de atribuição a partir do destino ou da fonte
                if dest_operand.type == 'ID' and dest_operand.value in self.var_map:
                    assign_llvm_type = self.var_map[dest_operand.value][1] 
                elif src_operand.type == 'TEMP' and src_operand.value in self.temp_map:
                    assign_llvm_type = self.temp_map[src_operand.value][1] 

                llvm_src_val = self._get_llvm_operand_value(src_operand, assign_llvm_type) # Obtém o valor da fonte
                
                if dest_operand.type == 'ID': # Se o destino é uma variável de programa (ID)
                    ptr_reg, _ = self.var_map[dest_operand.value]
                    self._add_instruction(f'  store {assign_llvm_type} {llvm_src_val}, {assign_llvm_type}* {ptr_reg}, align 4') # Armazena na memória
                elif dest_operand.type == 'TEMP': # Se o destino é um temporário TAC
                    # Mapeia o temporário TAC para o registrador LLVM que contém o valor
                    self.temp_map[dest_operand.value] = (llvm_src_val, assign_llvm_type) 

            # TRADUÇÃO DE OPERAÇÕES ARITMÉTICAS (ADD, SUB, MUL, DIV)
            elif op in ["ADD", "SUB", "MUL", "DIV"]: 
                op_result_llvm_type = "i32" # Assumimos i32 para resultados aritméticos
                llvm_arg1_val = self._get_llvm_operand_value(arg1_operand, op_result_llvm_type)
                llvm_arg2_val = self._get_llvm_operand_value(arg2_operand, op_result_llvm_type)
                
                # Mapeia o opcode TAC para a instrução LLVM IR
                llvm_op_str = {"ADD": "add", "SUB": "sub", "MUL": "mul", "DIV": "sdiv"}[op]
                
                target_reg = f'%{result_operand.value}' # Registrador para o resultado
                self._add_instruction(f'  {target_reg} = {llvm_op_str} {op_result_llvm_type} {llvm_arg1_val}, {llvm_arg2_val}')
                self.temp_map[result_operand.value] = (target_reg, op_result_llvm_type) # Armazena o temporário e seu tipo

            # TRADUÇÃO DE OPERAÇÕES DE COMPARAÇÃO E LÓGICAS (IGNORADAS NO MODO SIMPLIFICADO)
            elif op in ["EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR"]:
                # Estes foram removidos no modo simplificado. Se forem reintroduzidos, a lógica virá aqui.
                op_result_llvm_type = "i1" 
                # ... (Lógica de getelementptr e call para estas operações) ...
                pass 

            # TRADUÇÃO DE NOT (IGNORADO NO MODO SIMPLIFICADO)
            elif op == "NOT": 
                # Este foi removido no modo simplificado. Se for reintroduzido, a lógica virá aqui.
                op_result_llvm_type = "i1"
                # ... (Lógica de getelementptr e call para esta operação) ...
                pass 

            # TRADUÇÃO DE READ (Leitura de Entrada)
            elif op == "READ":
                var_operand = result_operand # O operando de resultado contém a variável
                var_name = var_operand.value
                ptr_reg, llvm_type = self.var_map.get(var_name, (None, None))
                if ptr_reg:
                    # Obtém ponteiro para a string de formato "%d"
                    format_str_name, format_str_len = self.string_literals["%d"] 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {fmt_ptr_reg} = getelementptr inbounds i8, [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0') 
                    # Chama scanf para ler o valor no ponteiro da variável
                    self._add_instruction(f'  %call_scanf_{self.next_llvm_reg()} = call i32 (i8*, ...) @scanf(i8* {fmt_ptr_reg}, {llvm_type}* {ptr_reg})') 

            # TRADUÇÃO DE WRITE (Escrita de Saída)
            elif op == "WRITE":
                val_operand = result_operand # O operando de resultado contém o valor a ser escrito
                
                # Se o valor a ser escrito é uma string literal
                if val_operand.type == 'LITERAL' and isinstance(val_operand.value, str) and val_operand.value.startswith('"'):
                    actual_string_with_newline = val_operand.value.strip('"') + "\n" # Adiciona newline
                    format_str_name, format_str_len = self._add_string_literal(actual_string_with_newline) # Adiciona string global
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {fmt_ptr_reg} = getelementptr inbounds i8, [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0') 
                    self._add_instruction(f'  %call_printf_{self.next_llvm_reg()} = call i32 (i8*, ...) @printf(i8* {fmt_ptr_reg})')
                # Se o valor a ser escrito é uma variável ou temporário (assumimos i32 para impressão)
                else: 
                    operand_llvm_type = "i32" 
                    if val_operand.type == 'ID' and val_operand.value in self.var_map:
                        operand_llvm_type = self.var_map[val_operand.value][1]
                    elif val_operand.type == 'TEMP' and val_operand.value in self.temp_map:
                        operand_llvm_type = self.temp_map[val_operand.value][1]

                    llvm_value = self._get_llvm_operand_value(val_operand, operand_llvm_type) # Obtém o valor
                    
                    format_str_name, format_str_len = self.string_literals["%d\n"] # Formato para inteiro com newline
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {fmt_ptr_reg} = getelementptr inbounds i8, [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0') 
                    self._add_instruction(f'  %call_printf_{self.next_llvm_reg()} = call i32 (i8*, ...) @printf(i8* {fmt_ptr_reg}, i32 {llvm_value})')

            # TRADUÇÃO DE CONTROLE DE FLUXO
            elif op == "LABEL" or op == "GOTO" or op == "IF_FALSE_GOTO" or op in ["EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR", "NOT"] :
                pass
            # TRADUÇÃO DE DECL (IGNORADO NO MODO SIMPLIFICADO, TRATADO NA ALOCAÇÃO INICIAL)
            elif op == "DECL": 
                pass 
            
            else:
                # Se uma instrução TAC não for reconhecida, adicionamos um comentário (para depuração)
                self._add_instruction(f'; Instrução TAC não implementada ou não reconhecida: {op}')

        # Garante que o último bloco da função main termine com um 'ret' se não houver um 'br' ou 'ret' explícito
        if self.current_block_instructions and not self.current_block_instructions[-1].strip().startswith(('ret ', 'br ')):
            self._add_instruction('  ret i32 0')
        # Caso o bloco esteja vazio (após um branch ou se o programa não tem instruções)
        elif not self.current_block_instructions: 
            self._add_instruction('  ret i32 0')

        # Finaliza o bloco atual e adiciona à lista de blocos da função main
        self.main_function_blocks.append(f'{self.current_block_name}:')
        self.main_function_blocks.extend(self.current_block_instructions)
        self.main_function_blocks.append('}')

        # --- FASE DE MONTAGEM FINAL DO CÓDIGO LLVM IR ---
        final_llvm_output = []
        final_llvm_output.extend(self.module_header_lines) # Adiciona o cabeçalho
        final_llvm_output.append('') # Adiciona linha em branco após o cabeçalho
        final_llvm_output.extend(self.global_strings_defs) # Adiciona as definições de strings globais
        final_llvm_output.append('') # Adiciona linha em branco após as strings
        final_llvm_output.extend(self.function_declarations) # Adiciona as declarações de funções externas
        final_llvm_output.append('') # Adiciona linha em branco após as declarações
        final_llvm_output.extend(self.main_function_blocks) # Adiciona os blocos da função main

        return "\n".join(final_llvm_output)