import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# Start coding
# tag.text
# tag['attribute']

movies = soup.select('ul.ipc-metadata-list > li')

# soup.select('tag_name[attribute="value"]')


# for movie in movies:
#     movie_tittle = movie.select_one('.titleColumn > a').text
#     print(movie_tittle)

for movie in movies:
    movie_title = movie.select_one('.ipc-title > a > h3').text
    # movie_title = movie.select_one('.ipc-metadata-list-summar-item_c .ipc-title_text').text
    year = movie.select('.cli-title-metadata > span')[0].text
    rating = movie.select_one('.cli-ratings-container > span').text
    print(movie_title, '/', year, '/', rating)