import requests
from bs4 import BeautifulSoup

# URL de ejemplo
url = "https://es.wikipedia.org/wiki/Python"

# Obtener el contenido de la web
response = requests.get(url)
html_content = response.text

# Parsear HTML y extraer solo el texto
soup = BeautifulSoup(html_content, "html.parser")
text = soup.get_text(separator="\n")  # separator="\n" para mantener saltos de línea

# Limpiar texto extra (opcional)
lines = [line.strip() for line in text.splitlines() if line.strip()]
clean_text = "\n".join(lines)

print(clean_text[:1000])  # Mostrar solo los primeros 1000 caracteres
