from datetime import datetime
from models.versiculo import Versiculo

class Enlace:
    def __init__(self, versiculo: Versiculo):
        self.tema = None
        self.texto = None
        self.versiculo = versiculo
        # self.image = None
        self.date_time = datetime.now()