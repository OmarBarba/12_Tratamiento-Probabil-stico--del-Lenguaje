import re

# Texto de ejemplo
texto = "El evento se llevará a cabo el 25 de noviembre de 2023 en la ciudad de Nueva York."

# Expresiones regulares para extraer fechas y lugares
expresion_fecha = r'(\d{1,2} de [a-zA-Z]+ de \d{4})'
expresion_lugar = r'en la ciudad de ([\w\s]+)\.'

# Extraer fechas
fechas_encontradas = re.findall(expresion_fecha, texto)
if fechas_encontradas:
    print("Fechas encontradas:")
    for fecha in fechas_encontradas:
        print(fecha)

# Extraer lugar
lugar_encontrado = re.search(expresion_lugar, texto)
if lugar_encontrado:
    print("Lugar encontrado:", lugar_encontrado.group(1))

