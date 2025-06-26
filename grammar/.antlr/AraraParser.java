// Generated from c:/Users/8760659/Documents/GitHub/compiladores/grammar/Arara.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class AraraParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LEIA=1, ESCREVA=2, SE=3, ENTAO=4, SENAO=5, FIMSE=6, ENQUANTO=7, FACA=8, 
		FIMENQ=9, TIPO=10, LPAREN=11, RPAREN=12, SEMICOLON=13, ATRIB=14, OPSUM=15, 
		OPMULT=16, OPCOMP=17, OPLOG=18, NOT=19, STRING=20, INT=21, ID=22, WS=23;
	public static final int
		RULE_programa = 0, RULE_comando = 1, RULE_condicional = 2, RULE_cond_opc = 3, 
		RULE_repeticao = 4, RULE_declaracao = 5, RULE_bloco = 6, RULE_expressao = 7, 
		RULE_logica = 8, RULE_logica_suf = 9, RULE_comparacao = 10, RULE_comparacao_suf = 11, 
		RULE_soma = 12, RULE_soma_suf = 13, RULE_termo = 14, RULE_termo_suf = 15, 
		RULE_fator = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "comando", "condicional", "cond_opc", "repeticao", "declaracao", 
			"bloco", "expressao", "logica", "logica_suf", "comparacao", "comparacao_suf", 
			"soma", "soma_suf", "termo", "termo_suf", "fator"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'leia'", "'escreva'", "'se'", "'entao'", "'senao'", "'fimse'", 
			"'enquanto'", "'faca'", "'fimenquanto'", null, "'('", "')'", "';'", "'<-'", 
			null, null, null, null, "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LEIA", "ESCREVA", "SE", "ENTAO", "SENAO", "FIMSE", "ENQUANTO", 
			"FACA", "FIMENQ", "TIPO", "LPAREN", "RPAREN", "SEMICOLON", "ATRIB", "OPSUM", 
			"OPMULT", "OPCOMP", "OPLOG", "NOT", "STRING", "INT", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Arara.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public AraraParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(AraraParser.EOF, 0); }
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(37);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4195470L) != 0)) {
				{
				{
				setState(34);
				comando();
				}
				}
				setState(39);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(40);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComandoContext extends ParserRuleContext {
		public ComandoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando; }
	 
		public ComandoContext() { }
		public void copyFrom(ComandoContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComandoCondicionalContext extends ComandoContext {
		public CondicionalContext condicional() {
			return getRuleContext(CondicionalContext.class,0);
		}
		public ComandoCondicionalContext(ComandoContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComandoDeclaracaoContext extends ComandoContext {
		public DeclaracaoContext declaracao() {
			return getRuleContext(DeclaracaoContext.class,0);
		}
		public ComandoDeclaracaoContext(ComandoContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComandoRepeticaoContext extends ComandoContext {
		public RepeticaoContext repeticao() {
			return getRuleContext(RepeticaoContext.class,0);
		}
		public ComandoRepeticaoContext(ComandoContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComandoLeiaContext extends ComandoContext {
		public TerminalNode LEIA() { return getToken(AraraParser.LEIA, 0); }
		public TerminalNode LPAREN() { return getToken(AraraParser.LPAREN, 0); }
		public TerminalNode ID() { return getToken(AraraParser.ID, 0); }
		public TerminalNode RPAREN() { return getToken(AraraParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(AraraParser.SEMICOLON, 0); }
		public ComandoLeiaContext(ComandoContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComandoEscrevaContext extends ComandoContext {
		public TerminalNode ESCREVA() { return getToken(AraraParser.ESCREVA, 0); }
		public TerminalNode LPAREN() { return getToken(AraraParser.LPAREN, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(AraraParser.RPAREN, 0); }
		public TerminalNode SEMICOLON() { return getToken(AraraParser.SEMICOLON, 0); }
		public ComandoEscrevaContext(ComandoContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ComandoAtribContext extends ComandoContext {
		public TerminalNode ID() { return getToken(AraraParser.ID, 0); }
		public TerminalNode ATRIB() { return getToken(AraraParser.ATRIB, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(AraraParser.SEMICOLON, 0); }
		public ComandoAtribContext(ComandoContext ctx) { copyFrom(ctx); }
	}

	public final ComandoContext comando() throws RecognitionException {
		ComandoContext _localctx = new ComandoContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_comando);
		try {
			setState(61);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LEIA:
				_localctx = new ComandoLeiaContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(42);
				match(LEIA);
				setState(43);
				match(LPAREN);
				setState(44);
				match(ID);
				setState(45);
				match(RPAREN);
				setState(46);
				match(SEMICOLON);
				}
				break;
			case ESCREVA:
				_localctx = new ComandoEscrevaContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(47);
				match(ESCREVA);
				setState(48);
				match(LPAREN);
				setState(49);
				expressao();
				setState(50);
				match(RPAREN);
				setState(51);
				match(SEMICOLON);
				}
				break;
			case ID:
				_localctx = new ComandoAtribContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(53);
				match(ID);
				setState(54);
				match(ATRIB);
				setState(55);
				expressao();
				setState(56);
				match(SEMICOLON);
				}
				break;
			case SE:
				_localctx = new ComandoCondicionalContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(58);
				condicional();
				}
				break;
			case ENQUANTO:
				_localctx = new ComandoRepeticaoContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(59);
				repeticao();
				}
				break;
			case TIPO:
				_localctx = new ComandoDeclaracaoContext(_localctx);
				enterOuterAlt(_localctx, 6);
				{
				setState(60);
				declaracao();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CondicionalContext extends ParserRuleContext {
		public TerminalNode SE() { return getToken(AraraParser.SE, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode ENTAO() { return getToken(AraraParser.ENTAO, 0); }
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public Cond_opcContext cond_opc() {
			return getRuleContext(Cond_opcContext.class,0);
		}
		public TerminalNode FIMSE() { return getToken(AraraParser.FIMSE, 0); }
		public CondicionalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicional; }
	}

	public final CondicionalContext condicional() throws RecognitionException {
		CondicionalContext _localctx = new CondicionalContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_condicional);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(63);
			match(SE);
			setState(64);
			expressao();
			setState(65);
			match(ENTAO);
			setState(66);
			bloco();
			setState(67);
			cond_opc();
			setState(68);
			match(FIMSE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Cond_opcContext extends ParserRuleContext {
		public TerminalNode SENAO() { return getToken(AraraParser.SENAO, 0); }
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public Cond_opcContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond_opc; }
	}

	public final Cond_opcContext cond_opc() throws RecognitionException {
		Cond_opcContext _localctx = new Cond_opcContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_cond_opc);
		try {
			setState(73);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SENAO:
				enterOuterAlt(_localctx, 1);
				{
				setState(70);
				match(SENAO);
				setState(71);
				bloco();
				}
				break;
			case FIMSE:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RepeticaoContext extends ParserRuleContext {
		public TerminalNode ENQUANTO() { return getToken(AraraParser.ENQUANTO, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode FACA() { return getToken(AraraParser.FACA, 0); }
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public TerminalNode FIMENQ() { return getToken(AraraParser.FIMENQ, 0); }
		public RepeticaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeticao; }
	}

	public final RepeticaoContext repeticao() throws RecognitionException {
		RepeticaoContext _localctx = new RepeticaoContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_repeticao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(ENQUANTO);
			setState(76);
			expressao();
			setState(77);
			match(FACA);
			setState(78);
			bloco();
			setState(79);
			match(FIMENQ);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclaracaoContext extends ParserRuleContext {
		public TerminalNode TIPO() { return getToken(AraraParser.TIPO, 0); }
		public TerminalNode ID() { return getToken(AraraParser.ID, 0); }
		public TerminalNode SEMICOLON() { return getToken(AraraParser.SEMICOLON, 0); }
		public DeclaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaracao; }
	}

	public final DeclaracaoContext declaracao() throws RecognitionException {
		DeclaracaoContext _localctx = new DeclaracaoContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_declaracao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(TIPO);
			setState(82);
			match(ID);
			setState(83);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlocoContext extends ParserRuleContext {
		public List<ComandoContext> comando() {
			return getRuleContexts(ComandoContext.class);
		}
		public ComandoContext comando(int i) {
			return getRuleContext(ComandoContext.class,i);
		}
		public BlocoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloco; }
	}

	public final BlocoContext bloco() throws RecognitionException {
		BlocoContext _localctx = new BlocoContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_bloco);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(88);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4195470L) != 0)) {
				{
				{
				setState(85);
				comando();
				}
				}
				setState(90);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressaoContext extends ParserRuleContext {
		public LogicaContext logica() {
			return getRuleContext(LogicaContext.class,0);
		}
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_expressao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			logica();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicaContext extends ParserRuleContext {
		public ComparacaoContext comparacao() {
			return getRuleContext(ComparacaoContext.class,0);
		}
		public Logica_sufContext logica_suf() {
			return getRuleContext(Logica_sufContext.class,0);
		}
		public LogicaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logica; }
	}

	public final LogicaContext logica() throws RecognitionException {
		LogicaContext _localctx = new LogicaContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_logica);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			comparacao();
			setState(94);
			logica_suf();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Logica_sufContext extends ParserRuleContext {
		public TerminalNode OPLOG() { return getToken(AraraParser.OPLOG, 0); }
		public ComparacaoContext comparacao() {
			return getRuleContext(ComparacaoContext.class,0);
		}
		public Logica_sufContext logica_suf() {
			return getRuleContext(Logica_sufContext.class,0);
		}
		public Logica_sufContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logica_suf; }
	}

	public final Logica_sufContext logica_suf() throws RecognitionException {
		Logica_sufContext _localctx = new Logica_sufContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_logica_suf);
		try {
			setState(101);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPLOG:
				enterOuterAlt(_localctx, 1);
				{
				setState(96);
				match(OPLOG);
				setState(97);
				comparacao();
				setState(98);
				logica_suf();
				}
				break;
			case ENTAO:
			case FACA:
			case RPAREN:
			case SEMICOLON:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparacaoContext extends ParserRuleContext {
		public SomaContext soma() {
			return getRuleContext(SomaContext.class,0);
		}
		public Comparacao_sufContext comparacao_suf() {
			return getRuleContext(Comparacao_sufContext.class,0);
		}
		public ComparacaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparacao; }
	}

	public final ComparacaoContext comparacao() throws RecognitionException {
		ComparacaoContext _localctx = new ComparacaoContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_comparacao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(103);
			soma();
			setState(104);
			comparacao_suf();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Comparacao_sufContext extends ParserRuleContext {
		public TerminalNode OPCOMP() { return getToken(AraraParser.OPCOMP, 0); }
		public SomaContext soma() {
			return getRuleContext(SomaContext.class,0);
		}
		public Comparacao_sufContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparacao_suf; }
	}

	public final Comparacao_sufContext comparacao_suf() throws RecognitionException {
		Comparacao_sufContext _localctx = new Comparacao_sufContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_comparacao_suf);
		try {
			setState(109);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPCOMP:
				enterOuterAlt(_localctx, 1);
				{
				setState(106);
				match(OPCOMP);
				setState(107);
				soma();
				}
				break;
			case ENTAO:
			case FACA:
			case RPAREN:
			case SEMICOLON:
			case OPLOG:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SomaContext extends ParserRuleContext {
		public TermoContext termo() {
			return getRuleContext(TermoContext.class,0);
		}
		public Soma_sufContext soma_suf() {
			return getRuleContext(Soma_sufContext.class,0);
		}
		public SomaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_soma; }
	}

	public final SomaContext soma() throws RecognitionException {
		SomaContext _localctx = new SomaContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_soma);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(111);
			termo();
			setState(112);
			soma_suf();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Soma_sufContext extends ParserRuleContext {
		public TerminalNode OPSUM() { return getToken(AraraParser.OPSUM, 0); }
		public TermoContext termo() {
			return getRuleContext(TermoContext.class,0);
		}
		public Soma_sufContext soma_suf() {
			return getRuleContext(Soma_sufContext.class,0);
		}
		public Soma_sufContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_soma_suf; }
	}

	public final Soma_sufContext soma_suf() throws RecognitionException {
		Soma_sufContext _localctx = new Soma_sufContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_soma_suf);
		try {
			setState(119);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPSUM:
				enterOuterAlt(_localctx, 1);
				{
				setState(114);
				match(OPSUM);
				setState(115);
				termo();
				setState(116);
				soma_suf();
				}
				break;
			case ENTAO:
			case FACA:
			case RPAREN:
			case SEMICOLON:
			case OPCOMP:
			case OPLOG:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermoContext extends ParserRuleContext {
		public FatorContext fator() {
			return getRuleContext(FatorContext.class,0);
		}
		public Termo_sufContext termo_suf() {
			return getRuleContext(Termo_sufContext.class,0);
		}
		public TermoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termo; }
	}

	public final TermoContext termo() throws RecognitionException {
		TermoContext _localctx = new TermoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_termo);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			fator();
			setState(122);
			termo_suf();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class Termo_sufContext extends ParserRuleContext {
		public TerminalNode OPMULT() { return getToken(AraraParser.OPMULT, 0); }
		public FatorContext fator() {
			return getRuleContext(FatorContext.class,0);
		}
		public Termo_sufContext termo_suf() {
			return getRuleContext(Termo_sufContext.class,0);
		}
		public Termo_sufContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_termo_suf; }
	}

	public final Termo_sufContext termo_suf() throws RecognitionException {
		Termo_sufContext _localctx = new Termo_sufContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_termo_suf);
		try {
			setState(129);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPMULT:
				enterOuterAlt(_localctx, 1);
				{
				setState(124);
				match(OPMULT);
				setState(125);
				fator();
				setState(126);
				termo_suf();
				}
				break;
			case ENTAO:
			case FACA:
			case RPAREN:
			case SEMICOLON:
			case OPSUM:
			case OPCOMP:
			case OPLOG:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FatorContext extends ParserRuleContext {
		public TerminalNode NOT() { return getToken(AraraParser.NOT, 0); }
		public FatorContext fator() {
			return getRuleContext(FatorContext.class,0);
		}
		public TerminalNode LPAREN() { return getToken(AraraParser.LPAREN, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(AraraParser.RPAREN, 0); }
		public TerminalNode INT() { return getToken(AraraParser.INT, 0); }
		public TerminalNode STRING() { return getToken(AraraParser.STRING, 0); }
		public TerminalNode ID() { return getToken(AraraParser.ID, 0); }
		public FatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_fator; }
	}

	public final FatorContext fator() throws RecognitionException {
		FatorContext _localctx = new FatorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_fator);
		try {
			setState(140);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case NOT:
				enterOuterAlt(_localctx, 1);
				{
				setState(131);
				match(NOT);
				setState(132);
				fator();
				}
				break;
			case LPAREN:
				enterOuterAlt(_localctx, 2);
				{
				setState(133);
				match(LPAREN);
				setState(134);
				expressao();
				setState(135);
				match(RPAREN);
				}
				break;
			case INT:
				enterOuterAlt(_localctx, 3);
				{
				setState(137);
				match(INT);
				}
				break;
			case STRING:
				enterOuterAlt(_localctx, 4);
				{
				setState(138);
				match(STRING);
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 5);
				{
				setState(139);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0017\u008f\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0005\u0000$\b\u0000\n\u0000"+
		"\f\u0000\'\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001>\b"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003J\b"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0005"+
		"\u0006W\b\u0006\n\u0006\f\u0006Z\t\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\tf\b"+
		"\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b"+
		"n\b\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0003\rx\b\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0003\u000f\u0082\b\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u008d\b\u0010\u0001\u0010\u0000"+
		"\u0000\u0011\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0018\u001a\u001c\u001e \u0000\u0000\u008d\u0000%\u0001\u0000\u0000\u0000"+
		"\u0002=\u0001\u0000\u0000\u0000\u0004?\u0001\u0000\u0000\u0000\u0006I"+
		"\u0001\u0000\u0000\u0000\bK\u0001\u0000\u0000\u0000\nQ\u0001\u0000\u0000"+
		"\u0000\fX\u0001\u0000\u0000\u0000\u000e[\u0001\u0000\u0000\u0000\u0010"+
		"]\u0001\u0000\u0000\u0000\u0012e\u0001\u0000\u0000\u0000\u0014g\u0001"+
		"\u0000\u0000\u0000\u0016m\u0001\u0000\u0000\u0000\u0018o\u0001\u0000\u0000"+
		"\u0000\u001aw\u0001\u0000\u0000\u0000\u001cy\u0001\u0000\u0000\u0000\u001e"+
		"\u0081\u0001\u0000\u0000\u0000 \u008c\u0001\u0000\u0000\u0000\"$\u0003"+
		"\u0002\u0001\u0000#\"\u0001\u0000\u0000\u0000$\'\u0001\u0000\u0000\u0000"+
		"%#\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&(\u0001\u0000\u0000"+
		"\u0000\'%\u0001\u0000\u0000\u0000()\u0005\u0000\u0000\u0001)\u0001\u0001"+
		"\u0000\u0000\u0000*+\u0005\u0001\u0000\u0000+,\u0005\u000b\u0000\u0000"+
		",-\u0005\u0016\u0000\u0000-.\u0005\f\u0000\u0000.>\u0005\r\u0000\u0000"+
		"/0\u0005\u0002\u0000\u000001\u0005\u000b\u0000\u000012\u0003\u000e\u0007"+
		"\u000023\u0005\f\u0000\u000034\u0005\r\u0000\u00004>\u0001\u0000\u0000"+
		"\u000056\u0005\u0016\u0000\u000067\u0005\u000e\u0000\u000078\u0003\u000e"+
		"\u0007\u000089\u0005\r\u0000\u00009>\u0001\u0000\u0000\u0000:>\u0003\u0004"+
		"\u0002\u0000;>\u0003\b\u0004\u0000<>\u0003\n\u0005\u0000=*\u0001\u0000"+
		"\u0000\u0000=/\u0001\u0000\u0000\u0000=5\u0001\u0000\u0000\u0000=:\u0001"+
		"\u0000\u0000\u0000=;\u0001\u0000\u0000\u0000=<\u0001\u0000\u0000\u0000"+
		">\u0003\u0001\u0000\u0000\u0000?@\u0005\u0003\u0000\u0000@A\u0003\u000e"+
		"\u0007\u0000AB\u0005\u0004\u0000\u0000BC\u0003\f\u0006\u0000CD\u0003\u0006"+
		"\u0003\u0000DE\u0005\u0006\u0000\u0000E\u0005\u0001\u0000\u0000\u0000"+
		"FG\u0005\u0005\u0000\u0000GJ\u0003\f\u0006\u0000HJ\u0001\u0000\u0000\u0000"+
		"IF\u0001\u0000\u0000\u0000IH\u0001\u0000\u0000\u0000J\u0007\u0001\u0000"+
		"\u0000\u0000KL\u0005\u0007\u0000\u0000LM\u0003\u000e\u0007\u0000MN\u0005"+
		"\b\u0000\u0000NO\u0003\f\u0006\u0000OP\u0005\t\u0000\u0000P\t\u0001\u0000"+
		"\u0000\u0000QR\u0005\n\u0000\u0000RS\u0005\u0016\u0000\u0000ST\u0005\r"+
		"\u0000\u0000T\u000b\u0001\u0000\u0000\u0000UW\u0003\u0002\u0001\u0000"+
		"VU\u0001\u0000\u0000\u0000WZ\u0001\u0000\u0000\u0000XV\u0001\u0000\u0000"+
		"\u0000XY\u0001\u0000\u0000\u0000Y\r\u0001\u0000\u0000\u0000ZX\u0001\u0000"+
		"\u0000\u0000[\\\u0003\u0010\b\u0000\\\u000f\u0001\u0000\u0000\u0000]^"+
		"\u0003\u0014\n\u0000^_\u0003\u0012\t\u0000_\u0011\u0001\u0000\u0000\u0000"+
		"`a\u0005\u0012\u0000\u0000ab\u0003\u0014\n\u0000bc\u0003\u0012\t\u0000"+
		"cf\u0001\u0000\u0000\u0000df\u0001\u0000\u0000\u0000e`\u0001\u0000\u0000"+
		"\u0000ed\u0001\u0000\u0000\u0000f\u0013\u0001\u0000\u0000\u0000gh\u0003"+
		"\u0018\f\u0000hi\u0003\u0016\u000b\u0000i\u0015\u0001\u0000\u0000\u0000"+
		"jk\u0005\u0011\u0000\u0000kn\u0003\u0018\f\u0000ln\u0001\u0000\u0000\u0000"+
		"mj\u0001\u0000\u0000\u0000ml\u0001\u0000\u0000\u0000n\u0017\u0001\u0000"+
		"\u0000\u0000op\u0003\u001c\u000e\u0000pq\u0003\u001a\r\u0000q\u0019\u0001"+
		"\u0000\u0000\u0000rs\u0005\u000f\u0000\u0000st\u0003\u001c\u000e\u0000"+
		"tu\u0003\u001a\r\u0000ux\u0001\u0000\u0000\u0000vx\u0001\u0000\u0000\u0000"+
		"wr\u0001\u0000\u0000\u0000wv\u0001\u0000\u0000\u0000x\u001b\u0001\u0000"+
		"\u0000\u0000yz\u0003 \u0010\u0000z{\u0003\u001e\u000f\u0000{\u001d\u0001"+
		"\u0000\u0000\u0000|}\u0005\u0010\u0000\u0000}~\u0003 \u0010\u0000~\u007f"+
		"\u0003\u001e\u000f\u0000\u007f\u0082\u0001\u0000\u0000\u0000\u0080\u0082"+
		"\u0001\u0000\u0000\u0000\u0081|\u0001\u0000\u0000\u0000\u0081\u0080\u0001"+
		"\u0000\u0000\u0000\u0082\u001f\u0001\u0000\u0000\u0000\u0083\u0084\u0005"+
		"\u0013\u0000\u0000\u0084\u008d\u0003 \u0010\u0000\u0085\u0086\u0005\u000b"+
		"\u0000\u0000\u0086\u0087\u0003\u000e\u0007\u0000\u0087\u0088\u0005\f\u0000"+
		"\u0000\u0088\u008d\u0001\u0000\u0000\u0000\u0089\u008d\u0005\u0015\u0000"+
		"\u0000\u008a\u008d\u0005\u0014\u0000\u0000\u008b\u008d\u0005\u0016\u0000"+
		"\u0000\u008c\u0083\u0001\u0000\u0000\u0000\u008c\u0085\u0001\u0000\u0000"+
		"\u0000\u008c\u0089\u0001\u0000\u0000\u0000\u008c\u008a\u0001\u0000\u0000"+
		"\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008d!\u0001\u0000\u0000\u0000"+
		"\t%=IXemw\u0081\u008c";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}