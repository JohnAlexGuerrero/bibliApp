import streamlit as st
from Dto.versiculoDTO import VersiculoDTO, CrearVersiculoDTO
from repository.versiculo_repositorio import VersiculoRepositorio
from service.versiculo_service import VersiculoService

# iniciar capas
repo = VersiculoRepositorio()
service = VersiculoService(repository=repo)

st.title("Formulario")

with st.form("my_form"):
    book = st.text_input("Libro: ")
    book_sort = st.text_input("Abreviatura del libro:")
    chapter = st.number_input("Capítulo:", min_value=1, step=1)
    verse = st.number_input("Versiculo:", min_value=1, step=1)
    event = st.text_input("Título del Evento:")
    text = st.text_area("Texto:")
    
    summited = st.form_submit_button("Guardar")
    
    if summited:
        try:
            dto = CrearVersiculoDTO(book=book, book_sort=book_sort, chapter=chapter, verse=verse, event=event, text=text)
            versiculo_dto = service.registrar_versiculo(dto=dto)
            st.success(f"El Versiculo {versiculo_dto.__str__()} fué guardado con éxito.")
        except ValueError as e:
            st.error(f"Error: {e}")
    
