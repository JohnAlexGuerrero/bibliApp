class VersiculoDTO:
  def __init__(self, book_sort, chapter, verse, text):
    self.book_sort = book_sort
    self.chapter = chapter
    self.verse = verse
    self.text = text
    
  def __str__(self):
    return f"{self.book_sort}. {self.chapter}: {self.verse} - {self.text}"
      
class CrearVersiculoDTO:
  def __init__(self, book, book_sort, chapter, verse, event, text):
    self.book = book
    self.book_sort = book_sort
    self.chapter = chapter
    self.verse = verse
    self.event = event
    self.text = text