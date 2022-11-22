import requests
from bs4 import BeautifulSoup
import json

req = requests.get('https://www.filmweb.pl/film/Nietykalni-2011-583390')

soup = BeautifulSoup(req.text, 'html.parser')

films = soup.find('div', {'class': 'filmPosterSection__container page__text'})

opis = []

for film in films.find_all('div', {'class': 'filmPosterSection__plot clamped'}):
    span = film.find('span')

    opis.append((span.text.strip()))
 
print(opis)

with open('actual_forum.json', 'w', encoding='utf-8') as f:
    json.dump(opis, f, ensure_ascii=False)