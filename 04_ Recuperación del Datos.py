# Conjunto de documentos ficticios
documentos = [
    "Este es el primer documento. Contiene información relevante.",
    "El segundo documento habla sobre el procesamiento de lenguaje natural.",
    "El tercer documento es un ejemplo de recuperación de datos.",
    "En el cuarto documento se menciona la inteligencia artificial.",
    "El último documento es sobre aprendizaje automático."
]

# Función para recuperar documentos relevantes
def recuperar_documentos(query, documentos):
    resultados = []
    for i, documento in enumerate(documentos):
        if query.lower() in documento.lower():
            resultados.append((i, documento))
    return resultados

# Consulta de ejemplo
consulta = "recuperación de datos"

# Recuperar documentos relevantes
resultados = recuperar_documentos(consulta, documentos)

if resultados:
    print(f"Documentos relevantes para la consulta '{consulta}':")
    for i, documento in resultados:
        print(f"Documento {i + 1}: {documento}")
else:
    print(f"No se encontraron documentos relevantes para la consulta '{consulta}'.")
