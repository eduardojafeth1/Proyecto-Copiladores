from AnalizadorSintactico import analizar_sintaxis

while True:
    entrada = input("Ingresa un número y tipo de conversión (ej. 15 binario): ")
    if entrada.lower() in ['salir', 'exit']:
        break
    analizar_sintaxis(entrada)