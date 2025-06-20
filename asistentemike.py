import streamlit as st
from PIL import Image
import os

robot_image_path = "robot_fullbody.png"

# Inicializa el estado de la aplicación
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": (
            "¡Hola! Soy **Mike**, tu asistente virtual. 🤖\n\n"
            "Estoy muy emocionado de que estés aquí. ¡Este curso puede marcar una gran diferencia en tu forma de enseñar! 💡\n\n"
            "Ahora dime... ¿Cuál es tu nombre?"
        )}
    ]
    st.session_state.etapa = "esperando_nombre"

# Mostrar imagen
col1, col2 = st.columns([1, 2])
with col1:
    if os.path.exists(robot_image_path):
        st.image(Image.open(robot_image_path), use_column_width=True)
    else:
        st.image("https://i.imgur.com/MT5J5Ch.png", use_column_width=True)
with col2:
    st.markdown("## 🤖 Chat con Mike")

# Mostrar historial del chat
for msg in st.session_state.messages:
    with st.chat_message("🤖 Mike" if msg["role"] == "assistant" else "🧑 Tú"):
        st.markdown(msg["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu respuesta aquí..."):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Responder según la etapa
    if st.session_state.etapa == "esperando_nombre":
        nombre = prompt.strip()
        respuesta = (
            f"Encantado de conocerte, {nombre}. 🎉\n\n"
            "Bienvenido al curso **IA para la educación con TensorFlow en Google Colab**. 🎓\n\n"
            "¿Por qué te interesó este curso?"
        )
        st.session_state.messages.append({"role": "assistant", "content": respuesta})
        st.session_state.etapa = "esperando_motivo"

    elif st.session_state.etapa == "esperando_motivo":
        motivo = prompt.strip()
        respuesta = (
            "¡Excelente! 🙌\n\n"
            "Ahora te invito a que conozcas el alcance, los objetivos y los contenidos del curso "
            "por parte de mi creador, **Luis Miguel Méndez**. 🚀\n\n"
            "**Disfruta este curso y te deseo el mayor de los éxitos.** 🎉"
        )
        st.session_state.messages.append({"role": "assistant", "content": respuesta})
        st.session_state.etapa = "finalizado"

    elif st.session_state.etapa == "finalizado":
        st.session_state.messages.append({
            "role": "assistant",
            "content": "La sesión ha terminado. Puedes recargar la página para comenzar de nuevo. 🔁"
        })
