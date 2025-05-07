// Generated from c:/Users/8760659/compiladores/grammar/Arara.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class AraraLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, ID=15, INT=16, STRING=17, 
		OPSUM=18, OPMULT=19, OPCOMP=20, OPLOG=21, WS=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "ID", "INT", "STRING", "OPSUM", 
			"OPMULT", "OPCOMP", "OPLOG", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'leia'", "'('", "')'", "';'", "'escreva'", "'<-'", "'se'", "'entao'", 
			"'fimse'", "'senao'", "'enquanto'", "'faca'", "'fimenquanto'", "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "ID", "INT", "STRING", "OPSUM", "OPMULT", "OPCOMP", 
			"OPLOG", "WS"
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


	public AraraLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Arara.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0016\u00a8\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0005\u000ew\b\u000e\n\u000e"+
		"\f\u000ez\t\u000e\u0001\u000f\u0004\u000f}\b\u000f\u000b\u000f\f\u000f"+
		"~\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0005\u0010\u0085\b"+
		"\u0010\n\u0010\f\u0010\u0088\t\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0003\u0013\u009a\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0003\u0014\u00a0\b\u0014\u0001\u0015\u0004\u0015\u00a3\b"+
		"\u0015\u000b\u0015\f\u0015\u00a4\u0001\u0015\u0001\u0015\u0000\u0000\u0016"+
		"\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r"+
		"\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016\u0001"+
		"\u0000\u0007\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001\u000009\u0002"+
		"\u0000\"\"\\\\\u0002\u0000++--\u0002\u0000**//\u0003\u0000\t\n\r\r  \u00b2"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0001-\u0001\u0000\u0000\u0000\u00032"+
		"\u0001\u0000\u0000\u0000\u00054\u0001\u0000\u0000\u0000\u00076\u0001\u0000"+
		"\u0000\u0000\t8\u0001\u0000\u0000\u0000\u000b@\u0001\u0000\u0000\u0000"+
		"\rC\u0001\u0000\u0000\u0000\u000fF\u0001\u0000\u0000\u0000\u0011L\u0001"+
		"\u0000\u0000\u0000\u0013R\u0001\u0000\u0000\u0000\u0015X\u0001\u0000\u0000"+
		"\u0000\u0017a\u0001\u0000\u0000\u0000\u0019f\u0001\u0000\u0000\u0000\u001b"+
		"r\u0001\u0000\u0000\u0000\u001dt\u0001\u0000\u0000\u0000\u001f|\u0001"+
		"\u0000\u0000\u0000!\u0080\u0001\u0000\u0000\u0000#\u008b\u0001\u0000\u0000"+
		"\u0000%\u008d\u0001\u0000\u0000\u0000\'\u0099\u0001\u0000\u0000\u0000"+
		")\u009f\u0001\u0000\u0000\u0000+\u00a2\u0001\u0000\u0000\u0000-.\u0005"+
		"l\u0000\u0000./\u0005e\u0000\u0000/0\u0005i\u0000\u000001\u0005a\u0000"+
		"\u00001\u0002\u0001\u0000\u0000\u000023\u0005(\u0000\u00003\u0004\u0001"+
		"\u0000\u0000\u000045\u0005)\u0000\u00005\u0006\u0001\u0000\u0000\u0000"+
		"67\u0005;\u0000\u00007\b\u0001\u0000\u0000\u000089\u0005e\u0000\u0000"+
		"9:\u0005s\u0000\u0000:;\u0005c\u0000\u0000;<\u0005r\u0000\u0000<=\u0005"+
		"e\u0000\u0000=>\u0005v\u0000\u0000>?\u0005a\u0000\u0000?\n\u0001\u0000"+
		"\u0000\u0000@A\u0005<\u0000\u0000AB\u0005-\u0000\u0000B\f\u0001\u0000"+
		"\u0000\u0000CD\u0005s\u0000\u0000DE\u0005e\u0000\u0000E\u000e\u0001\u0000"+
		"\u0000\u0000FG\u0005e\u0000\u0000GH\u0005n\u0000\u0000HI\u0005t\u0000"+
		"\u0000IJ\u0005a\u0000\u0000JK\u0005o\u0000\u0000K\u0010\u0001\u0000\u0000"+
		"\u0000LM\u0005f\u0000\u0000MN\u0005i\u0000\u0000NO\u0005m\u0000\u0000"+
		"OP\u0005s\u0000\u0000PQ\u0005e\u0000\u0000Q\u0012\u0001\u0000\u0000\u0000"+
		"RS\u0005s\u0000\u0000ST\u0005e\u0000\u0000TU\u0005n\u0000\u0000UV\u0005"+
		"a\u0000\u0000VW\u0005o\u0000\u0000W\u0014\u0001\u0000\u0000\u0000XY\u0005"+
		"e\u0000\u0000YZ\u0005n\u0000\u0000Z[\u0005q\u0000\u0000[\\\u0005u\u0000"+
		"\u0000\\]\u0005a\u0000\u0000]^\u0005n\u0000\u0000^_\u0005t\u0000\u0000"+
		"_`\u0005o\u0000\u0000`\u0016\u0001\u0000\u0000\u0000ab\u0005f\u0000\u0000"+
		"bc\u0005a\u0000\u0000cd\u0005c\u0000\u0000de\u0005a\u0000\u0000e\u0018"+
		"\u0001\u0000\u0000\u0000fg\u0005f\u0000\u0000gh\u0005i\u0000\u0000hi\u0005"+
		"m\u0000\u0000ij\u0005e\u0000\u0000jk\u0005n\u0000\u0000kl\u0005q\u0000"+
		"\u0000lm\u0005u\u0000\u0000mn\u0005a\u0000\u0000no\u0005n\u0000\u0000"+
		"op\u0005t\u0000\u0000pq\u0005o\u0000\u0000q\u001a\u0001\u0000\u0000\u0000"+
		"rs\u0005!\u0000\u0000s\u001c\u0001\u0000\u0000\u0000tx\u0007\u0000\u0000"+
		"\u0000uw\u0007\u0001\u0000\u0000vu\u0001\u0000\u0000\u0000wz\u0001\u0000"+
		"\u0000\u0000xv\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000y\u001e"+
		"\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000{}\u0007\u0002\u0000"+
		"\u0000|{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000~|\u0001\u0000"+
		"\u0000\u0000~\u007f\u0001\u0000\u0000\u0000\u007f \u0001\u0000\u0000\u0000"+
		"\u0080\u0086\u0005\"\u0000\u0000\u0081\u0085\b\u0003\u0000\u0000\u0082"+
		"\u0083\u0005\\\u0000\u0000\u0083\u0085\t\u0000\u0000\u0000\u0084\u0081"+
		"\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0088"+
		"\u0001\u0000\u0000\u0000\u0086\u0084\u0001\u0000\u0000\u0000\u0086\u0087"+
		"\u0001\u0000\u0000\u0000\u0087\u0089\u0001\u0000\u0000\u0000\u0088\u0086"+
		"\u0001\u0000\u0000\u0000\u0089\u008a\u0005\"\u0000\u0000\u008a\"\u0001"+
		"\u0000\u0000\u0000\u008b\u008c\u0007\u0004\u0000\u0000\u008c$\u0001\u0000"+
		"\u0000\u0000\u008d\u008e\u0007\u0005\u0000\u0000\u008e&\u0001\u0000\u0000"+
		"\u0000\u008f\u0090\u0005=\u0000\u0000\u0090\u009a\u0005=\u0000\u0000\u0091"+
		"\u0092\u0005!\u0000\u0000\u0092\u009a\u0005=\u0000\u0000\u0093\u009a\u0005"+
		"<\u0000\u0000\u0094\u0095\u0005<\u0000\u0000\u0095\u009a\u0005=\u0000"+
		"\u0000\u0096\u009a\u0005>\u0000\u0000\u0097\u0098\u0005>\u0000\u0000\u0098"+
		"\u009a\u0005=\u0000\u0000\u0099\u008f\u0001\u0000\u0000\u0000\u0099\u0091"+
		"\u0001\u0000\u0000\u0000\u0099\u0093\u0001\u0000\u0000\u0000\u0099\u0094"+
		"\u0001\u0000\u0000\u0000\u0099\u0096\u0001\u0000\u0000\u0000\u0099\u0097"+
		"\u0001\u0000\u0000\u0000\u009a(\u0001\u0000\u0000\u0000\u009b\u009c\u0005"+
		"&\u0000\u0000\u009c\u00a0\u0005&\u0000\u0000\u009d\u009e\u0005|\u0000"+
		"\u0000\u009e\u00a0\u0005|\u0000\u0000\u009f\u009b\u0001\u0000\u0000\u0000"+
		"\u009f\u009d\u0001\u0000\u0000\u0000\u00a0*\u0001\u0000\u0000\u0000\u00a1"+
		"\u00a3\u0007\u0006\u0000\u0000\u00a2\u00a1\u0001\u0000\u0000\u0000\u00a3"+
		"\u00a4\u0001\u0000\u0000\u0000\u00a4\u00a2\u0001\u0000\u0000\u0000\u00a4"+
		"\u00a5\u0001\u0000\u0000\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6"+
		"\u00a7\u0006\u0015\u0000\u0000\u00a7,\u0001\u0000\u0000\u0000\b\u0000"+
		"x~\u0084\u0086\u0099\u009f\u00a4\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}