import streamlit as st
from PIL import Image
import os

robot_image_path = "robot_fullbody.png"

mensaje_bienvenida = (
    "¡Hola! Soy **Mike**, tu asistente virtual. 🤖\n\n"
    "Estoy muy emocionado de que estés aquí. ¡Este curso puede marcar una gran diferencia en tu forma de enseñar! 💡\n\n"
    "Ahora dime... ¿Cuál es tu nombre?"
)

# Inicializa variables de estado
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [("🤖 Mike", mensaje_bienvenida)]
    st.session_state.etapa = 1  # Etapa 1 = pedir nombre

# Interfaz
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists(robot_image_path):
        st.image(Image.open(robot_image_path), use_column_width=True)
    else:
        st.image("https://i.imgur.com/MT5J5Ch.png", use_column_width=True)
with col2:
    st.markdown("## 🤖 Chat con Mike")

# Mostrar historial del chat
for autor, mensaje in st.session_state.chat_history:
    with st.chat_message(name=autor):
        st.markdown(mensaje)

# Entrada del usuario
user_input = st.chat_input("Escribe tu respuesta aquí...")

if user_input:
    # Mostrar entrada del usuario
    st.session_state.chat_history.append(("🧑 Tú", user_input))

    if st.session_state.etapa == 1:
        nombre = user_input.strip()
        respuesta = (
            f"Encantado de conocerte, {nombre}. 🎉\n\n"
            "Bienvenido al curso **IA para la educación con TensorFlow en Google Colab**. 🎓\n\n"
            "¿Por qué te interesó este curso?"
        )
        st.session_state.chat_history.append(("🤖 Mike", respuesta))
        st.session_state.etapa = 2

    elif st.session_state.etapa == 2:
        motivo = user_input.strip()
        respuesta = (
            "¡Excelente! 🙌\n\n"
            "Ahora te invito a que conozcas el alcance, los objetivos y los contenidos del curso "
            "por parte de mi creador, **Luis Miguel Méndez**. 🚀\n\n"
            "**Disfruta este curso y te deseo el mayor de los éxitos.** 🎉"
        )
        st.session_state.chat_history.append(("🤖 Mike", respuesta))
        st.session_state.etapa = 3

    else:
        st.session_state.chat_history.append(("🤖 Mike", "La sesión ha terminado. Puedes reiniciar la app si deseas comenzar de nuevo."))
