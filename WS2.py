#MAKED BY JASON

import requests
from bs4 import BeautifulSoup

# Hacer una solicitud a la página web
url = str(input("Ingresa el dominio de un sitio: "))
page = requests.get(url)

# Verificar si la solicitud fue exitosa
if page.status_code == 200:
    # Crear un objeto BeautifulSoup a partir del contenido de la página
    soup = BeautifulSoup(page.content, "html.parser")
    # Buscar y extraer información de la página
    title = soup.find("title").text
    headers = [header.text for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])]
    links = [link.get("href") for link in soup.find_all("a")]
    images = [image.get("src") for image in soup.find_all("img")]
    # Imprimir la información extraída
    print("Title:", title)
    print("Headers:", headers)
    print("Links:", links)
    print("Images:", images)
else:
    print("No se pudo acceder a la página")
