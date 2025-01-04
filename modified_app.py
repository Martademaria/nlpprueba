import streamlit as st


# Aplicar fondo beige a toda la página mediante CSS
st.markdown("""
    <style>
        body {
            background-color: #F5F5DC;  # Código hexadecimal para un tono beige
        }
    </style>
    """, unsafe_allow_html=True)


# Función para mostrar la información del restaurante
def show_restaurant_info():
    
    
    # Mostrar imágenes del restaurante (asegúrate de que las imágenes estén en el directorio adecuado)
    st.image("labellavita2.png", use_column_width=True)
    
    # Mostrar la segunda imagen debajo de la primera
    st.image("aboutus3.png", use_column_width=True)
    st.image("aa.png", use_column_width=True)
    st.image("loc.png", use_column_width=True)

    # Descripción del restaurante
    st.header("Sobre Nosotros")
    st.markdown("""
    Nuestro restaurante se especializa en cocina de autor, fusionando los sabores tradicionales con técnicas modernas.  
    Ofrecemos una experiencia gastronómica única, con un ambiente acogedor y un servicio excepcional.
    """)
    
    # Mostrar más detalles sobre el restaurante
    st.header("Información del Restaurante")
    st.markdown("""
    - **Ubicación**: Calle Ficticia 123, Ciudad XYZ  
    - **Horario**: Lunes a Domingo de 12:00 PM a 10:00 PM  
    - **Contacto**: (123) 456-7890  
    - **Especialidades**: Paella, Tacos de Mariscos, Postres Caseros
    """)

# Función para mostrar el chatbot
def show_chatbot():
    st.title("Asistente Virtual")
    
    # Explicar brevemente cómo interactuar con el chatbot
    st.markdown("""
    Nuestro asistente está aquí para ayudarte con las reservas, recomendaciones de platos y más.  
    Solo escribe tu consulta y nuestro chatbot te asistirá.
    """)

    # Implementar el chatbot aquí (como en el ejemplo anterior)
    # En este caso, usamos el mismo sistema de RAG o cualquier otro modelo generativo
    user_query = st.text_input("¿Cómo puedo ayudarte hoy?")
    
    if user_query:
        assistant_response = generate_response(user_query)
        st.write(f"Assistant: {assistant_response}")

# Función para generar una respuesta del chatbot (como el ejemplo anterior)
def generate_response(query):
    # Aquí implementas la lógica de RAG o cualquier otro modelo
    # Este es un ejemplo básico con OpenAI (ajusta según sea necesario)
    prompt = f"Usuario pregunta: {query}\n\nResponde como si fueras un asistente de restaurante, utilizando los siguientes datos:\n"
    
    # Recoge datos relevantes para incluir en la respuesta (por ejemplo, menú, reservas, etc.)
    relevant_data = retrieve_data(query)
    prompt += f"Datos relevantes: {relevant_data}\n\nRespuesta:"
    
    # Usar el modelo de OpenAI para generar la respuesta
    response = openai.Completion.create(
        engine="text-davinci-003",  # Puedes elegir otro modelo si prefieres
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()

# Función para recuperar información relevante de la base de datos
def retrieve_data(query):
    # Simulación de recuperación de datos (esto puede integrarse con tu base de datos real)
    if "menú" in query.lower():
        return get_current_menu()  # Obtén el menú actual de tu base de datos
    elif "reserva" in query.lower():
        return get_reservation_details()  # Información sobre reservas
    elif "recomendación" in query.lower():
        return get_customer_preferences()  # Recomendaciones basadas en preferencias
    elif "reseña" in query.lower():
        return get_reviews()  # Reseñas de los platos
    return "Lo siento, no pude recuperar información relevante."

# Función principal que muestra la información y el chatbot
def main():
    # Mostrar la información del restaurante
    show_restaurant_info()

    # Añadir un separador para dar espacio
    st.write("---")

    # Mostrar el chatbot después de la información
    show_chatbot()

# Ejecutar la función principal para mostrar la interfaz
if __name__ == "__main__":
    main()
