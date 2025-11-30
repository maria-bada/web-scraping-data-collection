import requests
from bs4 import BeautifulSoup
import csv

# Definir url
url = "http://quotes.toscrape.com"
# Solicitar acceso
response = requests.get(url)

 # Verificar si la solicitud es válida
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")# Parsear el contenido HTML de la página
    quotes = soup.find_all(class_="quote") # Encontrar todas las citas en la página
    # Crear una lista vacía para almacenar los datos extraídos
    data = []

    # Recorrer todas las citas
    for quote in quotes:
        text = quote.find(class_="text").get_text()   # Extraer el texto de las citas
        author = quote.find(class_="author").get_text()  # Extraer los autores        
        tags = quote.find_all(class_="tag") # Extraer las etiquetas asociadas a las citas
        tag_list = [tag.get_text() for tag in tags]  # Convertir los elementos en texto

        # Agregar la información a la lista de datos
        data.append({
            "cita": text,
            "autor": author,
            "etiquetas": ", ".join(tag_list)
        })

    # Definir el nombre del archivo csv donde se guardarán los datos
    output_file = "citas.csv"

    # Guardar los datos 
    with open(output_file, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["cita", "autor", "etiquetas"] # Definir las columnas
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader() # Escribir la cabecera 
        writer.writerows(data) # Escribir las filas 

   
    print(f"Datos guardados en '{output_file}'.")
else:
    # Mostrar un mensaje de error si la solicitud falla
    print(f"Error en la solicitud: {response.status_code}")

