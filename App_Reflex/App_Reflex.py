import reflex as rx

# COLORES
bg = "#f5eee6"
primary = "#6b3e26"
secondary = "#c8a27a"

# -------- NAVBAR --------
def navbar():
    return rx.hstack(
        rx.text("Coffee", font_size="24px", font_weight="bold", color=primary),
        rx.spacer(),
        rx.hstack(
            rx.text("Inicio"),
            rx.text("Menú"),
            rx.text("Historia"),
            rx.text("Ubicación"),
            rx.text("Contacto"),
            spacing="4",
            color=primary
        ),
        padding="20px",
        bg=bg
    )

# -------- HERO --------
def hero():
    return rx.hstack(
        rx.vstack(
            rx.heading("¡Disfruta la infusión perfecta!", size="8", color=primary),
            rx.text("Disfruta de un café premium elaborado con cariño.", color="#333"),
            rx.hstack(
                rx.button(
                    "Haz el pedido ahora",
                    bg=primary,
                    color="white",
                    on_click=rx.window_alert("Pedido realizado ☕")
                ),
                rx.link(
                    rx.button("Más información", bg=secondary),
                    href="#menu"
                ),
                spacing="3"
            ),
            align="start",
            spacing="4"
        ),
        rx.image(
            src="https://images.unsplash.com/photo-1509042239860-f550ce710b93",
            width="420px",
            border_radius="20px"
        ),
        spacing="6",
        padding="60px",
        bg=bg
    )

# -------- FEATURES --------
def features():
    def item(title):
        return rx.vstack(
            rx.box(
                width="60px",
                height="60px",
                border_radius="50%",
                bg=secondary
            ),
            rx.text(title, font_weight="bold", color=primary),
            spacing="3",
            align="center"
        )

    return rx.hstack(
        item("Espresso"),
        item("Latte"),
        item("Cold Brew"),
        item("Cappuccino"),
        spacing="8",
        justify="center",
        padding="50px",
        bg="white",
        id="menu"
    )

# -------- WHY US --------
def why_us():
    return rx.hstack(
        rx.box(
            rx.vstack(
                rx.heading("Why Choose Us?", size="7", color="white"),
                rx.text("Ofrecemos café de alta calidad en un ambiente acogedor."),
                rx.button("Leer más", bg="white", color=primary),
                align="start",
                spacing="4"
            ),
            bg=primary,
            color="white",
            padding="40px",
            width="50%"
        ),
        rx.box(
            rx.vstack(
                rx.heading("Oferta Especial", size="6", color=primary),
                rx.text("2x1 de 10am a 12pm"),
                rx.button("Ordenar ahora", bg=primary, color="white"),
                spacing="4"
            ),
            bg=bg,
            padding="40px",
            width="50%"
        )
    )

# -------- GALLERY --------
def gallery():
    return rx.vstack(
        rx.heading("Visítanos hoy", size="7", color=primary),
        rx.hstack(
            rx.image(src="https://images.unsplash.com/photo-1495474472287-4d71bcdd2085", width="120px"),
            rx.image(src="https://images.unsplash.com/photo-1509042239860-f550ce710b93", width="120px"),
            rx.image(src="https://images.unsplash.com/photo-1511920170033-f8396924c348", width="120px"),
            rx.image(src="https://images.unsplash.com/photo-1442512595331-e89e73853f31", width="120px"),
            spacing="4",
            justify="center"
        ),
        spacing="5",
        padding="40px"
    )

# -------- FOOTER --------
def footer():
    return rx.hstack(
        rx.text("© 2026 Coffee Shop"),
        rx.spacer(),
        rx.text("Síguenos en redes"),
        padding="20px",
        bg=primary,
        color="white"
    )

# -------- PAGE --------
def index():
    return rx.box(
        navbar(),
        hero(),
        features(),
        why_us(),
        gallery(),
        footer()
    )

app = rx.App()
app.add_page(index)