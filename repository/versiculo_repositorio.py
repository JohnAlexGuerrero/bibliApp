import pandas as pd
import os
from models.versiculo import Versiculo

CSV_FILE = 'data/versiculos.csv'

class VersiculoRepositorio:    
    def __init__(self):
        # Si el archivo no existe, creamos encabezados
        if not os.path.exists(CSV_FILE):
            df = pd.DataFrame(columns=["id", "book", "book_sort", "chapter","verse","title","text"])
            df.to_csv(CSV_FILE, index=False)
        
        # self._id__counter = self._df['id'].count()
        

    def _load_data(self):
        return pd.read_csv(CSV_FILE)
    
    def _save_data(self, df):
        df.to_csv(CSV_FILE, index=False)
    
    def save(self, verso: Versiculo):
        df = self._load_data()
        # Asignar un ID incremental
        next_id = 1 if df.empty else df["id"].max() + 1
        verso.id = next_id
        
        df = pd.concat([df, pd.DataFrame([vars(verso)], columns=df.columns)], ignore_index=True)
        self._save_data(df)
        
        return verso

    # def find_by_ref(reference: str):
        
