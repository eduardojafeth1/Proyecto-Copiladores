import ply.yacc as yacc
from AnalizadorLexico import *

# Lista de tokens
tokens = ['NUMERO', 'TIPO_CONVERSION']

# Definimos las reglas de la gramática
def p_expresion(p):
    'expresion : NUMERO TIPO_CONVERSION'
    numero = int(p[1])  # El número en base decimal
    tipo_conversion = p[2]  # El tipo de conversión
    convertir(numero, tipo_conversion)

# Manejo de errores de sintaxis
def p_error(p):
    print("Error de sintaxis")

# Función para realizar la conversión
def convertir(numero, tipo_conversion):
    if tipo_conversion == "hexadecimal":
        print(f"Hexadecimal: {hex(numero)[2:].upper()}")
    elif tipo_conversion == "octal":
        print(f"Octal: {oct(numero)[2:]}")
    elif tipo_conversion == "binario":
        print(f"Binario: {bin(numero)[2:]}")
    elif tipo_conversion == "romano":
        print(f"Romano: {decimal_a_romano(numero)}")
    elif tipo_conversion == "alternativo":
        print(f"Alternativo (base 5): {decimal_a_alternativo(numero)}")
    elif tipo_conversion == "aleatorio":
        # Conversión aleatoria: elegir entre las conversiones disponibles
        import random
        conversiones = ['hexadecimal', 'octal', 'binario', 'romano', 'alternativo']
        tipo_conversion = random.choice(conversiones)
        convertir(numero, tipo_conversion)

# Función para convertir a números romanos
def decimal_a_romano(numero):
    numerales_romanos = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    romano = ""
    for valor, simbolo in numerales_romanos:
        while numero >= valor:
            romano += simbolo
            numero -= valor
    return romano

# Función para convertir a un sistema alternativo (base 5 en este caso)
def decimal_a_alternativo(numero):
    base = 5
    digits = []
    while numero:
        digits.append(str(numero % base))
        numero //= base
    return ''.join(digits[::-1])

# Construir el parser
parser = yacc.yacc()

# Función para analizar la entrada
def analizar_sintaxis(entrada):
    parser.parse(entrada)

