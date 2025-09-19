import streamlit as st
import streamlit.components.v1 as components

from repository.versiculo_repositorio import VersiculoRepositorio

repository = VersiculoRepositorio()

LIST_BOOKS = [
    "Génesis", "Éxodo", "Levítico", "Números", "Deuteronomio",
    "Josué", "Jueces", "Rut", "1 Samuel", "2 Samuel", "1 Reyes", "2 Reyes", "1 Crónicas", "2 Crónicas", "Esdras", "Nehemías", "Ester",
    "Job", "Salmos", "Proverbios", "Eclesiastés", "Cantares",
    "Isaías", "Jeremías", "Lamentaciones", "Ezequiel", "Daniel", "Oseas", "Joel", "Amós", "Abdías", "Jonás", "Miqueas", "Nahún", "Habacuc", "Sofonías", "Ageo", "Zacarías", "Malaquías", 
    "Mateo", "Marcos", "Lucas", "Juan","Hechos","Romanos","1 Corintios","2 Corintios","Galátas","Efesios", "Filipenses","Colosenses","1 Tesalonicenses","2 Tesalonicenses","1 Timoteo", "2 Timoteo", "Tito","Filemón","Hebreos","Santiago","1 Pedro", "2 Pedro", "1 Juan", "2 Juan","3 Juan","Judas","Apocalipsis"
]

LIST_BOOKS_ABREVIATURES = [
    "Gen", "Ex", "Lv", "Nm", "Dt",
    "Jos", "Jue", "Rt", "1 S", "2 S", "1 R", "2 R", "1 Cr", "2 Cr", "Esd", "Neh", "Est",
    "Job", "Sal", "Pr", "Ec", "Cnt",
    "Is", "Jer", "Lm", "Ez", "Dn", "Os", "Jl", "Am", "Abd", "Jon", "Mi", "Nah", "Hab", "Sof", "Ageo", "Zacarías", "Malaquías", 
    "Mateo", "Marcos", "Lc", "Juan","Hechos","Romanos","1 Corintios","2 Corintios","Galátas","Efesios", "Filipenses","Colosenses","1 Tesalonicenses","2 Tesalonicenses","1 Timoteo", "2 Timoteo", "Tito","Filemón","Hebreos","Santiago","1 Pedro", "2 Pedro", "1 Juan", "2 Juan","3 Juan","Judas","Apocalipsis"
]

st.write("Versiculos")

st.write("Filtrar por:")

book_selected = st.selectbox("Libro", LIST_BOOKS)


index_abreviature = LIST_BOOKS.index(book_selected)

total_chapters = repository.count_chapters(LIST_BOOKS_ABREVIATURES[index_abreviature])

chapter_selected = st.selectbox("Capítulo", [i for i in range(1, (total_chapters + 1))])

versiculos = repository.filter_by_name_book(f"{LIST_BOOKS_ABREVIATURES[index_abreviature]}. {chapter_selected}: ")

for v in versiculos:
    components.html(f"""
    <div class="p-4">
        <p class="text-lg font-serif text-gray-800 mb-2">{v['text']}</p>
        <p class="text-sm text-gray-500">{v['verse']}</p>
    </div>
    """)