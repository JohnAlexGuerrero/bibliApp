from db.conexion import db
from models.enlace import Enlace

class EnlaceRepositorio:
    _database = db
    
    def __init__(self):
      self.collection = self._database["Enlaces"]
      
    def save(self, enlace: Enlace):
        print(enlace)