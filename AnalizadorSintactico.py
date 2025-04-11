import ply.yacc as yacc
from AnalizadorLexico import tokens, lexer  
from funcionesConversion import convertir

global_var=""
# === Regla inicial ===
def p_expresion(p):
    'expresion : conversion Final'
    p[0] = p[1] 
    return p[0]

def p_conversion(p):
    'conversion : SistemaOrigen Numero SistemaDestino'
    p[0]=convertir(p[2],p[1],p[3])
    global global_var
    global_var=f"Conversión válida: De {p[1]} a {p[3]} con el número {p[2]} resultado:{p[0]}"
# Definir las reglas de SistemaOrigen y SistemaDestino
def p_SistemaOrigen(p):
    'SistemaOrigen : Sistema'
    p[0] = p[1]  # Asignamos el valor del sistema de origen

def p_SistemaDestino(p):
    'SistemaDestino : Sistema'
    p[0] = p[1]  # Asignamos el valor del sistema de destino


def p_error(p):
    if p:
       global global_var 
       global_var= f"[SINTÁCTICO] Error de sintaxis con '{p.value}' en línea {p.lineno}"
    else:
       
       global_var = "[SINTÁCTICO] Error de sintaxis al final de la entrada."
    p="error"
    return "error"

parser = yacc.yacc()

def analizadorSintactico(input):
    res=""
    print(input)
    try:
        res=str(parser.parse(input))
    except Exception as e:
        return str(e)
    print(res)
    return global_var

'''with open("conversiones.txt",'r') as libro:
    for linea in libro:
        linea = linea.strip()
        parser.parse(linea)
        print("\n")'''
