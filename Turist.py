import os
import streamlit as st
from openai import OpenAI

# Inserta tu API KEY de OpenAI aquí
openai_api_key = "AQUÍ_INSERTA_TU_API_KEY_PERSONAL"

# Instanciar el cliente de OpenAI con tu API KEY personal
client = OpenAI(api_key=openai_api_key)

# Define la función para llamar al modelo de OpenAI
def call_openai_model(prompt):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            model="gpt-3.5-turbo",
        )
        # Accede al contenido del mensaje de completado del chat
        return response.choices[0].message["content"]
    except Exception as e:
        st.error(f"Error al obtener la descripción del tour: {str(e)}")

# Define la función principal para la interfaz de usuario
def main():
    # Configuración de la página
    st.set_page_config(page_title="ExploreMedellín", page_icon=":earth_americas:")

    # Título y descripción de la aplicación
    st.title("Bienvenido a ExploreMedellín")
    st.write("Encuentra experiencias auténticas y emocionantes en Medellín")

    # Barra de navegación
    nav_option = st.sidebar.radio("Navegación", ["Inicio", "Explorar", "Perfil", "Ayuda"])

    # Página de inicio
    if nav_option == "Inicio":
        st.write("¡Bienvenido a ExploreMedellín! Encuentra experiencias únicas y auténticas en Medellín.")

    # Página de exploración de experiencias
    elif nav_option == "Explorar":
        st.subheader("Explorar Experiencias")
        search_query = st.text_input("Buscar experiencias")
        location_filter = st.selectbox("Filtrar por ubicación", ["Todas", "Centro", "Poblado", "Envigado", "Laureles"])
        category_filter = st.multiselect("Filtrar por categoría", ["Aventura", "Cultura", "Gastronomía", "Naturaleza"])

        # Botón para generar el tour con OpenAI
        if st.button("Crear Tour"):
            prompt = f"Crear un tour en Medellín que incluya {search_query} y tenga una duración de un día."
            tour_description = call_openai_model(prompt)
            if tour_description:
                st.markdown(tour_description)

    # Página de perfil de usuario
    elif nav_option == "Perfil":
        st.subheader("Perfil de Usuario")
        username = st.text_input("Nombre de Usuario")
        email = st.text_input("Correo Electrónico")
        password = st.text_input("Contraseña", type="password")

        # Aquí agregaríamos la lógica para mostrar la información del perfil del usuario y las experiencias reservadas

    # Página de ayuda y soporte
    elif nav_option == "Ayuda":
        st.subheader("Ayuda y Soporte")
        st.write("¿Necesitas ayuda? ¡Estamos aquí para ayudarte!")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
