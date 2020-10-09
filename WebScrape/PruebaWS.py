from requests import get
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
print(response.text[:1000])

#------------------
from bs4 import BeautifulSoup
html_soup = BeautifulSoup(response.text, 'html.parser')

contenedores_peliculas = html_soup.find_all('div', class_ = 'lister-item mode-advanced')
print(type(contenedores_peliculas))
print(len(contenedores_peliculas))

print("----Separador----")
print(contenedores_peliculas[0])

first_movie = contenedores_peliculas[0]

print('---------------div---------------')
print(first_movie.div)


print('---------------a---------------')
print(first_movie.a)

print('---------------h3---------------')
print(first_movie.h3)

print('---------------h3 dentro a---------------')
print(first_movie.h3.a)

print('---------------nombre pelicula---------------')
primer_nombre=first_movie.h3.a.text
print(primer_nombre)

print('---------------año---------------')
primer_anio= first_movie.h3.find('span', class_= 'lister-item-year text-muted unbold')
print(primer_anio.text)

print('---------------calificacion---------------')
calificacion = first_movie.strong.text
print(calificacion)

print('---------------metascore---------------')
metascore = first_movie.find('span', class_='metascore favorable')
metascore = int(metascore.text)
print(metascore)

print('---------------votos---------------')
votes = first_movie.find('span', attrs = {'name':'nv'})
print(votes)
print(votes['data-value'])
votes = int(votes['data-value'])
print(votes)


# listas donde se guardaran los datos extraidos
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

#Extrayendo cada contenedor de forma indivudual
for container in contenedores_peliculas:
    #si la pelicula tiene metascore, entonces se extrae
    if container.find('div', class_='ratings-metascore') is not None:
        #Nombre
        name = container.h3.a.text
        names.append(name)
        #Año
        year = container.h3.find('span', class_= 'lister-item-year text-muted unbold').text
        years.append(year)
        # IMDB ratings
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)
        #metascore
        m_score = container.find('span', class_='metascore').text
        metascores.append(int(m_score))
        #num votos
        vote = container.find('span', attrs = {'name': 'nv'})['data-value']
        votes.append(int(vote))
        
        
print('---------------names---------------')
print(names)


print('---------------years---------------')
print(years)


print('---------------imdb_ratings---------------')
print(imdb_ratings)


print('---------------metascores---------------')
print(metascores)


print('---------------votes---------------')
print(votes)


print('---------------Usando Pandas---------------')
import pandas as pd
test_df = pd.DataFrame({'movie': names,
'year': years,
'imdb': imdb_ratings,
'metascore': metascores,
'votes': votes
})
print(test_df.info())

print(test_df)
        

#----------------------------------------Script multiples paginas

pages = [str(i) for i in range(1,5)]
years_url = [str(i) for i in range(2000,2018)]

#controlando el tiempo de las peticiones

from time import sleep
from random import randint

for _ in range(0,5):
    print('Blah')
    sleep(randint(1,4))
    
    
        
        
        

