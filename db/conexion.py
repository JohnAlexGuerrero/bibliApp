import pymongo

# Conectar a la base de datos
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["biblia_db"]
# collection = db["versos"]


# lista_de_versos = [
#     "Mi siervo Moisés ha muerto; ahora, pues, levántate y pasa el Jordán, tú y todo este pueblo"
# ]
# Insertar algunos documentos para el ejemplo
# collection.insert_many([
#     {"": "Ana", "edad": 25, "ciudad": "Madrid"},
#     {"nombre": "Luis", "edad": 30, "ciudad": "Barcelona"},
#     {"nombre": "Ana", "edad": 28, "ciudad": "Valencia"}
# ])

# 1. Buscar el primer documento sin filtro
# primer_documento = collection.find_one()
# print(f"Primer documento en la colección: {primer_documento}")

# 2. Buscar un documento que cumpla un criterio específico
# filtro_nombre = {"nombre": "Ana"}
# documento_encontrado = collection.find_one(filtro_nombre)
# print(f"Documento encontrado con el filtro 'nombre': {documento_encontrado}")

# 3. Usar `find_one()` con un filtro y una proyección
# Solo queremos el campo 'nombre' y 'ciudad', excluyendo el '_id'
# filtro_edad = {"edad": 30}
# proyeccion = {"_id": 0, "nombre": 1, "ciudad": 1} # 1 para incluir, 0 para excluir
# documento_proyectado = collection.find_one(filtro_edad, proyeccion)
# print(f"Documento proyectado: {documento_proyectado}")

# # 4. Cuando el documento no existe
# filtro_inexistente = {"nombre": "Pedro"}
# documento_inexistente = collection.find_one(filtro_inexistente)
# print(f"Documento inexistente (devuelve None): {documento_inexistente}")