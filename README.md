Markdown

# 🦜 ARARA — Um Compilador Didático

ARARA é uma linguagem de programação procedural e fictícia com comandos em **português**, inspirada na linguagem Tiny. Criada com fins didáticos para a disciplina de Compiladores, ela possui **sintaxe clara**, **tipagem estática simples** e **estruturas de controle completas**, sendo ideal para o estudo prático de todas as fases de um compilador moderno.

Este projeto implementa um compilador completo que traduz código-fonte `.arara` para **LLVM IR**, que por sua vez é compilado para um **executável nativo**.

---

## 🎯 Objetivos do Projeto

✅ Implementar um compilador completo com:

-   Análise **Léxica** com ANTLR4
-   Análise **Sintática** com geração de uma **Árvore Sintática Abstrata (AST)**
-   Análise **Semântica** (verificação de tipos, declarações, etc.)
-   Geração de **Código de Três Endereços (TAC)**
-   Geração de **Código Final** em **LLVM Intermediate Representation (IR)**
-   Tratamento de **erros personalizados** em múltiplas fases

---

## 🧠 Funcionalidades da Linguagem

🔤 **Tipos primitivos:**
`inteiro`, `real`

📥 **Entrada:**
`leia(variavel)`

📤 **Saída:**
`escreva(expressao)`

📝 **Atribuição:**
`variavel <- expressao`

🔁 **Controle de fluxo:**

```bash
se (condicao) entao
    // bloco de código
senao
    // bloco opcional
fimse

enquanto (condicao) faca
    // bloco de código
fimenquanto
```
🧮 **Expressões:**
``
-Aritméticas: +, -, *, /
``
``
-Relacionais: ==, !=, <, >, <=, >=
``
``
-Lógicas: &&, ||, !
``
-  Suporte a parênteses e precedência de operadores.

## 📐 Exemplo de Sintaxe

```bash
// Declara uma variável do tipo inteiro
inteiro n;

escreva("Digite um número: ");
leia(n);

se (n > 0) entao
    escreva("O número é positivo.");
senao
    escreva("O número é negativo ou zero.");
fimse
```
## 🗂 Estrutura do Projeto
```bash
arara-compiler/
├── grammar/          → Arquivo Arara.g4 (gramática ANTLR)
├── generated/        → Arquivos gerados pelo ANTLR
├── exemplos/         → Códigos de exemplo (.arara) e executáveis (.exe)
├── src/              → Código-fonte do compilador em Python
│   ├── main.py
│   ├── ast_generator.py
│   ├── tac_generator.py
│   ├── llvm_generator.py
│   └── ... (outros módulos)
├── docs/             → AST visual (.dot e .png)
├── antlr-4.13.1-complete.jar
└── README.md         → Este arquivo ✨
```
⚙️ **Pré-requisitos**
Antes de executar, certifique-se de que você tem o seguinte software instalado e configurado no seu PATH:

-  Python 3.x
-  Java Development Kit (JDK) (para executar o ANTLR)
-  ANTLR v4.13.1 (antlr-4.13.1-complete.jar)
-  LLVM e Clang: Essencial para compilar o código LLVM gerado. Baixe aqui.
-  (Opcional) Graphviz: Para visualizar a Árvore Sintática Abstrata (dot command).

⚠️ Nota para usuários do Windows: É altamente recomendável executar os comandos de compilação final (clang) no x64 Native Tools Command Prompt for VS, que já vem com o ambiente do compilador e do linker da Microsoft configurado corretamente.

🚀 Fluxo de Compilação Completo
Siga os passos abaixo para compilar e executar um programa escrito em Arara.

# Execute na raiz do projeto
```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -o generated grammar/Arara.g4
```
**Passo 1: Arara → LLVM IR (.ll)**
Use o script principal do compilador para traduzir seu código .arara para LLVM IR. Este comando executa todas as fases do seu compilador.
# Execute no terminal de sua preferência (ex: VS Code, PowerShell)
```bash
python src/main.py exemplos/SEU_EXEMPLO.arara --gerar-tac --gerar-llvm
```
Isso irá criar o arquivo:
```bash
exemplos/SEU_EXEMPLO.ll.
```
**Passo 2: LLVM IR → Executável (.exe)**
Agora, compile o arquivo .ll gerado para um executável nativo usando o clang.

Lembrete: Para evitar erros de linker no Windows, use o x64 Native Tools Command Prompt for VS.
# Execute no x64 Native Tools Command Prompt
```bash
clang exemplos\SEU_EXEMPLO.ll -o exemplos\SEU_EXEMPLO.exe -Wl,/DEFAULTLIB:legacy_stdio_definitions.lib
````
Passo 3: Executar!
Finalmente, execute seu programa recém-criado.
# Execute o programa
```bash
.\exemplos\SEU_EXEMPLO.exe
```
**👨‍🏫 Autores: Luiz.G e Pedro.L**

**📚 Projeto da disciplina de Compiladores (2025)**



