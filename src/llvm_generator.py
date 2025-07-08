# Arquivo: src/llvm_generator.py

import json
from src.tac.TACGenerator import TACOperand, TACInstruction 

class LLVMGenerator:
    def __init__(self, semantic_table={}): 
        self.module_header_lines = ['; ModuleID = "arara_program"', 'source_filename = "arara.arara"', 'target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"', 'target triple = "x86_64-pc-linux-gnu"']
        self.global_strings_defs = []
        self.function_declarations = ['declare i32 @printf(i8*, ...)', 'declare i32 @scanf(i8*, ...)']
        self.function_body = []
        self.string_literals = {}
        self.temp_map = {}
        self.var_map = {}
        self.semantic_table = semantic_table
        self.temp_count = 0
        self.string_count = 0
        self.label_count = 0

    def next_llvm_reg(self):
        reg_name = f'%t{self.temp_count}'
        self.temp_count += 1
        return reg_name

    def next_llvm_label_name(self):
        label_name = f'b{self.label_count}'
        self.label_count += 1
        return label_name

    def _add_string_literal(self, s_content):
        if s_content not in self.string_literals:
            name = f"@.str.{self.string_count}"
            self.string_count += 1
            encoded_bytes = s_content.encode('utf-8') + b'\0'
            array_len = len(encoded_bytes)
            array_type = f"[{array_len} x i8]"
            hex_bytes = "".join(f"\\{b:02X}" for b in encoded_bytes)
            llvm_string = f'{name} = private unnamed_addr constant {array_type} c"{hex_bytes}", align 1'
            self.global_strings_defs.append(llvm_string)
            self.string_literals[s_content] = (name, array_type)
        return self.string_literals[s_content]

    def _get_llvm_operand_value(self, tac_operand: 'TACOperand', target_llvm_type=None):
        val_type, val = tac_operand.type, tac_operand.value
        
        if val_type == 'LITERAL':
            if isinstance(val, str) and val.startswith('"'):
                # Pega o conteúdo da string, ex: "\\n"
                stripped_val = val.strip('"')
                
                # <--- CORREÇÃO PRINCIPAL AQUI ---
                # Processa os caracteres de escape (ex: converte '\\n' para o caractere de quebra de linha)
                unescaped_str = stripped_val.encode('latin1').decode('unicode_escape')
                
                # O resto da lógica usa a string já processada
                name, array_type = self._add_string_literal(unescaped_str)
                ptr_reg = self.next_llvm_reg()
                self.function_body.append(f'    {ptr_reg} = getelementptr inbounds {array_type}, {array_type}* {name}, i64 0, i64 0')
                return ptr_reg
            else:
                if target_llvm_type == "i1":
                    return "true" if int(val) != 0 else "false"
                return str(val)
        
        elif val_type == 'ID':
            ptr_reg, llvm_type = self.var_map[val]
            load_reg = self.next_llvm_reg()
            self.function_body.append(f'    {load_reg} = load {llvm_type}, {llvm_type}* {ptr_reg}, align 4')
            return load_reg
            
        elif val_type == 'TEMP':
            return f'%{val}'
            
        return "ERROR_OPERAND"

    def generate(self, tac_instructions: list['TACInstruction']):
        self.__init__(self.semantic_table)

        self._add_string_literal("%d")
        self._add_string_literal("%d ")

        entry_block = ['entry:']
        variables_to_allocate = sorted(list({arg.value for instr in tac_instructions for arg in [instr.result, instr.arg1, instr.arg2] if arg and arg.type == 'ID'}))
        
        for var_name in variables_to_allocate:
            arara_type = self.semantic_table.get(var_name, "inteiro")
            llvm_type = "i32" if arara_type == "inteiro" else "i1"
            ptr_reg = f'%{var_name}_ptr'
            entry_block.append(f'    {ptr_reg} = alloca {llvm_type}, align 4')
            self.var_map[var_name] = (ptr_reg, llvm_type)

        first_code_label = "start_code" 
        if not tac_instructions or tac_instructions[0].opcode != "LABEL":
             tac_instructions.insert(0, TACInstruction("LABEL", TACOperand("LABEL", first_code_label)))
        else:
             first_code_label = tac_instructions[0].result.value
             
        entry_block.append(f'    br label %{first_code_label}')
        
        for i, instr in enumerate(tac_instructions):
            op, result, arg1, arg2 = instr.opcode, instr.result, instr.arg1, instr.arg2

            if op == "LABEL":
                if self.function_body and not self.function_body[-1].strip().startswith(('br ', 'ret ')):
                    self.function_body.append(f'    br label %{result.value}')
                self.function_body.append(f'{result.value}:')
            
            elif op in ["ADD", "SUB", "MUL", "DIV", "EQ", "NEQ", "LT", "LE", "GT", "GE", "AND", "OR"]:
                target_reg = f'%{result.value}'
                llvm_type = "i1" if op in ["AND", "OR"] else "i32"
                val1 = self._get_llvm_operand_value(arg1, llvm_type)
                val2 = self._get_llvm_operand_value(arg2, llvm_type)
                op_map = {"ADD":"add", "SUB":"sub", "MUL":"mul", "DIV":"sdiv", "EQ":"icmp eq", "NEQ":"icmp ne", "LT":"icmp slt", "LE":"icmp sle", "GT":"icmp sgt", "GE":"icmp sge", "AND":"and", "OR":"or"}
                op_str = op_map[op]
                self.function_body.append(f'    {target_reg} = {op_str} {llvm_type} {val1}, {val2}')
                self.temp_map[result.value] = (target_reg, "i1" if "icmp" in op_str or op in ["AND", "OR"] else "i32")

            elif op == "ASSIGN":
                dest_ptr, dest_type = self.var_map[result.value]
                src_val = self._get_llvm_operand_value(arg1, dest_type)
                self.function_body.append(f'    store {dest_type} {src_val}, {dest_type}* {dest_ptr}, align 4')

            elif op == "GOTO":
                self.function_body.append(f'    br label %{result.value}')

            elif op == "IF_FALSE_GOTO":
                cond_val = self._get_llvm_operand_value(arg1, "i1")
                false_label = result.value
                true_label_block_name = self.next_llvm_label_name()
                self.function_body.append(f'    br i1 {cond_val}, label %{true_label_block_name}, label %{false_label}')
                self.function_body.append(f'{true_label_block_name}:')

            elif op == "READ":
                dest_ptr, dest_type = self.var_map[result.value]
                fmt_name, fmt_type = self.string_literals["%d"]
                fmt_ptr_reg = self.next_llvm_reg()
                self.function_body.append(f'    {fmt_ptr_reg} = getelementptr inbounds {fmt_type}, {fmt_type}* {fmt_name}, i64 0, i64 0')
                call_reg = self.next_llvm_reg()
                self.function_body.append(f'    {call_reg} = call i32 (i8*, ...) @scanf(i8* {fmt_ptr_reg}, {dest_type}* {dest_ptr})')

            elif op == "WRITE":
                if result.is_literal() and isinstance(result.value, str) and result.value.startswith('"'):
                    llvm_val_ptr = self._get_llvm_operand_value(result)
                    call_reg = self.next_llvm_reg()
                    self.function_body.append(f'    {call_reg} = call i32 (i8*, ...) @printf(i8* {llvm_val_ptr})')
                else: 
                    llvm_val = self._get_llvm_operand_value(result, "i32")
                    fmt_name, fmt_type = self.string_literals["%d "]
                    fmt_ptr_reg = self.next_llvm_reg()
                    self.function_body.append(f'    {fmt_ptr_reg} = getelementptr inbounds {fmt_type}, {fmt_type}* {fmt_name}, i64 0, i64 0')
                    call_reg = self.next_llvm_reg()
                    self.function_body.append(f'    {call_reg} = call i32 (i8*, ...) @printf(i8* {fmt_ptr_reg}, i32 {llvm_val})')

        if not self.function_body or not self.function_body[-1].strip().startswith(('br ', 'ret ')):
             self.function_body.append('    ret i32 0')

        final_code = ["define i32 @main() {"]
        final_code.extend(entry_block)
        final_code.extend(self.function_body)
        final_code.append("}")
        
        final_llvm_output = ["\n".join(self.module_header_lines), "\n".join(self.global_strings_defs), "\n".join(self.function_declarations), "\n".join(final_code)]
        return "\n\n".join(filter(None, final_llvm_output))