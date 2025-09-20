import streamlit as st
import streamlit.components.v1 as components

from pages.versiculos import LIST_BOOKS, LIST_BOOKS_ABREVIATURES
from repository.versiculo_repositorio import VersiculoRepositorio

repository = VersiculoRepositorio()

st.write("Enlaces")

st.sidebar.selectbox("Temas", ["la creación", "el principio", "El árbol de la vida"])

tema = st.text_input("",placeholder="Añade un tema")

libro_seleccionado = st.sidebar.selectbox("Libro", LIST_BOOKS)

idx_libro_seleccionado = LIST_BOOKS.index(libro_seleccionado)

abreviatura_libro = LIST_BOOKS_ABREVIATURES[idx_libro_seleccionado]

capitulos = repository.count_chapters(abreviatura_libro) + 1

capitulo_seleccionado = st.sidebar.selectbox("Capítulo", [i for i in range(1, capitulos)])

versiculos = repository.filter_by_name_book(f'{abreviatura_libro}. {capitulo_seleccionado}')

versos_seleccionados = st.sidebar.multiselect("versiculos", [v['verse'] for v in versiculos])

versiculos_arr = []

for v in versos_seleccionados:
    verso = repository.find_one(v)
    versiculos_arr.append(verso)
    
texto = st.text_area("Nota", placeholder="¿Qué piensas?", max_chars=300,)

for verso in versiculos_arr:
    components.html(f"""
    <div class="p-4">
        <p class="text-lg font-serif text-gray-800 mb-2">{verso['text']}</p>
        <p class="text-sm text-gray-500">{verso['verse']}</p>
    </div>
    """)
    
