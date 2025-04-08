import ply.lex as lex

tokens =(
    'Numero',
    'Destino',
    'Final'
)


t_Destino=r'Hexadecimal|Octal|Binario|Romano|Alternativo|Aleatorio'
t_Final=r'\$'

def t_Numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.valor)

t_ignore = ' \t\n'

def t_error(t):
    print(f"Carácter no válido: {t.value[0]}")
    t.lexer.skip(1)

lexer=lex.lex()


def analizadorLexico(L):
    lexer.input(L)
    for token in lexer:
        print(token)
    
# Abrir el archivo en modo lectura


