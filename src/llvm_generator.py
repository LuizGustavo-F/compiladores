# Arquivo: src/llvm_generator.py

import json
from src.tac.TACGenerator import TACOperand, TACInstruction 

class LLVMGenerator:
    def __init__(self, semantic_table={}): 
        self.module_header_lines = [
            '; ModuleID = "arara_program"',
            'source_filename = "arara.arara"',
            'target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"',
            'target triple = "x86_64-pc-linux-gnu"'
        ]
        self.global_strings_defs = [] 
        # CORREÇÃO AQUI: Declara scanf sem __isoc99_
        self.function_declarations = [
            'declare i32 @printf(i8*, ...)',
            'declare i32 @scanf(i8*, ...)' # Mudado de __isoc99_scanf para scanf
        ]
        self.main_function_blocks = [] 

        self.var_map = {}  
        self.temp_map = {} 
        self.label_map = {} 

        self.llvm_temp_counter = 0 
        self.string_count = 0

        self.current_block_instructions = [] 
        self.current_block_name = "entry" 

        self.string_literals = {} 
        self.semantic_table = semantic_table 

    def _add_instruction(self, instruction_line):
        self.current_block_instructions.append(f'  {instruction_line}')

    def _start_new_block(self, block_name):
        if self.current_block_instructions: 
            self.main_function_blocks.append(f'{self.current_block_name}:')
            self.main_function_blocks.extend(self.current_block_instructions)
        self.current_block_name = block_name
        self.current_block_instructions = [] 

    def _get_llvm_type(self, arara_type):
        return {
            "inteiro": "i32",
            "real": "float",
            "booleano": "i1"
        }.get(arara_type, "i8*")

    def _add_string_literal(self, s_content):
        if s_content not in self.string_literals:
            raw_bytes = s_content.encode('utf-8') + b'\x00'
            llvm_escaped_bytes = "".join(f"\\{b:02X}" for b in raw_bytes)
            byte_array_len = len(raw_bytes) 
            
            name = f"@.str.{self.string_count}"
            llvm_string = f'{name} = private unnamed_addr constant [{byte_array_len} x i8] c"{llvm_escaped_bytes}", align 1'
            
            self.global_strings_defs.append(llvm_string)
            self.string_literals[s_content] = (name, byte_array_len)
            self.string_count += 1
        return self.string_literals[s_content]

    def next_llvm_reg(self):
        self.llvm_temp_counter += 1
        return f'%temp{self.llvm_temp_counter - 1}'
    
    def next_llvm_label_name(self):
        return f'block_{self.llvm_temp_counter}' 

    # --- MÉTODO _get_llvm_operand_value ATUALIZADO (getelementptr para strings literais com i64) ---
    def _get_llvm_operand_value(self, tac_operand: 'TACOperand', target_llvm_type=None):
        val = tac_operand.value 

        if tac_operand.type == 'LITERAL':
            if isinstance(val, int) or str(val).isdigit(): 
                if target_llvm_type == "i1":
                    return "true" if int(val) != 0 else "false" 
                return str(val) 
            elif isinstance(val, str) and val.startswith('"'): 
                stripped_val = val.strip('"')
                name, length = self._add_string_literal(stripped_val)
                string_ptr_reg = self.next_llvm_reg()
                self._add_instruction(f'  {string_ptr_reg} = getelementptr inbounds i8, [{length} x i8]* {name}, i64 0, i64 0') 
                return string_ptr_reg

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

        elif tac_operand.type == 'TEMP': 
            temp_name = val 
            val_reg, actual_llvm_type = self.temp_map.get(temp_name, (f"%{temp_name}", "i32")) 
            
            if actual_llvm_type != target_llvm_type and target_llvm_type is not None:
                if actual_llvm_type == "i32" and target_llvm_type == "i1":
                    bool_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {bool_reg} = icmp ne i32 {val_reg}, 0')
                    return bool_reg
            return val_reg
        
        elif tac_operand.type == 'LABEL': 
            return tac_operand.value 

        return "ERROR_OPERAND" 

    # --- MÉTODO generate (COM TODAS AS CORREÇÕES FINAIS) ---
    def generate(self, tac_instructions: list['TACInstruction']): 
        self.__init__(self.semantic_table) 

        # 1. Cabeçalho do Módulo LLVM (definido no __init__)
        # 2. Declarações de Funções Externas (definido no __init__)
        
        # 3. Pré-processamento: Coletar strings e mapear rótulos TAC para nomes de blocos LLVM IR
        for instr in tac_instructions:
            if instr.opcode == "WRITE":
                if instr.result and instr.result.type == 'LITERAL' and isinstance(instr.result.value, str) and instr.result.value.startswith('"'):
                    string_content_with_newline = instr.result.value.strip('"') + "\n"
                    self._add_string_literal(string_content_with_newline)
                self._add_string_literal("%d\n") # Formato para imprimir inteiros com newline
            elif instr.opcode == "READ":
                 self._add_string_literal("%d") # Formato para ler inteiros (sem newline)
            
            if instr.opcode == "LABEL": 
                self.label_map[instr.result.value] = instr.result.value 

        # 4. Início da função principal (main)
        self.main_function_blocks.append('define i32 @main() {')
        self._start_new_block("entry") 
        
        # Alocação de variáveis Arara (somente no bloco de entrada)
        variables_to_allocate = set()
        for instr in tac_instructions:
            if instr.opcode == "DECL" or instr.opcode == "READ":
                variables_to_allocate.add(instr.result.value)
            elif instr.opcode == "ASSIGN":
                if instr.result.type == 'ID':
                    variables_to_allocate.add(instr.result.value)

        for var_name in sorted(list(variables_to_allocate)):
            arara_type = self.semantic_table.get(var_name, "inteiro") 
            llvm_type = self._get_llvm_type(arara_type)
            ptr_reg = f'%{var_name}_ptr'
            self._add_instruction(f'  {ptr_reg} = alloca {llvm_type}, align 4')
            self.var_map[var_name] = (ptr_reg, llvm_type) 

        # 5. Processar instruções TAC e preencher os blocos básicos
        for i, instr in enumerate(tac_instructions):
            op = instr.opcode
            result_operand = instr.result
            arg1_operand = instr.arg1
            arg2_operand = instr.arg2

            if op == "ASSIGN": 
                dest_operand = result_operand
                src_operand = arg1_operand
                
                assign_llvm_type = "i32" 
                if dest_operand.type == 'ID' and dest_operand.value in self.var_map:
                    assign_llvm_type = self.var_map[dest_operand.value][1] 
                elif src_operand.type == 'TEMP' and src_operand.value in self.temp_map:
                    assign_llvm_type = self.temp_map[src_operand.value][1] 


                llvm_src_val = self._get_llvm_operand_value(src_operand, assign_llvm_type)
                
                if dest_operand.type == 'ID': 
                    ptr_reg, _ = self.var_map[dest_operand.value]
                    self._add_instruction(f'  store {assign_llvm_type} {llvm_src_val}, {assign_llvm_type}* {ptr_reg}, align 4')
                elif dest_operand.type == 'TEMP': 
                    target_reg = f'%{dest_operand.value}' 
                    self.temp_map[dest_operand.value] = (llvm_src_val, assign_llvm_type) 

            elif op in ["ADD", "SUB", "MUL", "DIV"]: 
                op_result_llvm_type = "i32" 
                llvm_arg1_val = self._get_llvm_operand_value(arg1_operand, op_result_llvm_type)
                llvm_arg2_val = self._get_llvm_operand_value(arg2_operand, op_result_llvm_type)
                
                llvm_op_str = {"ADD": "add", "SUB": "sub", "MUL": "mul", "DIV": "sdiv"}[op]
                
                target_reg = f'%{result_operand.value}'
                self._add_instruction(f'  {target_reg} = {llvm_op_str} {op_result_llvm_type} {llvm_arg1_val}, {llvm_arg2_val}')
                self.temp_map[result_operand.value] = (target_reg, op_result_llvm_type)

            elif op in ["EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR"]:
                op_result_llvm_type = "i1" 

                llvm_arg1_val = self._get_llvm_operand_value(arg1_operand, "i32") 
                llvm_arg2_val = self._get_llvm_operand_value(arg2_operand, "i32") 

                llvm_op_str = ""
                if op == "EQ": llvm_op_str = "icmp eq"
                elif op == "NEQ": llvm_op_str = "icmp ne"
                elif op == "LT": llvm_op_str = "icmp slt"
                elif op == "LE": llvm_op_str = "icmp sle"
                elif op == "GT": llvm_op_str = "icmp sgt"
                elif op == "GE": llvm_op_str = "icmp sge"
                elif op == "AND": llvm_op_str = "and"
                elif op == "OR": llvm_op_str = "or"
                
                target_reg = f'%{result_operand.value}'
                if op in ["AND", "OR"]: 
                     self._add_instruction(f'  {target_reg} = {llvm_op_str} i1 {llvm_arg1_val}, {llvm_arg2_val}')
                else: 
                     self._add_instruction(f'  {target_reg} = {llvm_op_str} i32 {llvm_arg1_val}, {llvm_arg2_val}')
                
                self.temp_map[result_operand.value] = (target_reg, op_result_llvm_type)

            elif op == "NOT": 
                op_result_llvm_type = "i1"
                llvm_arg1_val = self._get_llvm_operand_value(arg1_operand, op_result_llvm_type)
                
                target_reg = f'%{result_operand.value}'
                self._add_instruction(f'  {target_reg} = xor i1 {llvm_arg1_val}, true') 
                self.temp_map[result_operand.value] = (target_reg, op_result_llvm_type)

            elif op == "READ":
                var_operand = result_operand 
                var_name = var_operand.value
                ptr_reg, llvm_type = self.var_map.get(var_name, (None, None))
                if ptr_reg:
                    format_str_name, format_str_len = self.string_literals["%d"] 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {fmt_ptr_reg} = getelementptr inbounds i8, [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0') 

            elif op == "WRITE":
                val_operand = result_operand 
                
                if val_operand.type == 'LITERAL' and isinstance(val_operand.value, str) and val_operand.value.startswith('"'):
                    actual_string_with_newline = val_operand.value.strip('"') + "\n"
                    format_str_name, format_str_len = self.string_literals[actual_string_with_newline] 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {fmt_ptr_reg} = getelementptr inbounds i8, [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0') 
                    self._add_instruction(f'  %call_printf_{self.next_llvm_reg()} = call i32 (i8*, ...) @printf(i8* {fmt_ptr_reg})')
                else: 
                    operand_llvm_type = "i32" 
                    if val_operand.type == 'ID' and val_operand.value in self.var_map:
                        operand_llvm_type = self.var_map[val_operand.value][1]
                    elif val_operand.type == 'TEMP' and val_operand.value in self.temp_map:
                        operand_llvm_type = self.temp_map[val_operand.value][1]

                    llvm_value = self._get_llvm_operand_value(val_operand, operand_llvm_type)
                    
                    format_str_name, format_str_len = self.string_literals["%d\n"] 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'  {fmt_ptr_reg} = getelementptr inbounds i8, [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0') 
                    self._add_instruction(f'  %call_printf_{self.next_llvm_reg()} = call i32 (i8*, ...) @printf(i8* {fmt_ptr_reg}, i32 {llvm_value})')

            elif op == "LABEL" or op == "GOTO" or op == "IF_FALSE_GOTO" or op in ["EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR", "NOT"] :
                pass
            elif op == "DECL": 
                pass 
            
            else:
                self._add_instruction(f'; Instrução TAC não implementada ou não reconhecida: {op}')

        if self.current_block_instructions and not self.current_block_instructions[-1].strip().startswith(('ret', 'br')):
            self._add_instruction('  ret i32 0')
        elif not self.current_block_instructions: 
            self._add_instruction('  ret i32 0')

        if self.current_block_name not in [block_name.split(':')[0] for block_name in self.main_function_blocks if ':' in block_name]:
            self.main_function_blocks.append(f'{self.current_block_name}:')
        self.main_function_blocks.extend(self.current_block_instructions)

        self.main_function_blocks.append('}') 

        final_llvm_output = []
        final_llvm_output.extend(self.module_header_lines)
        final_llvm_output.append('') 
        final_llvm_output.extend(self.global_strings_defs) 
        final_llvm_output.append('') 
        final_llvm_output.extend(self.function_declarations) 
        final_llvm_output.append('') 
        final_llvm_output.extend(self.main_function_blocks) 

        return "\n".join(final_llvm_output)