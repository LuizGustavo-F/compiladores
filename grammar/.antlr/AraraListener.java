// Generated from c:/Users/lgzic/compiladores/grammar/Arara.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link AraraParser}.
 */
public interface AraraListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link AraraParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(AraraParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(AraraParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comandoLeia}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComandoLeia(AraraParser.ComandoLeiaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comandoLeia}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComandoLeia(AraraParser.ComandoLeiaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comandoEscreva}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComandoEscreva(AraraParser.ComandoEscrevaContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comandoEscreva}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComandoEscreva(AraraParser.ComandoEscrevaContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comandoAtrib}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComandoAtrib(AraraParser.ComandoAtribContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comandoAtrib}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComandoAtrib(AraraParser.ComandoAtribContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comandoCondicional}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComandoCondicional(AraraParser.ComandoCondicionalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comandoCondicional}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComandoCondicional(AraraParser.ComandoCondicionalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comandoRepeticao}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComandoRepeticao(AraraParser.ComandoRepeticaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comandoRepeticao}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComandoRepeticao(AraraParser.ComandoRepeticaoContext ctx);
	/**
	 * Enter a parse tree produced by the {@code comandoDeclaracao}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComandoDeclaracao(AraraParser.ComandoDeclaracaoContext ctx);
	/**
	 * Exit a parse tree produced by the {@code comandoDeclaracao}
	 * labeled alternative in {@link AraraParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComandoDeclaracao(AraraParser.ComandoDeclaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#condicional}.
	 * @param ctx the parse tree
	 */
	void enterCondicional(AraraParser.CondicionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#condicional}.
	 * @param ctx the parse tree
	 */
	void exitCondicional(AraraParser.CondicionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#cond_opc}.
	 * @param ctx the parse tree
	 */
	void enterCond_opc(AraraParser.Cond_opcContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#cond_opc}.
	 * @param ctx the parse tree
	 */
	void exitCond_opc(AraraParser.Cond_opcContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#repeticao}.
	 * @param ctx the parse tree
	 */
	void enterRepeticao(AraraParser.RepeticaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#repeticao}.
	 * @param ctx the parse tree
	 */
	void exitRepeticao(AraraParser.RepeticaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao(AraraParser.DeclaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao(AraraParser.DeclaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#bloco}.
	 * @param ctx the parse tree
	 */
	void enterBloco(AraraParser.BlocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#bloco}.
	 * @param ctx the parse tree
	 */
	void exitBloco(AraraParser.BlocoContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExpressao(AraraParser.ExpressaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExpressao(AraraParser.ExpressaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#logica}.
	 * @param ctx the parse tree
	 */
	void enterLogica(AraraParser.LogicaContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#logica}.
	 * @param ctx the parse tree
	 */
	void exitLogica(AraraParser.LogicaContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#logica_suf}.
	 * @param ctx the parse tree
	 */
	void enterLogica_suf(AraraParser.Logica_sufContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#logica_suf}.
	 * @param ctx the parse tree
	 */
	void exitLogica_suf(AraraParser.Logica_sufContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#comparacao}.
	 * @param ctx the parse tree
	 */
	void enterComparacao(AraraParser.ComparacaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#comparacao}.
	 * @param ctx the parse tree
	 */
	void exitComparacao(AraraParser.ComparacaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#comparacao_suf}.
	 * @param ctx the parse tree
	 */
	void enterComparacao_suf(AraraParser.Comparacao_sufContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#comparacao_suf}.
	 * @param ctx the parse tree
	 */
	void exitComparacao_suf(AraraParser.Comparacao_sufContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#soma}.
	 * @param ctx the parse tree
	 */
	void enterSoma(AraraParser.SomaContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#soma}.
	 * @param ctx the parse tree
	 */
	void exitSoma(AraraParser.SomaContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#soma_suf}.
	 * @param ctx the parse tree
	 */
	void enterSoma_suf(AraraParser.Soma_sufContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#soma_suf}.
	 * @param ctx the parse tree
	 */
	void exitSoma_suf(AraraParser.Soma_sufContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#termo}.
	 * @param ctx the parse tree
	 */
	void enterTermo(AraraParser.TermoContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#termo}.
	 * @param ctx the parse tree
	 */
	void exitTermo(AraraParser.TermoContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#termo_suf}.
	 * @param ctx the parse tree
	 */
	void enterTermo_suf(AraraParser.Termo_sufContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#termo_suf}.
	 * @param ctx the parse tree
	 */
	void exitTermo_suf(AraraParser.Termo_sufContext ctx);
	/**
	 * Enter a parse tree produced by {@link AraraParser#fator}.
	 * @param ctx the parse tree
	 */
	void enterFator(AraraParser.FatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link AraraParser#fator}.
	 * @param ctx the parse tree
	 */
	void exitFator(AraraParser.FatorContext ctx);
}