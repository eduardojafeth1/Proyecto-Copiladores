# PROYECTO COPILADORES

> [!IMPORTANT]
> Proyecto terminado con exito 🎉

El analizador léxico tiene como objetivo identificar y dividir la entrada en tokens. Los tokens que se deben identificar son:

- **Sistema**: Los sistemas de numeración soportados (Binario, Octal, Decimal, Hexadecimal, Romano, Alternativo, Aleatorio).
- **Número**: El número que se va a convertir.
- **Final**: El símbolo `$` que indica el final de la entrada.

**Tareas a realizar**:
- [x] Definir los tokens `Numero`, `Sistema`, `Final`.
- [x] Crear el lexer utilizando la librería **PLY**.
- [x] Implementar las funciones `t_Sistema`, `t_Numero` y `t_Final` para reconocer los tokens.
- [x] Añadir manejo de errores léxicos en caso de caracteres no válidos.
- [x] Implementar la función `analizadorLexico` para procesar entradas y generar tokens.

---

### 2. **Analizador Sintáctico**

El analizador sintáctico tiene como objetivo analizar la estructura de los tokens generados por el analizador léxico y comprobar si la secuencia es válida según las reglas definidas en la gramática.

**Tareas a realizar**:
- [x] Definir la gramática para la conversión, utilizando reglas como:
  - `expresion : conversion Final`
  - `conversion : SistemaOrigen Numero SistemaDestino`
- [x] Implementar el analizador sintáctico utilizando **PLY** y las reglas gramaticales.
- [x] Implementar las funciones para manejar las reglas de **SistemaOrigen** y **SistemaDestino**.
- [x] Crear las funciones para manejar errores sintácticos.
- [x] Imprimir un mensaje al detectar una conversión válida y los detalles del sistema de origen, número y sistema de destino.
-[x] Crear Funciones de conversion y remplazar el comportamiento en las reglas del analizador Sintactico
---

