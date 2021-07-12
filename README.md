# TeX_Parser
We imagine a markup programming language that preserves TeX's 
syntax but does completely away with the concept of macro expansion.
We perform lexical analysis and recursive parsing for the imaginary language.

In this imaginary language, the user can 
* Access an object oriented base language that controls display
* Write literal text to be displayed
* Enter math mode and write normal TeX math syntax.
* Forget the nightmares of TeX's lunacy (more of wishful thinking)

The main idea is to not rely on TeX syntax to program the document, because it's very stupid syntax, 
but rather rely on another language. LuaTeX is trying to do this, but evil 
remnants of TeX continue to haunt the modern TeX-engine and they'll never go away. Clearly, a 
better idea is to just stop making TeX engines, which is the attitude of this imaginary language.

A sample of the language would appear as below:
```
def multiply(x, y):
    # Here's a comment. This is a function definition. We imagine python-like syntax with dynamic typing and
    # built-in memory management.
    return x * y
    
\begin(document) # Start the document
    Here is some text. Now here is some access to the base programming language 
    instantiated by curly brackets:
    {
    a = 1
    b = 2
    render(multiply(a,b))
    }
    Here, ``render'' would be a built in function that instructs what it is to be displayed.
    
    In TeX, \{ brackets introduce ``grouping.'' But TeX's concept of grouping is archaic and conflicts
    with the modern notion of lexical scoping. So we do away with it and use \{ brackets to access the 
    base language.
    
    In this imaginary language, the previous example could have been achieved by calling \multiply(a, b). 
    The backslash allows us to call a function, in this case ``multiply'', supply arguments to it, 
    in this case a and b, and display the return of the function, in this case, the number 2.
     
    We would also allow creating functions that take in literal text so we could 
    do something like \textcolor(red){this text is red!}. Finally, one could also 
    store a variable {res = 10} and call it via \res. 
    
    Math would not even change at all, and someone could use $x = 1$, \(\phi(x) = x^2\), 
    $$ 
        \int f(x)dx 
    $$
    or
    \[
        \sum_{i} x_i \otimes y_i. 
    \] 
    One could start a section as below, and similarly, a chapter heading, subsection, etc.
    \section(My title)
    
    The ideal form of this language would be where 
    \begin(itemize)
        \item(1) Standard TeX macros would be lifted to programming functions that perform procedures and 
        optionally print text to the document. 
        \item(2) All commonly used, useful TeX macros variously distributed through all kinds of 
        packages would be united into various standard libraries that could be imported, making the entire 
        process of writing documents easier, more organized, and intuitive.
        \item(3) The keyword ``\\begin'' would be a wrapper function for instantiating an object-oriented 
        like data structure, which we would call an ``environment'', that a user could easily create and design \emph{in the 
        language of the base programming language} and \emph{not} in any kind of awkward TeX syntax 
    \end(itemize)   
\end(document)
```

