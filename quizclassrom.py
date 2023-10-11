import requests
import certifi
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.f6od9yz.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.bilibili.tv/id/anime', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

animes = soup.select('.section__list__item')

for anime in animes:
    animes_title = anime.select_one('.bstar-video-card__title-text').text
    genre = anime.select_one('.bstar-video-card__desc--normal').text.split('-')[1].strip()
    img = anime.select_one('.bstar-video-card__cover-wrap > div > picture > source')
    print(animes_title, '/', genre, '/', img)
    data = {
        'title': animes_title,
        'genre': genre,
        'img': img
    }
    db.animes._insert_one(data)