class Versiculo:
    def __init__(self, id, verse, text):
        self.id = id
        self.verse = verse
        self.text = text
    
    def __dir__(self):
        return {"versiculo": self.verse, "texto": self.text}
