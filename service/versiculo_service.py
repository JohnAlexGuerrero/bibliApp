from repository.versiculo_repositorio import VersiculoRepositorio
from Dto.versiculoDTO import CrearVersiculoDTO, VersiculoDTO
from models.versiculo import Versiculo

class VersiculoService:
    def __init__(self, repository: VersiculoRepositorio):
        self.repository = repository
    
    def registrar_versiculo(self, dto: CrearVersiculoDTO) -> VersiculoDTO:
        # validar si el versiculo existe
        # if self.repository
        
        verso = Versiculo(
            id=None,
            book=dto.book,
            book_sort=dto.book_sort,
            chapter=dto.chapter,
            verse=dto.verse,
            title=dto.event,
            text=dto.text
        )
        
        verso_guardado = self.repository.save(verso=verso)
        return VersiculoDTO(
            book_sort=verso_guardado.book_sort, 
            chapter=verso_guardado.chapter, 
            verse=verso_guardado.verse, 
            text=verso_guardado.text
        )
    