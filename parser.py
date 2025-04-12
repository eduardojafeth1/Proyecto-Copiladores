import ply.lex as lex
import ply.yacc as yacc
import random

# === LISTA DE TOKENS ===
tokens = (
    'NUMERO',
    'TIPO',
    'DOLAR',
)

# === TOKENS REGEX ===
t_DOLAR = r'\$'
t_ignore = ' \t'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TIPO(t):
    r'Hexadecimal|Binario|Octal|Romano|Alternativo|Aleatorio'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"[LÉXICO] Token ilegal '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

# === CREAR ANALIZADOR LÉXICO ===
lexer = lex.lex()


# === FUNCIONES DE CONVERSIÓN ===

def decimal_a_romano(n):
    val = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = ''
    for (arab, rom) in val:
        while n >= arab:
            res += rom
            n -= arab
    return res

def convertir(numero, tipo):
    if tipo == 'Hexadecimal':
        return hex(numero)[2:].upper()
    elif tipo == 'Binario':
        return bin(numero)[2:]
    elif tipo == 'Octal':
        return oct(numero)[2:]
    elif tipo == 'Romano':
        return decimal_a_romano(numero)
    elif tipo == 'Alternativo':
        return f"[ALT:{numero}]"
    elif tipo == 'Aleatorio':
        tipo_random = random.choice(['Hexadecimal', 'Binario', 'Octal', 'Romano'])
        return convertir(numero, tipo_random)
    else:
        return "Tipo desconocido"


# === GRAMÁTICA ===

def p_expresion(p):
    'expresion : NUMERO TIPO DOLAR'
    resultado = convertir(p[1], p[2])
    print("\n🧠 Resultado de conversión:")
    print(f"  - Número: {p[1]}")
    print(f"  - Tipo: {p[2]}")
    print(f"  - Resultado: {resultado}")

def p_error(p):
    print("[SINTÁCTICO] Error de sintaxis.")

# === CREAR ANALIZADOR SINTÁCTICO ===
parser = yacc.yacc()


# === PRUEBA DEL PROGRAMA ===
if __name__ == '__main__':
    entrada = input("📥 Ingrese cadena (ej. 123Romano$): ").strip()
    print("\n🔍 Tokens encontrados:")
    lexer.input(entrada)
    for tok in lexer:
        print(f"  Línea {tok.lineno} → Tipo: {tok.type}, Valor: {tok.value}")
    
    # Parsear
    print("\n📦 Analizando sintaxis...")
    parser.parse(entrada)
