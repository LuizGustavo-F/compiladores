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
        self.function_declarations = [
            'declare i32 @printf(i8*, ...)',
            'declare i32 @scanf(i8*, ...)'
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
        self.current_block_instructions.append(f'    {instruction_line}')

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
            array_type = f"[{byte_array_len} x i8]"
            llvm_string = f'{name} = private unnamed_addr constant {array_type} c"{llvm_escaped_bytes}", align 1'
            
            self.global_strings_defs.append(llvm_string)
            self.string_literals[s_content] = (name, array_type)
            self.string_count += 1
        return self.string_literals[s_content]

    def next_llvm_reg(self):
        self.llvm_temp_counter += 1
        return f'%temp{self.llvm_temp_counter - 1}'
    
    def next_llvm_label_name(self):
        return f'block_{self.llvm_temp_counter}' 

    def _get_llvm_operand_value(self, tac_operand: 'TACOperand', target_llvm_type=None):
        val = tac_operand.value 
        if tac_operand.type == 'LITERAL' and isinstance(val, str) and val.startswith('"'): 
            stripped_val = val.strip('"')
            name, array_type = self._add_string_literal(stripped_val)
            string_ptr_reg = self.next_llvm_reg()
            self._add_instruction(f'{string_ptr_reg} = getelementptr inbounds {array_type}, {array_type}* {name}, i64 0, i64 0') 
            return string_ptr_reg
        elif tac_operand.type == 'LITERAL':
            if isinstance(val, int) or str(val).isdigit(): 
                if target_llvm_type == "i1": return "true" if int(val) != 0 else "false" 
                return str(val) 
        elif tac_operand.type == 'ID': 
            var_name = val 
            ptr_reg, actual_llvm_type = self.var_map[var_name] 
            load_reg = self.next_llvm_reg()
            self._add_instruction(f'{load_reg} = load {actual_llvm_type}, {actual_llvm_type}* {ptr_reg}, align 4')
            return load_reg
        elif tac_operand.type == 'TEMP': 
            temp_name = val 
            val_reg, _ = self.temp_map.get(temp_name, (f"%{temp_name}", "i32")) 
            return val_reg
        return "ERROR_OPERAND" 

    def generate(self, tac_instructions: list['TACInstruction']): 
        self.__init__(self.semantic_table) 

        for instr in tac_instructions:
            if instr.opcode == "WRITE":
                if instr.result and instr.result.type == 'LITERAL' and isinstance(instr.result.value, str):
                    string_content_with_newline = instr.result.value.strip('"') + "\n"
                    self._add_string_literal(string_content_with_newline)
                else:
                    self._add_string_literal("%d\n")
            elif instr.opcode == "READ":
                self._add_string_literal("%d")
        
        self.main_function_blocks.append('define i32 @main() {')
        self._start_new_block("entry") 
        
        variables_to_allocate = set()
        for instr in tac_instructions:
            for arg in [instr.result, instr.arg1, instr.arg2]:
                if arg and arg.type == 'ID':
                    variables_to_allocate.add(arg.value)

        for var_name in sorted(list(variables_to_allocate)):
            arara_type = self.semantic_table.get(var_name, "inteiro")
            llvm_type = self._get_llvm_type(arara_type)
            ptr_reg = f'%{var_name}_ptr'
            self._add_instruction(f'{ptr_reg} = alloca {llvm_type}, align 4')
            self.var_map[var_name] = (ptr_reg, llvm_type) 
        
        for i, instr in enumerate(tac_instructions):
            op = instr.opcode
            result_operand = instr.result
            arg1_operand = instr.arg1
            arg2_operand = instr.arg2

            # <--- LÓGICA RE-ADICIONADA
            # Esta seção é crucial para que a atribuição e a soma funcionem.
            if op == "ASSIGN": 
                dest_operand = result_operand
                src_operand = arg1_operand
                assign_llvm_type = self.var_map[dest_operand.value][1] if dest_operand.value in self.var_map else "i32"
                llvm_src_val = self._get_llvm_operand_value(src_operand, assign_llvm_type)
                if dest_operand.type == 'ID': 
                    ptr_reg, _ = self.var_map[dest_operand.value]
                    self._add_instruction(f'store {assign_llvm_type} {llvm_src_val}, {assign_llvm_type}* {ptr_reg}, align 4')
                elif dest_operand.type == 'TEMP': 
                    self.temp_map[dest_operand.value] = (llvm_src_val, assign_llvm_type) 

            elif op in ["ADD", "SUB", "MUL", "DIV"]: 
                op_result_llvm_type = "i32"
                llvm_arg1_val = self._get_llvm_operand_value(arg1_operand, op_result_llvm_type)
                llvm_arg2_val = self._get_llvm_operand_value(arg2_operand, op_result_llvm_type)
                llvm_op_str = {"ADD": "add", "SUB": "sub", "MUL": "mul", "DIV": "sdiv"}[op]
                target_reg = f'%{result_operand.value}'
                self._add_instruction(f'{target_reg} = {llvm_op_str} {op_result_llvm_type} {llvm_arg1_val}, {llvm_arg2_val}')
                self.temp_map[result_operand.value] = (target_reg, op_result_llvm_type)
            # --- FIM DA LÓGICA RE-ADICIONADA

            elif instr.opcode == "READ":
                var_name = instr.result.value
                ptr_reg, llvm_type = self.var_map.get(var_name, (None, None))
                if ptr_reg:
                    format_str_name, format_array_type = self.string_literals["%d"] 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'{fmt_ptr_reg} = getelementptr inbounds {format_array_type}, {format_array_type}* {format_str_name}, i64 0, i64 0') 
                    
                    call_reg = self.next_llvm_reg()
                    # <--- CORREÇÃO AQUI
                    self._add_instruction(f'{call_reg} = call i32 (i8*, ...) @scanf(i8* {fmt_ptr_reg}, {llvm_type}* {ptr_reg})')

            elif instr.opcode == "WRITE":
                val_operand = instr.result
                if val_operand.type == 'LITERAL' and isinstance(val_operand.value, str):
                    actual_string_with_newline = val_operand.value.strip('"') + "\n"
                    format_str_name, format_array_type = self.string_literals[actual_string_with_newline] 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'{fmt_ptr_reg} = getelementptr inbounds {format_array_type}, {format_array_type}* {format_str_name}, i64 0, i64 0') 
                    
                    call_reg = self.next_llvm_reg()
                    # <--- CORREÇÃO AQUI
                    self._add_instruction(f'{call_reg} = call i32 (i8*, ...) @printf(i8* {fmt_ptr_reg})')
                else: 
                    operand_llvm_type = "i32"
                    if val_operand.type == 'ID' and val_operand.value in self.var_map:
                         _, operand_llvm_type = self.var_map[val_operand.value]
                    elif val_operand.type == 'TEMP' and val_operand.value in self.temp_map:
                         _, operand_llvm_type = self.temp_map[val_operand.value]

                    llvm_value = self._get_llvm_operand_value(val_operand, operand_llvm_type)
                    format_str_name, format_array_type = self.string_literals["%d\n"] 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'{fmt_ptr_reg} = getelementptr inbounds {format_array_type}, {format_array_type}* {format_str_name}, i64 0, i64 0') 
                    
                    call_reg = self.next_llvm_reg()
                    # <--- CORREÇÃO AQUI
                    self._add_instruction(f'{call_reg} = call i32 (i8*, ...) @printf(i8* {fmt_ptr_reg}, {operand_llvm_type} {llvm_value})')

        if not self.current_block_instructions or not self.current_block_instructions[-1].strip().startswith(('ret', 'br')):
            self._add_instruction('ret i32 0')

        if self.current_block_name not in [b.split(':')[0] for b in self.main_function_blocks if ':' in b]:
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