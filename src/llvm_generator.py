# Arquivo: src/llvm_generator.py

import json # Manter o import para segurança

class LLVMGenerator:
    def __init__(self):
        self.module_header_lines = []
        self.global_strings_defs = [] 
        self.function_declarations = [] 
        self.main_function_blocks = [] 
        
        self.var_map = {}  
        self.temp_map = {} 
        self.label_map = {} 
        
        self.llvm_temp_counter = 0 
        self.string_count = 0
        
        self.current_block_instructions = [] 
        self.current_block_name = "entry" 
        
        self.string_literals = {} 


    def _add_instruction(self, instruction_line):
        """Adiciona uma instrução ao bloco básico atual."""
        self.current_block_instructions.append(f'  {instruction_line}')

    def _start_new_block(self, block_name):
        """Finaliza o bloco atual e inicia um novo."""
        if self.current_block_instructions: 
            self.main_function_blocks.append(f'{self.current_block_name}:')
            self.main_function_blocks.extend(self.current_block_instructions)
            
        self.current_block_name = block_name
        self.current_block_instructions = [] 

    def _get_llvm_type(self, arara_type):
        if arara_type == "inteiro":
            return "i32"
        elif arara_type == "real":
            return "float" 
        elif arara_type == "booleano":
            return "i1"
        return "i8*" 

    def _declare_printf_scanf(self):
        # Nenhuma linha em branco aqui, elas serão adicionadas na montagem final
        self.function_declarations.append('declare i32 @printf(i8* noundef, ...) # !0')
        self.function_declarations.append('declare i32 @__isoc99_scanf(i8* noundef, ...) # !1')

    def _add_string_literal(self, s_content):
        """
        Adiciona uma string literal global ao LLVM IR, garantindo que o tamanho seja correto.
        Lida com o escapamento de caracteres e a adição do null terminator.
        """
        if s_content not in self.string_literals:
            raw_bytes = s_content.encode('utf-8') + b'\x00'
            
            llvm_escaped_bytes = "".join(f"\\{b:02X}" for b in raw_bytes)
            
            byte_array_len = len(raw_bytes) 
            
            # --- MANTER LINHAS DE DEPURAR PARA VERIFICAR A CORREÇÃO ---
            print(f"DEBUG (NEW): Processing string content: '{s_content}'")
            print(f"DEBUG (NEW): Raw bytes: {raw_bytes}")
            print(f"DEBUG (NEW): LLVM escaped bytes: '{llvm_escaped_bytes}'")
            print(f"DEBUG (NEW): Calculated byte_array_len: {byte_array_len}")
            # --- FIM DAS LINHAS DE DEPURAR ---

            name = f"@.str.{self.string_count}"
            llvm_string = f'{name} = private unnamed_addr constant [{byte_array_len} x i8] c"{llvm_escaped_bytes}", align 1'
            
            self.global_strings_defs.append(llvm_string)
            self.string_literals[s_content] = (name, byte_array_len)
            self.string_count += 1
        return self.string_literals[s_content]

    def next_llvm_reg(self):
        self.llvm_temp_counter += 1
        return f'temp{self.llvm_temp_counter - 1}'
    
    def next_llvm_label_name(self):
        """Gera um nome de rótulo LLVM único para blocos implícitos."""
        label_name = f'block_{self.next_llvm_reg()}' 
        return label_name

    def _get_llvm_operand_value(self, tac_operand_str, target_llvm_type=None):
        """
        Retorna o registrador LLVM IR que contém o valor do operando TAC,
        realizando loads e conversões de tipo conforme necessário.
        """
        if tac_operand_str.isdigit() or (tac_operand_str.startswith('-') and tac_operand_str[1:].isdigit()):
            return tac_operand_str 

        elif tac_operand_str.startswith('"'):
            name, length = self._add_string_literal(tac_operand_str.strip('"'))
            string_ptr_reg = self.next_llvm_reg()
            self._add_instruction(f'%{string_ptr_reg} = getelementptr inbounds ([{length} x i8], [{length} x i8]* {name}, i64 0, i64 0)')
            return f'%{string_ptr_reg}'

        elif tac_operand_str in self.var_map:
            ptr_reg, actual_llvm_type = self.var_map[tac_operand_str]
            val_reg = self.next_llvm_reg()
            self._add_instruction(f'%{val_reg} = load {actual_llvm_type}, {actual_llvm_type}* {ptr_reg}, align 4')
            
            if actual_llvm_type != target_llvm_type and target_llvm_type is not None:
                if actual_llvm_type == "i32" and target_llvm_type == "i1":
                    bool_reg = self.next_llvm_reg()
                    self._add_instruction(f'%{bool_reg} = icmp ne i32 %{val_reg}, 0') 
                    return f'%{bool_reg}'
            return f'%{val_reg}'

        elif tac_operand_str in self.temp_map:
            val_reg, actual_llvm_type = self.temp_map[tac_operand_str]

            if actual_llvm_type != target_llvm_type and target_llvm_type is not None:
                if actual_llvm_type == "i32" and target_llvm_type == "i1":
                    bool_reg = self.next_llvm_reg()
                    self._add_instruction(f'%{bool_reg} = icmp ne i32 {val_reg}, 0')
                    return f'%{bool_reg}'
            return val_reg
        else:
            if tac_operand_str.startswith('_t'):
                return f'%{tac_operand_str}'
            return tac_operand_str 

    def generate_llvm_ir(self, tac_instructions, semantic_table={}):
        self.__init__() 

        # Cabeçalho do Módulo LLVM
        self.module_header_lines = [
            '; ModuleID = "arara_program"',
            'source_filename = "arara.arara"',
            'target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"',
            'target triple = "x86_64-pc-linux-gnu"'
            # REMOVA A LINHA EM BRANCO AQUI
        ]
        
        # As declarações de printf/scanf não adicionam mais linha em branco no final
        self._declare_printf_scanf() 

        for instr_str in tac_instructions:
            if instr_str.endswith(':'): 
                label_name = instr_str.strip(':')
                self.label_map[label_name] = label_name 


        self.main_function_blocks.append('define i32 @main() {')
        self._start_new_block("entry") 
        
        variables_to_allocate = set()
        for instr_str in tac_instructions:
            if "READ " in instr_str:
                var_name = instr_str.split(' ')[1].strip()
                variables_to_allocate.add(var_name)
            elif " = " in instr_str:
                parts = instr_str.split(" = ")
                result_var = parts[0].strip()
                if not result_var.startswith('_t'): 
                     variables_to_allocate.add(result_var)

        for var_name in sorted(list(variables_to_allocate)):
            arara_type = semantic_table.get(var_name, "inteiro") 
            llvm_type = self._get_llvm_type(arara_type)
            ptr_reg = f'%{var_name}_ptr'
            self._add_instruction(f'{ptr_reg} = alloca {llvm_type}, align 4')
            self.var_map[var_name] = (ptr_reg, llvm_type) 


        for i, instr_str in enumerate(tac_instructions):
            if instr_str.endswith(':'): 
                label_name = instr_str.strip(':')
                self._start_new_block(self.label_map[label_name]) 

            elif " = " in instr_str: 
                parts = instr_str.split(" = ")
                result_tac_name = parts[0].strip()
                expr_parts = parts[1].split(' ')
                
                op_result_llvm_type = "i32" 

                if len(expr_parts) == 1: 
                    arg1_tac = expr_parts[0]
                    if result_tac_name in self.var_map:
                        op_result_llvm_type = self.var_map[result_tac_name][1] 
                    elif arg1_tac in self.temp_map:
                        op_result_llvm_type = self.temp_map[arg1_tac][1] 

                    llvm_arg1_val = self._get_llvm_operand_value(arg1_tac, op_result_llvm_type)
                    
                    if result_tac_name.startswith('_t'): 
                        target_reg = f'%{result_tac_name}'
                        if arg1_tac.isdigit() or (arg1_tac.startswith('-') and arg1_tac[1:].isdigit()):
                             self._add_instruction(f'{target_reg} = add {op_result_llvm_type} {llvm_arg1_val}, 0 ; Literal to temp')
                        else: 
                             self.temp_map[result_tac_name] = (llvm_arg1_val, op_result_llvm_type)
                             continue 
                        self.temp_map[result_tac_name] = (target_reg, op_result_llvm_type)
                    elif result_tac_name in self.var_map: 
                        ptr_reg, _ = self.var_map[result_tac_name]
                        self._add_instruction(f'store {op_result_llvm_type} {llvm_arg1_val}, {op_result_llvm_type}* {ptr_reg}, align 4')

                elif len(expr_parts) == 3: 
                    arg1_tac, op, arg2_tac = expr_parts
                    
                    llvm_op_str = ""
                    if op in ['+', '-', '*', '/']:
                        op_result_llvm_type = "i32" 
                    elif op in ['==', '!=', '<', '<=', '>', '>=']:
                        op_result_llvm_type = "i1" 
                        llvm_op_str = "icmp " 
                    elif op in ['&&', '||']:
                        op_result_llvm_type = "i1" 

                    llvm_arg1_val = self._get_llvm_operand_value(arg1_tac, op_result_llvm_type)
                    llvm_arg2_val = self._get_llvm_operand_value(arg2_tac, op_result_llvm_type)

                    if op == '+': llvm_op_str += "add"
                    elif op == '-': llvm_op_str += "sub"
                    elif op == '*': llvm_op_str += "mul"
                    elif op == '/': llvm_op_str += "sdiv" 
                    elif op == '&&': llvm_op_str += "and"
                    elif op == '||': llvm_op_str += "or"
                    elif op == '==': llvm_op_str += "eq"
                    elif op == '!=': llvm_op_str += "ne"
                    elif op == '<': llvm_op_str += "slt" 
                    elif op == '<=': llvm_op_str += "sle"
                    elif op == '>': llvm_op_str += "sgt" 
                    elif op == '>=': llvm_op_str += "sge"
                    
                    if llvm_op_str:
                        target_reg = f'%{result_tac_name}'
                        self._add_instruction(f'{target_reg} = {llvm_op_str} {op_result_llvm_type} {llvm_arg1_val}, {llvm_arg2_val}')
                        self.temp_map[result_tac_name] = (target_reg, op_result_llvm_type)

                elif len(expr_parts) == 2 and expr_parts[0] == '!': 
                    arg_tac = expr_parts[1]
                    op_result_llvm_type = self._get_llvm_type("booleano") 
                    llvm_arg_val = self._get_llvm_operand_value(arg_tac, op_result_llvm_type)
                    
                    target_reg = f'%{result_tac_name}'
                    self._add_instruction(f'{target_reg} = xor {op_result_llvm_type} {llvm_arg_val}, true')
                    self.temp_map[result_tac_name] = (target_reg, op_result_llvm_type)

            elif instr_str.startswith("READ"):
                var_name = instr_str.split(' ')[1]
                ptr_reg, llvm_type = self.var_map.get(var_name, (None, None))
                if ptr_reg:
                    format_str_name, format_str_len = self._add_string_literal("%d")
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'%{fmt_ptr_reg} = getelementptr inbounds ([{format_str_len} x i8], [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0)')
                    self._add_instruction(f'%call_scanf_{self.next_llvm_reg()} = call i32 (i8*, ...) @__isoc99_scanf(i8* %{fmt_ptr_reg}, {llvm_type}* {ptr_reg})')

            elif instr_str.startswith("WRITE"):
                operand_str = instr_str.split(' ', 1)[1]
                
                if operand_str.startswith('"'): 
                    actual_string = operand_str.strip('"')
                    format_str_name, format_str_len = self._add_string_literal(actual_string + "\n") 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'%{fmt_ptr_reg} = getelementptr inbounds ([{format_str_len} x i8], [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0)')
                    self._add_instruction(f'%call_printf_{self.next_llvm_reg()} = call i32 (i8*, ...) @printf(i8* %{fmt_ptr_reg})')
                else: 
                    operand_llvm_type = "i32" 
                    if operand_str in self.var_map:
                        operand_llvm_type = self.var_map[operand_str][1]
                    elif operand_str in self.temp_map:
                        operand_llvm_type = self.temp_map[operand_str][1]

                    llvm_value = self._get_llvm_operand_value(operand_str, operand_llvm_type)
                    
                    format_str_name, format_str_len = self._add_string_literal("%d\n") 
                    fmt_ptr_reg = self.next_llvm_reg()
                    self._add_instruction(f'%{fmt_ptr_reg} = getelementptr inbounds ([{format_str_len} x i8], [{format_str_len} x i8]* {format_str_name}, i64 0, i64 0)')
                    self._add_instruction(f'%call_printf_{self.next_llvm_reg()} = call i32 (i8*, ...) @printf(i8* %{fmt_ptr_reg}, {operand_llvm_type} {llvm_value})')

            elif instr_str.startswith("IF_FALSE_GOTO"):
                parts = instr_str.split(' ')
                condition_tac_var = parts[1]
                goto_tac_label = parts[3].strip(':')
                
                llvm_cond_val = self._get_llvm_operand_value(condition_tac_var, self._get_llvm_type("booleano"))
                
                true_block_name = self.next_llvm_label_name() 
                false_block_name = self.label_map.get(goto_tac_label) 

                self._add_instruction(f'br i1 {llvm_cond_val}, label %{true_block_name}, label %{false_block_name}')
                self._start_new_block(true_block_name) 

            elif instr_str.startswith("GOTO"):
                label_tac = instr_str.split(' ')[1].strip(':')
                llvm_goto_label = self.label_map.get(label_tac)
                self._add_instruction(f'br label %{llvm_goto_label}')
                self._start_new_block(self.next_llvm_label_name()) 

        if self.current_block_instructions and not self.current_block_instructions[-1].strip().startswith(('ret', 'br')):
            self._add_instruction('ret i32 0')
        elif not self.current_block_instructions: 
            self._add_instruction('ret i32 0')

        if self.current_block_name not in self.label_map or not self.main_function_blocks: 
             self.main_function_blocks.append(f'{self.current_block_name}:')
        self.main_function_blocks.extend(self.current_block_instructions)

        self.main_function_blocks.append('}') 

        final_llvm_output = []
        final_llvm_output.extend(self.module_header_lines)
        final_llvm_output.append('') # Adiciona uma linha em branco após o cabeçalho do módulo
        final_llvm_output.extend(self.global_strings_defs) 
        final_llvm_output.append('') # Adiciona uma linha em branco após as definições de strings
        final_llvm_output.extend(self.function_declarations) 
        final_llvm_output.append('') # Adiciona uma linha em branco após as declarações de função
        final_llvm_output.extend(self.main_function_blocks) 

        return "\n".join(final_llvm_output)