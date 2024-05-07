# api Imgflip: https://imgflip.com/api 
#La librería request es una librería de Python que permite hacer peticiones HTTP
#El método get() envía una solicitud de datos a un servidor web . El objeto de respuesta que devuelve contiene varios tipos de datos, como el texto de la página web, el código de estado y el motivo de esa respuesta.

import requests
from PIL import Image
from io import BytesIO

Numimagen = 6 #Cambio el numero de imagen de la API que deseo imprimir


# 1. URL de destino
url = "https://api.imgflip.com/get_memes"
headers = {"Accept-Encoding": "gzip, deflate"}

# 2. Obtener response
response = requests.get(url, headers=headers)
data = response.json()

# 3. Verificar keys de data
print(data.keys())

# 4. Mirar estructura y consistencia de datos
print(len(data['data']['memes']))
print(data['data']['memes'][Numimagen])

#5. Obtener figura aleatoria
destino= data['data']['memes'][Numimagen]
response = requests.get(destino['url'])
img = Image.open(BytesIO(response.content))
img.save("DE_S1/imagen_meme.jpeg", "JPEG")
print('Proceso finalizado con exito')
