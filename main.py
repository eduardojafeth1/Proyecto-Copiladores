from AnalizadorLexico import analizadorLexico
from AnalizadorSintactico import parser


with open('conversiones.txt', 'r') as archivo:
    for linea in archivo:
        print(analizadorLexico(linea))

        
with open("conversiones.txt",'r') as libro:
    for linea in libro:
        linea = linea.strip()
        parser.parse(linea)