# Generated from Quetzal.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from build.intermediateCode import *




def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2Q")
        buf.write("\u02d4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \5 \u01d5\n \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%")
        buf.write("\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3<")
        buf.write("\3=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3B\3C\3")
        buf.write("C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\6I\u026c\nI\rI\16")
        buf.write("I\u026d\3I\3I\6I\u0272\nI\rI\16I\u0273\3J\6J\u0277\nJ")
        buf.write("\rJ\16J\u0278\3K\3K\7K\u027d\nK\fK\16K\u0280\13K\3L\3")
        buf.write("L\5L\u0284\nL\3M\3M\3M\7M\u0289\nM\fM\16M\u028c\13M\3")
        buf.write("M\3M\3N\3N\5N\u0292\nN\3O\3O\5O\u0296\nO\3P\3P\3P\3P\5")
        buf.write("P\u029c\nP\3Q\3Q\3R\3R\3S\3S\3T\3T\5T\u02a6\nT\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\3V\5V\u02b1\nV\3V\3V\3V\3V\3W\6W\u02b8")
        buf.write("\nW\rW\16W\u02b9\3W\3W\3X\3X\3X\7X\u02c1\nX\fX\16X\u02c4")
        buf.write("\13X\3X\3X\3X\3X\3X\3Y\3Y\3Y\7Y\u02ce\nY\fY\16Y\u02d1")
        buf.write("\13Y\3Y\3Y\3\u02c2\2Z\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\2\27\2\31\f\33\r\35\16\37\17!\20#\21%\22\'")
        buf.write("\23)\24+\25-\26/\27\61\30\63\31\65\32\67\339\34;\35=\36")
        buf.write("?\37A C!E\"G#I$K%M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63")
        buf.write("i\64k\65m\66o\67q8s9u:w;y<{=}>\177?\u0081@\u0083A\u0085")
        buf.write("B\u0087C\u0089D\u008bE\u008dF\u008fG\u0091H\u0093I\u0095")
        buf.write("J\u0097K\u0099L\u009bM\u009d\2\u009f\2\u00a1\2\u00a3\2")
        buf.write("\u00a5\2\u00a7\2\u00a9\2\u00abN\u00adO\u00afP\u00b1Q\3")
        buf.write("\2\n\4\2\"\"\61\61\5\2\60\60<<^^\3\2\62;\3\2C\\\3\2c|")
        buf.write("\4\2CHch\4\2\13\13\"\"\4\2\f\f\17\17\2\u02ea\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2\2\2\u00b1")
        buf.write("\3\2\2\2\3\u00b3\3\2\2\2\5\u00bb\3\2\2\2\7\u00c0\3\2\2")
        buf.write("\2\t\u00c7\3\2\2\2\13\u00ce\3\2\2\2\r\u00d1\3\2\2\2\17")
        buf.write("\u00d6\3\2\2\2\21\u00dc\3\2\2\2\23\u00e2\3\2\2\2\25\u00e7")
        buf.write("\3\2\2\2\27\u00ec\3\2\2\2\31\u00f2\3\2\2\2\33\u00f7\3")
        buf.write("\2\2\2\35\u00fc\3\2\2\2\37\u0104\3\2\2\2!\u010c\3\2\2")
        buf.write("\2#\u0116\3\2\2\2%\u0123\3\2\2\2\'\u012f\3\2\2\2)\u013d")
        buf.write("\3\2\2\2+\u014a\3\2\2\2-\u015a\3\2\2\2/\u016a\3\2\2\2")
        buf.write("\61\u017e\3\2\2\2\63\u0192\3\2\2\2\65\u01a1\3\2\2\2\67")
        buf.write("\u01af\3\2\2\29\u01b4\3\2\2\2;\u01b8\3\2\2\2=\u01be\3")
        buf.write("\2\2\2?\u01d4\3\2\2\2A\u01d6\3\2\2\2C\u01dc\3\2\2\2E\u01e0")
        buf.write("\3\2\2\2G\u01e5\3\2\2\2I\u01ea\3\2\2\2K\u01f1\3\2\2\2")
        buf.write("M\u01f8\3\2\2\2O\u01fe\3\2\2\2Q\u0203\3\2\2\2S\u0208\3")
        buf.write("\2\2\2U\u020f\3\2\2\2W\u0214\3\2\2\2Y\u021c\3\2\2\2[\u0222")
        buf.write("\3\2\2\2]\u0228\3\2\2\2_\u022d\3\2\2\2a\u0234\3\2\2\2")
        buf.write("c\u0236\3\2\2\2e\u0238\3\2\2\2g\u023a\3\2\2\2i\u023c\3")
        buf.write("\2\2\2k\u023e\3\2\2\2m\u0240\3\2\2\2o\u0242\3\2\2\2q\u0244")
        buf.write("\3\2\2\2s\u0246\3\2\2\2u\u0248\3\2\2\2w\u024a\3\2\2\2")
        buf.write("y\u024d\3\2\2\2{\u024f\3\2\2\2}\u0251\3\2\2\2\177\u0254")
        buf.write("\3\2\2\2\u0081\u0257\3\2\2\2\u0083\u025a\3\2\2\2\u0085")
        buf.write("\u025d\3\2\2\2\u0087\u0260\3\2\2\2\u0089\u0262\3\2\2\2")
        buf.write("\u008b\u0264\3\2\2\2\u008d\u0266\3\2\2\2\u008f\u0268\3")
        buf.write("\2\2\2\u0091\u026b\3\2\2\2\u0093\u0276\3\2\2\2\u0095\u027a")
        buf.write("\3\2\2\2\u0097\u0283\3\2\2\2\u0099\u0285\3\2\2\2\u009b")
        buf.write("\u0291\3\2\2\2\u009d\u0295\3\2\2\2\u009f\u029b\3\2\2\2")
        buf.write("\u00a1\u029d\3\2\2\2\u00a3\u029f\3\2\2\2\u00a5\u02a1\3")
        buf.write("\2\2\2\u00a7\u02a5\3\2\2\2\u00a9\u02a7\3\2\2\2\u00ab\u02b0")
        buf.write("\3\2\2\2\u00ad\u02b7\3\2\2\2\u00af\u02bd\3\2\2\2\u00b1")
        buf.write("\u02ca\3\2\2\2\u00b3\u00b4\7r\2\2\u00b4\u00b5\7t\2\2\u00b5")
        buf.write("\u00b6\7q\2\2\u00b6\u00b7\7i\2\2\u00b7\u00b8\7t\2\2\u00b8")
        buf.write("\u00b9\7c\2\2\u00b9\u00ba\7o\2\2\u00ba\4\3\2\2\2\u00bb")
        buf.write("\u00bc\7h\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be\7p\2\2\u00be")
        buf.write("\u00bf\7e\2\2\u00bf\6\3\2\2\2\u00c0\u00c1\7f\2\2\u00c1")
        buf.write("\u00c2\7g\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4\7k\2\2\u00c4")
        buf.write("\u00c5\7p\2\2\u00c5\u00c6\7g\2\2\u00c6\b\3\2\2\2\u00c7")
        buf.write("\u00c8\7t\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7v\2\2\u00ca")
        buf.write("\u00cb\7w\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7p\2\2\u00cd")
        buf.write("\n\3\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0\7h\2\2\u00d0")
        buf.write("\f\3\2\2\2\u00d1\u00d2\7g\2\2\u00d2\u00d3\7n\2\2\u00d3")
        buf.write("\u00d4\7u\2\2\u00d4\u00d5\7g\2\2\u00d5\16\3\2\2\2\u00d6")
        buf.write("\u00d7\7y\2\2\u00d7\u00d8\7j\2\2\u00d8\u00d9\7k\2\2\u00d9")
        buf.write("\u00da\7n\2\2\u00da\u00db\7g\2\2\u00db\20\3\2\2\2\u00dc")
        buf.write("\u00dd\7r\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7k\2\2\u00df")
        buf.write("\u00e0\7p\2\2\u00e0\u00e1\7v\2\2\u00e1\22\3\2\2\2\u00e2")
        buf.write("\u00e3\7t\2\2\u00e3\u00e4\7g\2\2\u00e4\u00e5\7c\2\2\u00e5")
        buf.write("\u00e6\7f\2\2\u00e6\24\3\2\2\2\u00e7\u00e8\7V\2\2\u00e8")
        buf.write("\u00e9\7t\2\2\u00e9\u00ea\7w\2\2\u00ea\u00eb\7g\2\2\u00eb")
        buf.write("\26\3\2\2\2\u00ec\u00ed\7H\2\2\u00ed\u00ee\7c\2\2\u00ee")
        buf.write("\u00ef\7n\2\2\u00ef\u00f0\7u\2\2\u00f0\u00f1\7g\2\2\u00f1")
        buf.write("\30\3\2\2\2\u00f2\u00f3\7o\2\2\u00f3\u00f4\7c\2\2\u00f4")
        buf.write("\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\32\3\2\2\2\u00f7")
        buf.write("\u00f8\7x\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7k\2\2\u00fa")
        buf.write("\u00fb\7f\2\2\u00fb\34\3\2\2\2\u00fc\u00fd\7q\2\2\u00fd")
        buf.write("\u00fe\7r\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7p\2\2\u0100")
        buf.write("\u0101\7K\2\2\u0101\u0102\7o\2\2\u0102\u0103\7i\2\2\u0103")
        buf.write("\36\3\2\2\2\u0104\u0105\7u\2\2\u0105\u0106\7c\2\2\u0106")
        buf.write("\u0107\7x\2\2\u0107\u0108\7g\2\2\u0108\u0109\7K\2\2\u0109")
        buf.write("\u010a\7o\2\2\u010a\u010b\7i\2\2\u010b \3\2\2\2\u010c")
        buf.write("\u010d\7i\2\2\u010d\u010e\7t\2\2\u010e\u010f\7c\2\2\u010f")
        buf.write("\u0110\7{\2\2\u0110\u0111\7u\2\2\u0111\u0112\7e\2\2\u0112")
        buf.write("\u0113\7c\2\2\u0113\u0114\7n\2\2\u0114\u0115\7g\2\2\u0115")
        buf.write("\"\3\2\2\2\u0116\u0117\7e\2\2\u0117\u0118\7q\2\2\u0118")
        buf.write("\u0119\7n\2\2\u0119\u011a\7q\2\2\u011a\u011b\7t\2\2\u011b")
        buf.write("\u011c\7T\2\2\u011c\u011d\7g\2\2\u011d\u011e\7r\2\2\u011e")
        buf.write("\u011f\7n\2\2\u011f\u0120\7c\2\2\u0120\u0121\7e\2\2\u0121")
        buf.write("\u0122\7g\2\2\u0122$\3\2\2\2\u0123\u0124\7e\2\2\u0124")
        buf.write("\u0125\7q\2\2\u0125\u0126\7n\2\2\u0126\u0127\7q\2\2\u0127")
        buf.write("\u0128\7t\2\2\u0128\u0129\7H\2\2\u0129\u012a\7k\2\2\u012a")
        buf.write("\u012b\7n\2\2\u012b\u012c\7v\2\2\u012c\u012d\7g\2\2\u012d")
        buf.write("\u012e\7t\2\2\u012e&\3\2\2\2\u012f\u0130\7g\2\2\u0130")
        buf.write("\u0131\7f\2\2\u0131\u0132\7i\2\2\u0132\u0133\7g\2\2\u0133")
        buf.write("\u0134\7F\2\2\u0134\u0135\7g\2\2\u0135\u0136\7v\2\2\u0136")
        buf.write("\u0137\7g\2\2\u0137\u0138\7e\2\2\u0138\u0139\7v\2\2\u0139")
        buf.write("\u013a\7k\2\2\u013a\u013b\7q\2\2\u013b\u013c\7p\2\2\u013c")
        buf.write("(\3\2\2\2\u013d\u013e\7u\2\2\u013e\u013f\7c\2\2\u013f")
        buf.write("\u0140\7x\2\2\u0140\u0141\7g\2\2\u0141\u0142\7U\2\2\u0142")
        buf.write("\u0143\7e\2\2\u0143\u0144\7c\2\2\u0144\u0145\7n\2\2\u0145")
        buf.write("\u0146\7g\2\2\u0146\u0147\7K\2\2\u0147\u0148\7o\2\2\u0148")
        buf.write("\u0149\7i\2\2\u0149*\3\2\2\2\u014a\u014b\7i\2\2\u014b")
        buf.write("\u014c\7g\2\2\u014c\u014d\7v\2\2\u014d\u014e\7E\2\2\u014e")
        buf.write("\u014f\7q\2\2\u014f\u0150\7n\2\2\u0150\u0151\7q\2\2\u0151")
        buf.write("\u0152\7t\2\2\u0152\u0153\7R\2\2\u0153\u0154\7c\2\2\u0154")
        buf.write("\u0155\7n\2\2\u0155\u0156\7g\2\2\u0156\u0157\7v\2\2\u0157")
        buf.write("\u0158\7v\2\2\u0158\u0159\7g\2\2\u0159,\3\2\2\2\u015a")
        buf.write("\u015b\7e\2\2\u015b\u015c\7q\2\2\u015c\u015d\7n\2\2\u015d")
        buf.write("\u015e\7q\2\2\u015e\u015f\7t\2\2\u015f\u0160\7O\2\2\u0160")
        buf.write("\u0161\7c\2\2\u0161\u0162\7v\2\2\u0162\u0163\7e\2\2\u0163")
        buf.write("\u0164\7j\2\2\u0164\u0165\7K\2\2\u0165\u0166\7o\2\2\u0166")
        buf.write("\u0167\7c\2\2\u0167\u0168\7i\2\2\u0168\u0169\7g\2\2\u0169")
        buf.write(".\3\2\2\2\u016a\u016b\7g\2\2\u016b\u016c\7p\2\2\u016c")
        buf.write("\u016d\7e\2\2\u016d\u016e\7q\2\2\u016e\u016f\7f\2\2\u016f")
        buf.write("\u0170\7g\2\2\u0170\u0171\7U\2\2\u0171\u0172\7v\2\2\u0172")
        buf.write("\u0173\7g\2\2\u0173\u0174\7i\2\2\u0174\u0175\7c\2\2\u0175")
        buf.write("\u0176\7p\2\2\u0176\u0177\7q\2\2\u0177\u0178\7i\2\2\u0178")
        buf.write("\u0179\7t\2\2\u0179\u017a\7c\2\2\u017a\u017b\7r\2\2\u017b")
        buf.write("\u017c\7j\2\2\u017c\u017d\7{\2\2\u017d\60\3\2\2\2\u017e")
        buf.write("\u017f\7f\2\2\u017f\u0180\7g\2\2\u0180\u0181\7e\2\2\u0181")
        buf.write("\u0182\7q\2\2\u0182\u0183\7f\2\2\u0183\u0184\7g\2\2\u0184")
        buf.write("\u0185\7U\2\2\u0185\u0186\7v\2\2\u0186\u0187\7g\2\2\u0187")
        buf.write("\u0188\7i\2\2\u0188\u0189\7c\2\2\u0189\u018a\7p\2\2\u018a")
        buf.write("\u018b\7q\2\2\u018b\u018c\7i\2\2\u018c\u018d\7t\2\2\u018d")
        buf.write("\u018e\7c\2\2\u018e\u018f\7r\2\2\u018f\u0190\7j\2\2\u0190")
        buf.write("\u0191\7{\2\2\u0191\62\3\2\2\2\u0192\u0193\7i\2\2\u0193")
        buf.write("\u0194\7g\2\2\u0194\u0195\7v\2\2\u0195\u0196\7K\2\2\u0196")
        buf.write("\u0197\7o\2\2\u0197\u0198\7c\2\2\u0198\u0199\7i\2\2\u0199")
        buf.write("\u019a\7g\2\2\u019a\u019b\7J\2\2\u019b\u019c\7g\2\2\u019c")
        buf.write("\u019d\7k\2\2\u019d\u019e\7i\2\2\u019e\u019f\7j\2\2\u019f")
        buf.write("\u01a0\7v\2\2\u01a0\64\3\2\2\2\u01a1\u01a2\7i\2\2\u01a2")
        buf.write("\u01a3\7g\2\2\u01a3\u01a4\7v\2\2\u01a4\u01a5\7K\2\2\u01a5")
        buf.write("\u01a6\7o\2\2\u01a6\u01a7\7c\2\2\u01a7\u01a8\7i\2\2\u01a8")
        buf.write("\u01a9\7g\2\2\u01a9\u01aa\7Y\2\2\u01aa\u01ab\7k\2\2\u01ab")
        buf.write("\u01ac\7f\2\2\u01ac\u01ad\7v\2\2\u01ad\u01ae\7j\2\2\u01ae")
        buf.write("\66\3\2\2\2\u01af\u01b0\7d\2\2\u01b0\u01b1\7q\2\2\u01b1")
        buf.write("\u01b2\7q\2\2\u01b2\u01b3\7n\2\2\u01b38\3\2\2\2\u01b4")
        buf.write("\u01b5\7k\2\2\u01b5\u01b6\7p\2\2\u01b6\u01b7\7v\2\2\u01b7")
        buf.write(":\3\2\2\2\u01b8\u01b9\7h\2\2\u01b9\u01ba\7n\2\2\u01ba")
        buf.write("\u01bb\7q\2\2\u01bb\u01bc\7c\2\2\u01bc\u01bd\7v\2\2\u01bd")
        buf.write("<\3\2\2\2\u01be\u01bf\7e\2\2\u01bf\u01c0\7q\2\2\u01c0")
        buf.write("\u01c1\7n\2\2\u01c1\u01c2\7q\2\2\u01c2\u01c3\7t\2\2\u01c3")
        buf.write(">\3\2\2\2\u01c4\u01d5\5A!\2\u01c5\u01d5\5C\"\2\u01c6\u01d5")
        buf.write("\5E#\2\u01c7\u01d5\5G$\2\u01c8\u01d5\5I%\2\u01c9\u01d5")
        buf.write("\5K&\2\u01ca\u01d5\5M\'\2\u01cb\u01d5\5O(\2\u01cc\u01d5")
        buf.write("\5Q)\2\u01cd\u01d5\5S*\2\u01ce\u01d5\5U+\2\u01cf\u01d5")
        buf.write("\5W,\2\u01d0\u01d5\5Y-\2\u01d1\u01d5\5[.\2\u01d2\u01d5")
        buf.write("\5]/\2\u01d3\u01d5\5_\60\2\u01d4\u01c4\3\2\2\2\u01d4\u01c5")
        buf.write("\3\2\2\2\u01d4\u01c6\3\2\2\2\u01d4\u01c7\3\2\2\2\u01d4")
        buf.write("\u01c8\3\2\2\2\u01d4\u01c9\3\2\2\2\u01d4\u01ca\3\2\2\2")
        buf.write("\u01d4\u01cb\3\2\2\2\u01d4\u01cc\3\2\2\2\u01d4\u01cd\3")
        buf.write("\2\2\2\u01d4\u01ce\3\2\2\2\u01d4\u01cf\3\2\2\2\u01d4\u01d0")
        buf.write("\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4")
        buf.write("\u01d3\3\2\2\2\u01d5@\3\2\2\2\u01d6\u01d7\7Y\2\2\u01d7")
        buf.write("\u01d8\7j\2\2\u01d8\u01d9\7k\2\2\u01d9\u01da\7v\2\2\u01da")
        buf.write("\u01db\7g\2\2\u01dbB\3\2\2\2\u01dc\u01dd\7T\2\2\u01dd")
        buf.write("\u01de\7g\2\2\u01de\u01df\7f\2\2\u01dfD\3\2\2\2\u01e0")
        buf.write("\u01e1\7N\2\2\u01e1\u01e2\7k\2\2\u01e2\u01e3\7o\2\2\u01e3")
        buf.write("\u01e4\7g\2\2\u01e4F\3\2\2\2\u01e5\u01e6\7D\2\2\u01e6")
        buf.write("\u01e7\7n\2\2\u01e7\u01e8\7w\2\2\u01e8\u01e9\7g\2\2\u01e9")
        buf.write("H\3\2\2\2\u01ea\u01eb\7U\2\2\u01eb\u01ec\7k\2\2\u01ec")
        buf.write("\u01ed\7n\2\2\u01ed\u01ee\7x\2\2\u01ee\u01ef\7g\2\2\u01ef")
        buf.write("\u01f0\7t\2\2\u01f0J\3\2\2\2\u01f1\u01f2\7O\2\2\u01f2")
        buf.write("\u01f3\7c\2\2\u01f3\u01f4\7t\2\2\u01f4\u01f5\7q\2\2\u01f5")
        buf.write("\u01f6\7q\2\2\u01f6\u01f7\7p\2\2\u01f7L\3\2\2\2\u01f8")
        buf.write("\u01f9\7I\2\2\u01f9\u01fa\7t\2\2\u01fa\u01fb\7g\2\2\u01fb")
        buf.write("\u01fc\7g\2\2\u01fc\u01fd\7p\2\2\u01fdN\3\2\2\2\u01fe")
        buf.write("\u01ff\7P\2\2\u01ff\u0200\7c\2\2\u0200\u0201\7x\2\2\u0201")
        buf.write("\u0202\7{\2\2\u0202P\3\2\2\2\u0203\u0204\7I\2\2\u0204")
        buf.write("\u0205\7t\2\2\u0205\u0206\7c\2\2\u0206\u0207\7{\2\2\u0207")
        buf.write("R\3\2\2\2\u0208\u0209\7[\2\2\u0209\u020a\7g\2\2\u020a")
        buf.write("\u020b\7n\2\2\u020b\u020c\7n\2\2\u020c\u020d\7q\2\2\u020d")
        buf.write("\u020e\7y\2\2\u020eT\3\2\2\2\u020f\u0210\7C\2\2\u0210")
        buf.write("\u0211\7s\2\2\u0211\u0212\7w\2\2\u0212\u0213\7c\2\2\u0213")
        buf.write("V\3\2\2\2\u0214\u0215\7H\2\2\u0215\u0216\7w\2\2\u0216")
        buf.write("\u0217\7e\2\2\u0217\u0218\7j\2\2\u0218\u0219\7u\2\2\u0219")
        buf.write("\u021a\7k\2\2\u021a\u021b\7c\2\2\u021bX\3\2\2\2\u021c")
        buf.write("\u021d\7D\2\2\u021d\u021e\7n\2\2\u021e\u021f\7c\2\2\u021f")
        buf.write("\u0220\7e\2\2\u0220\u0221\7m\2\2\u0221Z\3\2\2\2\u0222")
        buf.write("\u0223\7Q\2\2\u0223\u0224\7n\2\2\u0224\u0225\7k\2\2\u0225")
        buf.write("\u0226\7x\2\2\u0226\u0227\7g\2\2\u0227\\\3\2\2\2\u0228")
        buf.write("\u0229\7V\2\2\u0229\u022a\7g\2\2\u022a\u022b\7c\2\2\u022b")
        buf.write("\u022c\7n\2\2\u022c^\3\2\2\2\u022d\u022e\7R\2\2\u022e")
        buf.write("\u022f\7w\2\2\u022f\u0230\7t\2\2\u0230\u0231\7r\2\2\u0231")
        buf.write("\u0232\7n\2\2\u0232\u0233\7g\2\2\u0233`\3\2\2\2\u0234")
        buf.write("\u0235\7=\2\2\u0235b\3\2\2\2\u0236\u0237\7<\2\2\u0237")
        buf.write("d\3\2\2\2\u0238\u0239\7.\2\2\u0239f\3\2\2\2\u023a\u023b")
        buf.write("\7a\2\2\u023bh\3\2\2\2\u023c\u023d\7}\2\2\u023dj\3\2\2")
        buf.write("\2\u023e\u023f\7\177\2\2\u023fl\3\2\2\2\u0240\u0241\7")
        buf.write("]\2\2\u0241n\3\2\2\2\u0242\u0243\7_\2\2\u0243p\3\2\2\2")
        buf.write("\u0244\u0245\7*\2\2\u0245r\3\2\2\2\u0246\u0247\7+\2\2")
        buf.write("\u0247t\3\2\2\2\u0248\u0249\7?\2\2\u0249v\3\2\2\2\u024a")
        buf.write("\u024b\7?\2\2\u024b\u024c\7?\2\2\u024cx\3\2\2\2\u024d")
        buf.write("\u024e\7@\2\2\u024ez\3\2\2\2\u024f\u0250\7>\2\2\u0250")
        buf.write("|\3\2\2\2\u0251\u0252\7#\2\2\u0252\u0253\7?\2\2\u0253")
        buf.write("~\3\2\2\2\u0254\u0255\7@\2\2\u0255\u0256\7?\2\2\u0256")
        buf.write("\u0080\3\2\2\2\u0257\u0258\7>\2\2\u0258\u0259\7?\2\2\u0259")
        buf.write("\u0082\3\2\2\2\u025a\u025b\7~\2\2\u025b\u025c\7~\2\2\u025c")
        buf.write("\u0084\3\2\2\2\u025d\u025e\7(\2\2\u025e\u025f\7(\2\2\u025f")
        buf.write("\u0086\3\2\2\2\u0260\u0261\7$\2\2\u0261\u0088\3\2\2\2")
        buf.write("\u0262\u0263\7-\2\2\u0263\u008a\3\2\2\2\u0264\u0265\7")
        buf.write("/\2\2\u0265\u008c\3\2\2\2\u0266\u0267\7,\2\2\u0267\u008e")
        buf.write("\3\2\2\2\u0268\u0269\7\61\2\2\u0269\u0090\3\2\2\2\u026a")
        buf.write("\u026c\5\u00a1Q\2\u026b\u026a\3\2\2\2\u026c\u026d\3\2")
        buf.write("\2\2\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u026f")
        buf.write("\3\2\2\2\u026f\u0271\7\60\2\2\u0270\u0272\5\u00a1Q\2\u0271")
        buf.write("\u0270\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0271\3\2\2\2")
        buf.write("\u0273\u0274\3\2\2\2\u0274\u0092\3\2\2\2\u0275\u0277\5")
        buf.write("\u00a1Q\2\u0276\u0275\3\2\2\2\u0277\u0278\3\2\2\2\u0278")
        buf.write("\u0276\3\2\2\2\u0278\u0279\3\2\2\2\u0279\u0094\3\2\2\2")
        buf.write("\u027a\u027e\5\u00a5S\2\u027b\u027d\5\u009fP\2\u027c\u027b")
        buf.write("\3\2\2\2\u027d\u0280\3\2\2\2\u027e\u027c\3\2\2\2\u027e")
        buf.write("\u027f\3\2\2\2\u027f\u0096\3\2\2\2\u0280\u027e\3\2\2\2")
        buf.write("\u0281\u0284\5? \2\u0282\u0284\5\u00a9U\2\u0283\u0281")
        buf.write("\3\2\2\2\u0283\u0282\3\2\2\2\u0284\u0098\3\2\2\2\u0285")
        buf.write("\u028a\7$\2\2\u0286\u0289\5\u009fP\2\u0287\u0289\t\2\2")
        buf.write("\2\u0288\u0286\3\2\2\2\u0288\u0287\3\2\2\2\u0289\u028c")
        buf.write("\3\2\2\2\u028a\u0288\3\2\2\2\u028a\u028b\3\2\2\2\u028b")
        buf.write("\u028d\3\2\2\2\u028c\u028a\3\2\2\2\u028d\u028e\7$\2\2")
        buf.write("\u028e\u009a\3\2\2\2\u028f\u0292\5\25\13\2\u0290\u0292")
        buf.write("\5\27\f\2\u0291\u028f\3\2\2\2\u0291\u0290\3\2\2\2\u0292")
        buf.write("\u009c\3\2\2\2\u0293\u0296\5\u00a3R\2\u0294\u0296\5\u00a5")
        buf.write("S\2\u0295\u0293\3\2\2\2\u0295\u0294\3\2\2\2\u0296\u009e")
        buf.write("\3\2\2\2\u0297\u029c\5\u009dO\2\u0298\u029c\5\u00a1Q\2")
        buf.write("\u0299\u029c\5g\64\2\u029a\u029c\t\3\2\2\u029b\u0297\3")
        buf.write("\2\2\2\u029b\u0298\3\2\2\2\u029b\u0299\3\2\2\2\u029b\u029a")
        buf.write("\3\2\2\2\u029c\u00a0\3\2\2\2\u029d\u029e\t\4\2\2\u029e")
        buf.write("\u00a2\3\2\2\2\u029f\u02a0\t\5\2\2\u02a0\u00a4\3\2\2\2")
        buf.write("\u02a1\u02a2\t\6\2\2\u02a2\u00a6\3\2\2\2\u02a3\u02a6\t")
        buf.write("\7\2\2\u02a4\u02a6\5\u00a1Q\2\u02a5\u02a3\3\2\2\2\u02a5")
        buf.write("\u02a4\3\2\2\2\u02a6\u00a8\3\2\2\2\u02a7\u02a8\7%\2\2")
        buf.write("\u02a8\u02a9\5\u00a7T\2\u02a9\u02aa\5\u00a7T\2\u02aa\u02ab")
        buf.write("\5\u00a7T\2\u02ab\u02ac\5\u00a7T\2\u02ac\u02ad\5\u00a7")
        buf.write("T\2\u02ad\u02ae\5\u00a7T\2\u02ae\u00aa\3\2\2\2\u02af\u02b1")
        buf.write("\7\17\2\2\u02b0\u02af\3\2\2\2\u02b0\u02b1\3\2\2\2\u02b1")
        buf.write("\u02b2\3\2\2\2\u02b2\u02b3\7\f\2\2\u02b3\u02b4\3\2\2\2")
        buf.write("\u02b4\u02b5\bV\2\2\u02b5\u00ac\3\2\2\2\u02b6\u02b8\t")
        buf.write("\b\2\2\u02b7\u02b6\3\2\2\2\u02b8\u02b9\3\2\2\2\u02b9\u02b7")
        buf.write("\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb")
        buf.write("\u02bc\bW\2\2\u02bc\u00ae\3\2\2\2\u02bd\u02be\5\u008f")
        buf.write("H\2\u02be\u02c2\5\u008dG\2\u02bf\u02c1\13\2\2\2\u02c0")
        buf.write("\u02bf\3\2\2\2\u02c1\u02c4\3\2\2\2\u02c2\u02c3\3\2\2\2")
        buf.write("\u02c2\u02c0\3\2\2\2\u02c3\u02c5\3\2\2\2\u02c4\u02c2\3")
        buf.write("\2\2\2\u02c5\u02c6\5\u008dG\2\u02c6\u02c7\5\u008fH\2\u02c7")
        buf.write("\u02c8\3\2\2\2\u02c8\u02c9\bX\3\2\u02c9\u00b0\3\2\2\2")
        buf.write("\u02ca\u02cb\5\u008fH\2\u02cb\u02cf\5\u008fH\2\u02cc\u02ce")
        buf.write("\n\t\2\2\u02cd\u02cc\3\2\2\2\u02ce\u02d1\3\2\2\2\u02cf")
        buf.write("\u02cd\3\2\2\2\u02cf\u02d0\3\2\2\2\u02d0\u02d2\3\2\2\2")
        buf.write("\u02d1\u02cf\3\2\2\2\u02d2\u02d3\bY\3\2\u02d3\u00b2\3")
        buf.write("\2\2\2\23\2\u01d4\u026d\u0273\u0278\u027e\u0283\u0288")
        buf.write("\u028a\u0291\u0295\u029b\u02a5\u02b0\u02b9\u02c2\u02cf")
        buf.write("\4\b\2\2\2\3\2")
        return buf.getvalue()


class QuetzalLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TK_PROGRAM = 1
    TK_FUNC = 2
    TK_DEFINE = 3
    TK_RETURN = 4
    TK_IF = 5
    TK_ELSE = 6
    TK_WHILE = 7
    TK_PRINT = 8
    TK_READ = 9
    TK_MAIN = 10
    TK_VOID = 11
    TK_OPENIMG = 12
    TK_SAVEIMG = 13
    TK_GRAYSCALE = 14
    TK_COLOR_REPLACE = 15
    TK_COLOR_FILTER = 16
    TK_EDGE_DETECTION = 17
    TK_SCALE_IMAGE = 18
    TK_GET_COLOR_PALETTE = 19
    TK_COLOR_MATCH_IMAGE = 20
    TK_ENCODE_STEGANOGRAPHY = 21
    TK_DECODE_STEGANOGRAPHY = 22
    TK_GET_IMAGE_HEIGHT = 23
    TK_GET_IMAGE_WIDTH = 24
    TK_BOOL = 25
    TK_INT = 26
    TK_FLOAT = 27
    TK_COLOR = 28
    CTE_COLOR = 29
    TK_WHITE = 30
    TK_RED = 31
    TK_LIME = 32
    TK_BLUE = 33
    TK_SILVER = 34
    TK_MAROON = 35
    TK_GREEN = 36
    TK_NAVY = 37
    TK_GRAY = 38
    TK_YELLOW = 39
    TK_AQUA = 40
    TK_FUCHSIA = 41
    TK_BLACK = 42
    TK_OLIVE = 43
    TK_TEAL = 44
    TK_PURPLE = 45
    SYM_SEMI_COL = 46
    SYM_DOUB_COL = 47
    SYM_COMMA = 48
    SYM_UNDER_SCORE = 49
    SYM_CURLY_BRACK_OPEN = 50
    SYM_CURLY_BRACK_CLOSE = 51
    SYM_SQUARE_BRACK_OPEN = 52
    SYM_SQUARE_BRACK_CLOSE = 53
    SYM_PAREN_OPEN = 54
    SYM_PAREN_CLOSE = 55
    SYM_ASSIGN = 56
    SYM_EQUAL = 57
    SYM_GRE_THAN = 58
    SYM_LOW_THAN = 59
    SYM_NOT_EQUAL = 60
    SYM_GRE_EQ = 61
    SYM_LOW_EQ = 62
    SYM_OR = 63
    SYM_AND = 64
    SYM_QUOT = 65
    SYM_PLUS = 66
    SYM_MINUS = 67
    SYM_MULT = 68
    SYM_DIV = 69
    TYPE_FLOAT = 70
    TYPE_INT = 71
    TYPE_ID = 72
    TYPE_COLOR = 73
    CTE_TAG = 74
    TYPE_BOOL = 75
    NEWLINE = 76
    WS = 77
    BLOCK_COMMENT = 78
    LINE_COMMENT = 79

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'program'", "'func'", "'define'", "'return'", "'if'", "'else'", 
            "'while'", "'print'", "'read'", "'main'", "'void'", "'openImg'", 
            "'saveImg'", "'grayscale'", "'colorReplace'", "'colorFilter'", 
            "'edgeDetection'", "'saveScaleImg'", "'getColorPalette'", "'colorMatchImage'", 
            "'encodeSteganography'", "'decodeSteganography'", "'getImageHeight'", 
            "'getImageWidth'", "'bool'", "'int'", "'float'", "'color'", 
            "'White'", "'Red'", "'Lime'", "'Blue'", "'Silver'", "'Maroon'", 
            "'Green'", "'Navy'", "'Gray'", "'Yellow'", "'Aqua'", "'Fuchsia'", 
            "'Black'", "'Olive'", "'Teal'", "'Purple'", "';'", "':'", "','", 
            "'_'", "'{'", "'}'", "'['", "']'", "'('", "')'", "'='", "'=='", 
            "'>'", "'<'", "'!='", "'>='", "'<='", "'||'", "'&&'", "'\"'", 
            "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "TK_PROGRAM", "TK_FUNC", "TK_DEFINE", "TK_RETURN", "TK_IF", 
            "TK_ELSE", "TK_WHILE", "TK_PRINT", "TK_READ", "TK_MAIN", "TK_VOID", 
            "TK_OPENIMG", "TK_SAVEIMG", "TK_GRAYSCALE", "TK_COLOR_REPLACE", 
            "TK_COLOR_FILTER", "TK_EDGE_DETECTION", "TK_SCALE_IMAGE", "TK_GET_COLOR_PALETTE", 
            "TK_COLOR_MATCH_IMAGE", "TK_ENCODE_STEGANOGRAPHY", "TK_DECODE_STEGANOGRAPHY", 
            "TK_GET_IMAGE_HEIGHT", "TK_GET_IMAGE_WIDTH", "TK_BOOL", "TK_INT", 
            "TK_FLOAT", "TK_COLOR", "CTE_COLOR", "TK_WHITE", "TK_RED", "TK_LIME", 
            "TK_BLUE", "TK_SILVER", "TK_MAROON", "TK_GREEN", "TK_NAVY", 
            "TK_GRAY", "TK_YELLOW", "TK_AQUA", "TK_FUCHSIA", "TK_BLACK", 
            "TK_OLIVE", "TK_TEAL", "TK_PURPLE", "SYM_SEMI_COL", "SYM_DOUB_COL", 
            "SYM_COMMA", "SYM_UNDER_SCORE", "SYM_CURLY_BRACK_OPEN", "SYM_CURLY_BRACK_CLOSE", 
            "SYM_SQUARE_BRACK_OPEN", "SYM_SQUARE_BRACK_CLOSE", "SYM_PAREN_OPEN", 
            "SYM_PAREN_CLOSE", "SYM_ASSIGN", "SYM_EQUAL", "SYM_GRE_THAN", 
            "SYM_LOW_THAN", "SYM_NOT_EQUAL", "SYM_GRE_EQ", "SYM_LOW_EQ", 
            "SYM_OR", "SYM_AND", "SYM_QUOT", "SYM_PLUS", "SYM_MINUS", "SYM_MULT", 
            "SYM_DIV", "TYPE_FLOAT", "TYPE_INT", "TYPE_ID", "TYPE_COLOR", 
            "CTE_TAG", "TYPE_BOOL", "NEWLINE", "WS", "BLOCK_COMMENT", "LINE_COMMENT" ]

    ruleNames = [ "TK_PROGRAM", "TK_FUNC", "TK_DEFINE", "TK_RETURN", "TK_IF", 
                  "TK_ELSE", "TK_WHILE", "TK_PRINT", "TK_READ", "TK_TRUE", 
                  "TK_FALSE", "TK_MAIN", "TK_VOID", "TK_OPENIMG", "TK_SAVEIMG", 
                  "TK_GRAYSCALE", "TK_COLOR_REPLACE", "TK_COLOR_FILTER", 
                  "TK_EDGE_DETECTION", "TK_SCALE_IMAGE", "TK_GET_COLOR_PALETTE", 
                  "TK_COLOR_MATCH_IMAGE", "TK_ENCODE_STEGANOGRAPHY", "TK_DECODE_STEGANOGRAPHY", 
                  "TK_GET_IMAGE_HEIGHT", "TK_GET_IMAGE_WIDTH", "TK_BOOL", 
                  "TK_INT", "TK_FLOAT", "TK_COLOR", "CTE_COLOR", "TK_WHITE", 
                  "TK_RED", "TK_LIME", "TK_BLUE", "TK_SILVER", "TK_MAROON", 
                  "TK_GREEN", "TK_NAVY", "TK_GRAY", "TK_YELLOW", "TK_AQUA", 
                  "TK_FUCHSIA", "TK_BLACK", "TK_OLIVE", "TK_TEAL", "TK_PURPLE", 
                  "SYM_SEMI_COL", "SYM_DOUB_COL", "SYM_COMMA", "SYM_UNDER_SCORE", 
                  "SYM_CURLY_BRACK_OPEN", "SYM_CURLY_BRACK_CLOSE", "SYM_SQUARE_BRACK_OPEN", 
                  "SYM_SQUARE_BRACK_CLOSE", "SYM_PAREN_OPEN", "SYM_PAREN_CLOSE", 
                  "SYM_ASSIGN", "SYM_EQUAL", "SYM_GRE_THAN", "SYM_LOW_THAN", 
                  "SYM_NOT_EQUAL", "SYM_GRE_EQ", "SYM_LOW_EQ", "SYM_OR", 
                  "SYM_AND", "SYM_QUOT", "SYM_PLUS", "SYM_MINUS", "SYM_MULT", 
                  "SYM_DIV", "TYPE_FLOAT", "TYPE_INT", "TYPE_ID", "TYPE_COLOR", 
                  "CTE_TAG", "TYPE_BOOL", "FRAG_LETTER", "FRAG_FOLLOW", 
                  "FRAG_DIGIT", "FRAG_UPPER_CASE", "FRAG_LOWER_CASE", "FRAG_HEX_VAL", 
                  "FRAG_HEX_COLOR", "NEWLINE", "WS", "BLOCK_COMMENT", "LINE_COMMENT" ]

    grammarFileName = "Quetzal.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


