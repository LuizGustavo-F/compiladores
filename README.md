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

```arara
se (condicao) entao
    // bloco de código
senao
    // bloco opcional
fimse

enquanto (condicao) faca
    // bloco de código
fimenquanto
