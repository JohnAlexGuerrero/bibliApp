from typing import List
import pandas as pd
import os
from models.versiculo import Versiculo
from db.conexion import db

CSV_FILE = 'data/versiculos.csv'


class VersiculoRepositorio:
    _database = db
        
    def __init__(self):
        self.collection = self._database['versos']        

    # def _load_data(self):
    #     return pd.read_csv(CSV_FILE)
    
    # def _save_data(self, df):
    #     df.to_csv(CSV_FILE, index=False)
    
    def save(self, verso: Versiculo):
        insert_data = {"verse":verso.verse, "text": verso.text}
        verso = self.collection.insert_one(insert_data)
        # # Asignar un ID incremental
        # next_id = 1 if df.empty else df["id"].max() + 1
        # verso.id = next_id
        
        # df = pd.concat([df, pd.DataFrame([vars(verso)], columns=df.columns)], ignore_index=True)
        # self._save_data(df)
        
        return verso
    
    def get_all_verses(self) -> List:
        return self.collection.find()

    def filter_by_name_book(self, name: str) -> List:
        query = {"verse": {"$regex":f'{name}'}}
        return self.collection.find(query)
    
    def find_one(self, name: str) -> Versiculo:
        query = {"verse": f'{name}'}
        return self.collection.find_one(query)
    
    def count_chapters(self, name: str) -> int: 
        chapters = []
        
        for resultado in self.filter_by_name_book(name): 
            # if resultado['verse'].find(name) == 0:
            chapters.append(resultado['verse'].split(':')[0])
        return len(set(chapters))
