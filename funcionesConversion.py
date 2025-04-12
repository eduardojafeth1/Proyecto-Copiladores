import random


def decimal_a_alternativo(decimal):
    return "|" * int(decimal)

def octal_a_alternativo(octal):
    return "|" * int(octal, 8)

def hexadecimal_a_alternativo(hexadecimal):
    return "|" * int(hexadecimal, 16)

def binario_a_alternativo(binario):
    return "|" * int(binario, 2)

def romano_a_alternativo(romano):
    return "|" * romano_a_decimal(romano)

def decimal_a_octal(decimal):
    return oct(decimal)

def decimal_a_hexadecimal(decimal):
    return hex(decimal)

def decimal_a_binario(decimal):
    return bin(decimal)

def decimal_a_romano(decimal):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    romano = ""
    for i in range(len(valores)):
        while decimal >= valores[i]:
            romano += simbolos[i]
            decimal -= valores[i]
    return romano

def octal_a_decimal(octal):
    return int(octal, 8)

def octal_a_hexadecimal(octal):
    return hex(int(octal, 8))

def octal_a_binario(octal):
    return bin(int(octal, 8))

def octal_a_romano(octal):
    return decimal_a_romano(int(octal, 8))

def hexadecimal_a_decimal(hexadecimal):
    return int(hexadecimal, 16)

def hexadecimal_a_octal(hexadecimal):
    return oct(int(hexadecimal, 16))

def hexadecimal_a_binario(hexadecimal):
    return bin(int(hexadecimal, 16))

def hexadecimal_a_romano(hexadecimal):
    return decimal_a_romano(int(hexadecimal, 16))

def binario_a_decimal(binario):
    return int(binario, 2)

def binario_a_octal(binario):
    return oct(int(binario, 2))

def binario_a_hexadecimal(binario):
    return hex(int(binario, 2))

def binario_a_romano(binario):
    return decimal_a_romano(int(binario, 2))

def romano_a_decimal(romano):
    romano = romano.upper()
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    decimal = 0
    i = 0
    while romano != "":
        if romano.startswith(simbolos[i]):
            decimal += valores[i]
            romano = romano[len(simbolos[i]):]
        else:
            i += 1
    return decimal

def romano_a_octal(romano):
    return oct(romano_a_decimal(romano))

def romano_a_hexadecimal(romano):
    return hex(romano_a_decimal(romano))

def romano_a_binario(romano):
    return bin(romano_a_decimal(romano))

def convertir(valor, origen, destino):
    if destino==origen:
        return valor
    elif destino == "Aleatorio":
        return convertir_aleatorio(valor, origen)
    elif origen == "Decimal":
        if destino == "Octal":
            return decimal_a_octal(int(valor))
        elif destino == "Hexadecimal":
            return decimal_a_hexadecimal(int(valor))
        elif destino == "Binario":
            return decimal_a_binario(int(valor))
        elif destino == "Romano":
            return decimal_a_romano(int(valor))
        elif destino == "Alternativo":
            return decimal_a_alternativo(int(valor))
    elif origen == "Octal":
        if destino == "Decimal":
            return octal_a_decimal(valor)
        elif destino == "Hexadecimal":
            return octal_a_hexadecimal(valor)
        elif destino == "Binario":
            return octal_a_binario(valor)
        elif destino == "Romano":
            return octal_a_romano(valor)
        elif destino == "Alternativo":
            return decimal_a_octal(int(valor))
    elif origen == "Hexadecimal":
        if destino == "Decimal":
            return hexadecimal_a_decimal(valor)
        elif destino == "Octal":
            return hexadecimal_a_octal(valor)
        elif destino == "Binario":
            return hexadecimal_a_binario(valor)
        elif destino == "Romano":
            return hexadecimal_a_romano(valor)
        elif destino == "Alternativo":
            return hexadecimal_a_alternativo(valor)
    elif origen == "Binario":
        if destino == "Decimal":
            return binario_a_decimal(valor)
        elif destino == "Octal":
            return binario_a_octal(valor)
        elif destino == "Hexadecimal":
            return binario_a_hexadecimal(valor)
        elif destino == "Romano":
            return binario_a_romano(valor)
        elif destino == "Alternativo":
            return binario_a_alternativo(valor)
    elif origen == "Romano":
        if destino == "Decimal":
            return romano_a_decimal(valor)
        elif destino == "Octal":
            return romano_a_octal(valor)
        elif destino == "Hexadecimal":
            return romano_a_hexadecimal(valor)
        elif destino == "Binario":
            return romano_a_binario(valor)
        elif destino == "Alternativo":
            return romano_a_alternativo(valor)
    
    

def convertir_aleatorio(valor, origen):
    # Lista de posibles destinos
    destinos_posibles = ["Decimal", "Octal", "Hexadecimal", "Binario", "Romano"]
    
    # Filtrar los destinos posibles para que no sea igual al origen
    destinos_posibles = [destino for destino in destinos_posibles if destino != origen]
    
    # Escoge un destino aleatorio
    destino = random.choice(destinos_posibles)
    
    return convertir(valor, origen, destino)

