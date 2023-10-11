import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('mongodb+srv://yasmin:yasmin@cluster0.yrjugsf.mongodb.net/?retryWrites=true&w=majority')
db = client.billboard

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

url = 'https://www.billboard.com/charts/hot-100/'

data = requests.get(url, headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

billboard = soup.select('.chart-results-list > .o-chart-results-list-row-container')

for artist in billboard:
    rank = artist.select_one('.o-chart-results-list__item > span').text.strip()
    song = artist.select_one('#title-of-a-story').text.strip()
    artist = artist.select_one('.o-chart-results-list__item > span:nth-child(2)').text.strip()
    data = {
        'rank':rank,
        'artist':artist,
        'song':song,
    }
    db.top.insert_one(data)