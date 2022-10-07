import os
from urllib.parse import urlparse

import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE','pair_pjt.settings')
django.setup()

from reviews.models import Movie

def get_movie_data():
    result = []
    url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20221006'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    print(soup)

    web_page_link_root = 'https://movie.naver.com/'
    list_items = soup.find_all('div')

    for item in list_items:

        title = item.find('meta[property="og:title"]')['content']
        img = item.find('meta[property="og:image"]')['content']
        description = item.find('meta[property="og:description"]')['content']
        running_time = item.find('meta[property="og:title"]')['content']

        item_obj ={
            'title':title,
            'img':img,
            'description':description,
            'running_time':running_time,

        }

        print(item_obj)
        result.append(item_obj)

    return result

if __name__ == '__main__':
    get_movie_data()

def add_data(data):

    db_object=[]
    for item in data:
        db_object.append(item)
    db_object.reverse()

    for item in db_object:
        print("테스트 성공")
        Movie(title=item['title'],
              img=item['img'],
              summary=item['description'],
              running_time=item['running_time']).save()

    return db_object
