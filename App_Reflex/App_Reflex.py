import reflex as rx


class State(rx.State):
    mensaje = "Bienvenido al mundo marino 🌊"

    def oceano(self):
        self.mensaje = "El océano cubre más del 70% de la Tierra 🌎"

    def coral(self):
        self.mensaje = "Los arrecifes de coral son hogar de miles de especies 🪸"

    def calma(self):
        self.mensaje = "El sonido del mar transmite tranquilidad y paz 💙"


def index():
    return rx.center(
        rx.vstack(

            rx.heading(
                "Ocean Blue",
                size="9",
                color="#0B3C5D",
            ),

            rx.text(
                State.mensaje,
                font_size="22px",
                color="#134B70",
                text_align="center",
            ),

            rx.hstack(

                rx.button(
                    "Océano",
                    on_click=State.oceano,
                    bg="#4DA8DA",
                    color="white",
                    border_radius="12px",
                    padding_x="20px",
                    _hover={"bg": "#2E8BC0"},
                ),

                rx.button(
                    "Corales",
                    on_click=State.coral,
                    bg="#62B6CB",
                    color="white",
                    border_radius="12px",
                    padding_x="20px",
                    _hover={"bg": "#3A86A8"},
                ),

                rx.button(
                    "Calma",
                    on_click=State.calma,
                    bg="#5FA8D3",
                    color="white",
                    border_radius="12px",
                    padding_x="20px",
                    _hover={"bg": "#417D9A"},
                ),

                spacing="4",
            ),

            rx.box(
                rx.text(
                    "Explora un diseño inspirado en el océano utilizando Reflex y Python.",
                    color="#0B3C5D",
                    text_align="center",
                    font_size="18px",
                ),
                bg="white",
                padding="20px",
                border_radius="15px",
                width="60%",
                box_shadow="0px 4px 10px rgba(0,0,0,0.1)",
            ),

            spacing="7",
            align="center",
        ),

        bg="linear-gradient(180deg, #DFF6FF, #B8E8FC, #7CD1F9)",
        width="100%",
        height="100vh",
    )


app = rx.App()
app.add_page(index)