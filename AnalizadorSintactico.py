import ply.yacc as yacc
from AnalizadorLexico import tokens, lexer  

import random

# === Funciones de conversión ===

# === Regla inicial ===
def p_expresion(p):
    'expresion : conversion Final'

def p_conversion(p):
    'conversion : SistemaOrigen Numero SistemaDestino'
    print(f"Conversión válida: De {p[1]} a {p[3]} con el número {p[2]}")

# Definir las reglas de SistemaOrigen y SistemaDestino
def p_SistemaOrigen(p):
    'SistemaOrigen : Sistema'
    p[0] = p[1]  # Asignamos el valor del sistema de origen

def p_SistemaDestino(p):
    'SistemaDestino : Sistema'
    p[0] = p[1]  # Asignamos el valor del sistema de destino


def p_error(t):
    if t:
        print(f"[SINTÁCTICO] Error de sintaxis con '{t.value}' en línea {t.lineno}")
    else:
        print("[SINTÁCTICO] Error de sintaxis al final de la entrada.")


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
parser = yacc.yacc()

with open('conversiones.txt', 'r') as archivo:
    for linea in archivo:
        parser.parse(linea)
    print(parser)