import ply.lex as lex

tokens =(
    'Numero',
    'Sistema',
    'Final'
)


def t_Sistema(t):
    r'Hexadecimal|Octal|Binario|Romano|Alternativo|Aleatorio|Decimal'
    return t
t_Final=r'\$'

def t_Numero(t):
    r'[A-Fa-f0-9]+'
    t.value = (t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter no válido: {t.value[0]}")
    t.lexer.skip(1)

lexer=lex.lex()


def analizadorLexico(L):
    res=[]
    lexer.input(L)
    for token in lexer:
        res.append( "\n"+f"Línea: {token.lineno} | Tipo: {token.type} | Valor: {token.value}\n")
    return res
    
    




