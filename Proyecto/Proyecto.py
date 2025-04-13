"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from AnalizadorSintactico import parser,analizadorSintactico
from AnalizadorLexico import analizadorLexico

from rxconfig import config

sistemas_origen = ["Binario", "Octal", "Decimal", "Hexadecimal"]
sistemas_destino = ["Binario", "Octal", "Decimal", "Hexadecimal", "Romano", "Aleatorio","Alternativo"]

class State(rx.State):
    """The app state."""
    sistema_origen: str = "Decimal"
    sistema_destino: str = "Binario"
    numero: str = ""
    salida: str = ""
    tokens=[]

    @rx.event
    def mostrar_datos(self):

        entrada=self.sistema_origen+" "+self.numero+" "+self.sistema_destino+"$"
        if self.numero:
            salida= analizadorSintactico(entrada)
            self.salida=str(salida)
        else:
            self.salida	= "no hay nada"
        self.tokens= analizadorLexico(entrada)



    ...


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Conversor de Sistemas Numéricos", size="9"),
            rx.select(
                sistemas_origen,
                value=State.sistema_origen,
                on_change=State.set_sistema_origen,
                placeholder="Selecciona sistema de origen"
            ),
            rx.input(
                placeholder="Ingrese el número",
                on_blur=State.set_numero,
                border_radius="md"
            ),
            rx.select(
                sistemas_destino,
                value=State.sistema_destino,
                on_change=State.set_sistema_destino,
                placeholder="Selecciona sistema de destino"
            ),
            rx.button("Mostrar datos", on_click=State.mostrar_datos),
            rx.box(
    rx.hstack(
        rx.box(
            rx.heading("Analizis sintactico",color="#111"),
            rx.text(State.salida, color="#000"),
            width="50%",
            padding="1em"
        ),

     
        rx.box(
            width="1px",
            background_color="#ccc",  
            height="100%"
        ),

        rx.box(
            rx.heading("Analizis Lexico",color="#111"),
            rx.foreach(
                State.tokens,
                lambda t: rx.text(t, color="#000",size="3")
                    ),
            width="50%",
            padding="1em"
        ),
        width="100%",
        height="100%",
        align_items="stretch"
    ),

    border="1px solid #ccc",
    padding="1em",
    margin_top="1em",
    border_radius="34px",
    background_color="#f9f9f9",
    width="50vw",
    height="50vh",
)

           

        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
