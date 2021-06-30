from tex_lexer import TeX_Lexer

if __name__ == "__main__":
    lex = TeX_Lexer()
    input = [
        r"some text and words",            # Words
        r"some text with a \controlsq",    # Words + variable call
        r"some text with a \controlsq(arg1, arg2)",    # Words + function call
        r"some text with a \controlsq{literal text}",    # Words + literal call
        r"more text with $ math here $",   # Words + classic inline math
        r"more text with \( math here \)",   # Words + modern inline math
        r"more text with $$ math here $$",   # Words + classic multiline math
        r"more text with \[ math here \]",   # Words + classic multiline math
        r"more text with $ math here \myid_123$",   # Words + classic inline math + variable call
        r"more text with \( math here \myid_123\)",   # Words + modern inline math + variable call
        r"more text with $$ math here \myid_123 $$",   # Words + classic multiline math + variable call
        r"more text with \[ math here \myid_123 \]",   # Words + classic multiline math + variable call
        r"more text with $ math here \myfunction_1(arg1, arg2) $",   # Words + classic inline math + function call
        r"more text with \( math here \myfunction_1(arg1, arg2) \)",   # Words + modern inline math + function call
        r"more text with $$ math here \myfunction_1(arg1, arg2) $$",   # Words + classic multiline math + function call
        r"more text with \[ math here \myfunction_1(arg1, arg2) \]",   # Words + classic multiline math + function call
        r"more text with $ math here \literal_text{some text} $",   # Words + classic inline math + literal call
        r"more text with \( math here \literal_text{some text} \)",   # Words + modern inline math + literal call
        r"more text with $$ math here \literal_text{some text} $$",   # Words + classic multiline math + literal call
        r"more text with \[ math here \literal_text{some text} \]",   # Words + classic multiline math + literal call
        r"some text with {program access}"  # Words + program access
    ]