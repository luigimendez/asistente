import streamlit as st
from PIL import Image
import os

# Imagen local o por defecto
robot_image_path = "robot_fullbody.png"
if not os.path.exists(robot_image_path):
    robot_image_path = "https://i.imgur.com/MT5J5Ch.png"

# Inicializar variables de sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.etapa = 0  # 0: pedir nombre, 1: pedir motivo, 2: despedida
    bienvenida = (
        "¡Hola! Soy **Mike**, tu asistente virtual. 🤖\n\n"
        "Estoy muy emocionado de que estés aquí. ¡Este curso puede marcar una gran diferencia en tu forma de enseñar! 💡\n\n"
        "Ahora dime... ¿Cuál es tu nombre?"
    )
    st.session_state.messages.append(("🤖 Mike", bienvenida))

# Entrada del usuario (primero procesamos)
user_input = st.chat_input("Escribe tu respuesta aquí...")

if user_input:
    st.session_state.messages.append(("🧑 Tú", user_input))

    if st.session_state.etapa == 0:
        nombre = user_input.strip()
        st.session_state.messages.append(("🤖 Mike",
            f"Encantado de conocerte, {nombre}. 🎉\n\n"
            "Bienvenido al curso **IA para la educación con TensorFlow en Google Colab**. 🎓\n\n"
            "¿Por qué te interesó este curso?"
        ))
        st.session_state.etapa = 1

    elif st.session_state.etapa == 1:
        motivo = user_input.strip()
        st.session_state.messages.append(("🤖 Mike",
            "¡Excelente! 🙌\n\n"
            "Ahora te invito a que conozcas el alcance, los objetivos y los contenidos del curso "
            "por parte de mi creador, **Luis Miguel Méndez**. 🚀\n\n"
            "**Disfruta este curso y te deseo el mayor de los éxitos.** 🎉"
        ))
        st.session_state.etapa = 2

    else:
        st.session_state.messages.append(("🤖 Mike", "La sesión ha terminado. Puedes recargar para iniciar de nuevo 🔁"))

# Ahora mostramos todo el historial ya actualizado
col1, col2 = st.columns([1, 2])
with col1:
    st.image(robot_image_path, use_container_width=True)
with col2:
    st.markdown("## 🤖 Chat con Mike")

for autor, mensaje in st.session_state.messages:
    with st.chat_message(autor):
        st.markdown(mensaje)
