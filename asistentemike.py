import streamlit as st
from PIL import Image

# Cargar imagen del asistente
robot_image_path = "robot_fullbody.png"

# Mensaje inicial
mensaje_bienvenida = (
    "¡Hola! Soy **Mike**, tu asistente virtual. 🤖\n\n"
    "Estoy muy emocionado de que estés aquí. ¡Este curso puede marcar una gran diferencia en tu forma de enseñar! 💡\n\n"
    "Ahora dime... ¿Cuál es tu nombre?"
)

# Inicializa historial en sesión
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [("🤖 Mike", mensaje_bienvenida)]

# Mostrar imagen y título
col1, col2 = st.columns([1, 2])
with col1:
    st.image(Image.open(robot_image_path), use_column_width=True)
with col2:
    st.markdown("## 🤖 Chat con Mike")

# Mostrar historial del chat
for user, msg in st.session_state.chat_history:
    with st.chat_message(name=user):
        st.markdown(msg)

# Entrada del usuario
user_input = st.chat_input("Escribe tu respuesta aquí...")

if user_input:
    st.session_state.chat_history.append(("🧑 Tú", user_input))

    # Respuestas automáticas según la etapa
    history_len = len(st.session_state.chat_history)

    if history_len == 2:
        nombre = user_input.strip()
        respuesta = (
            f"Encantado de conocerte, {nombre}. 🎉\n\n"
            "Bienvenido al curso **IA para la educación con TensorFlow en Google Colab**. 🎓\n\n"
            "¿Por qué te interesó este curso?"
        )
        st.session_state.chat_history.append(("🤖 Mike", respuesta))

    elif history_len == 4:
        respuesta = (
            "¡Excelente! 🙌\n\n"
            "Ahora te invito a que conozcas el alcance, los objetivos y los contenidos del curso "
            "por parte de mi creador, **Luis Miguel Méndez**. 🚀\n\n"
            "**Disfruta este curso y te deseo el mayor de los éxitos.** 🎉"
        )
        st.session_state.chat_history.append(("🤖 Mike", respuesta))
    else:
        st.session_state.chat_history.append(("🤖 Mike", "La sesión ha terminado. Puedes reiniciar para comenzar de nuevo."))