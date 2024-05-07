#pip install spotipy
#pip install wheel
#pip install psycopg2

#Librerias
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import numpy as np

#Ingreso a la Web de Developers de Spotify para obtener client_id Y client_secret 
# https://developer.spotify.com/

#Obtengo los datos de usuario y contraseña de archivo TXT de modo de no mostrar contraseñas y datos sensibles
with open("C:/Users/Sofia Medici/Desktop/DATA - Programas/Py Notebooks/DE_S5_Entregable/client_secret_spotify.txt",'r') as f:
    password= f.read()

#Autenticar
client_id= 'a25133e8be74459883f8c73541945ab9'
client_secret = password

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



print('Consulta_1------------------------------------------------------------------------------------------------------------------------------------------')
results = sp.search(q='Los Fundamentalistas del Aire Acondicionado', type='artist', limit=10)
artist_id = results['artists']['items'][0]['id']
print(artist_id)

albums = sp.artist_albums(artist_id, album_type='album')

for album in albums['items']:
  print(album['name'])


print('Consulta_2------------------------------------------------------------------------------------------------------------------------------------------')
results = sp.search(q='year:2023', type='track', limit=10)
data = {'Id': [],'Artista': [], 'Cancion': [],'Duracion_ms': [], 'Genero': [],'Album': [], 'Album_img': [], 'Total_canciones_album': [], 'Popularidad': [], 'fecha_lanzamiento': []}
for track in results['tracks']['items']:
    id = track['id']
    artist_name = track['artists'][0]['name']
    artist_id = track['artists'][0]['id']
    track_name = track['name']
    duration_ms = track['duration_ms']
    track_id = track['id']
    album_group = track['album']['name']
    album_img = track['album']['images'][0]['url'] #imagen de album
    album_cont = track['album']['total_tracks']
    track_genre = sp.artist(artist_id)['genres']
    track_popularity = track['popularity']
    track_year = track['album']['release_date']
    #Quitar las comillas 
    track_name = track_name.replace("'", "")
    album_group = album_group.replace("'", "")
    #Separar el género por coma
    track_genre = ', '.join(track_genre)

    data['Id'].append(id)
    data['Artista'].append(artist_name)
    data['Cancion'].append(track_name)
    data['Duracion_ms'].append(duration_ms)
    data['Album'].append(album_group)
    data['Album_img'].append(album_img)
    data['Total_canciones_album'].append(album_cont)
    data['Genero'].append(track_genre)
    data['Popularidad'].append(track_popularity)
    data['fecha_lanzamiento'].append(track_year)


df = pd.DataFrame(data)
#Evitar que haya canciones duplicadas
df.drop_duplicates(subset=['Artista', 'Cancion','Album'], keep='first', inplace=True)
#Reemplazar valores nulos o vacios en el campo Género por Desconocido
df['Genero'].fillna('Desconocido', inplace=True)
df.loc[df['Genero'] == '', 'Genero'] = 'Desconocido'
#Evitar que se cargue una canción con duración 0 ms
df = df[df['Duracion_ms'] != 0]
#Verificar que la fecha se muestre en formato fecha 
df['fecha_lanzamiento'] = pd.to_datetime(df['fecha_lanzamiento'], format='%Y-%m-%d')
print(df)

print('FIN------------------------------------------------------------------------------------------------------------------------------------------')





