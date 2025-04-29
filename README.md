# 🦜 ARARA — Compilador Acadêmico

ARARA é uma linguagem de programação fictícia com comandos em **português**, inspirada na linguagem Tiny. Criada com fins didáticos, ela possui **sintaxe clara**, **tipagem simples** e **estrutura de controle completa**, sendo ideal para o estudo de compiladores.

---

## 🎯 Objetivos do Projeto

✅ Implementar um compilador completo com:

- Análise **léxica**
- Análise **sintática**
- Geração de **Árvore Sintática Abstrata (AST)**
- Tratamento de **erros personalizados**
- Uso de **ANTLR4** com gramática LL(1)

---

## 🧠 Funcionalidades da Linguagem

🔤 **Tipos primitivos**  
`int`, `string`

📥 **Entrada**  
`leia()`

📤 **Saída**  
`escreva()`

🔁 **Controle de fluxo**
```plaintext
se ... entao ... senao ... fimse  
enquanto ... faca ... fimenquanto
🧮 Expressões

Aritméticas: +, -, *, /

Lógicas: &&, ||, !

Comparações: ==, !=, <, >, <=, >=

🗂 Estrutura do Projeto
pgsql
Copiar
Editar
arara/
├── grammar/         → Arquivo Arara.g4 (gramática ANTLR)
├── generated/       → Arquivos gerados pelo ANTLR
├── exemplos/        → Códigos de exemplo (.arara)
├── src/             → Código-fonte do compilador
│   ├── main.py
│   ├── error_handler.py
│   └── ast_generator.py
├── docs/            → AST visual (.dot e .png)
├── analisador.log   → Log de execução (opcional)
├── antlr-4.13.1-complete.jar
└── README.md        → Este arquivo ✨
⚙️ Como Executar
Gerar arquivos ANTLR:

bash
Copiar
Editar
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -o generated grammar/Arara.g4
Executar o compilador:

bash
Copiar
Editar
python3 src/main.py exemplos/triangulo.arara
Gerar imagem da AST:

bash
Copiar
Editar
dot -Tpng docs/ast.dot -o docs/ast.png
📸 Exemplo de Código ARARA
arara
Copiar
Editar
leia(x)
se x > 0 entao
    escreva("Positivo")
senao
    escreva("Negativo ou zero")
fimse
👨‍🏫 Autor
Desenvolvido por Pedro Lucas dos Santos
📚 Projeto da disciplina de Compiladores (2025)
🔗 GitHub do projeto

