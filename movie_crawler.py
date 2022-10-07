import os
from urllib.parse import urlparse
from urllib.request import urlopen
import re
import django
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pair_pjt.settings')
django.setup()

from reviews.models import Movie

url = 'https://movie.naver.com/movie/running/current.naver'

req = urlopen(url)
byte_data = req.read()

text_data = byte_data.decode("utf-8")

html = BeautifulSoup(text_data, 'html.parser')

movie_list = html.select('div[class="lst_wrap"] > ul[class="lst_detail_t1"] > li', limit=30)

base_url = 'https://movie.naver.com'
urls = []
for li in movie_list:
    a_tag = li.select_one('div[class="thumb"] > a')
    urls.append(base_url + a_tag.get('href'))



def get_movie_data(url):

    request = urlopen(url)
    byte_data = request.read()
    text_data = byte_data.decode("utf-8")
    html = BeautifulSoup(text_data, 'html.parser')
    soup = html.find("div", class_="poster")

    title = html.select_one('div[class="mv_info"] > h3[class="h_movie"] > a').string
    summary = html.select_one('div[class="story_area"] > p').text
    img = soup.find('img')["src"]
    context = {
        'title':title,
        'summary':summary,
        'img':img,
    }

    return context




def add_data():
    result =[]

    for url in urls:
        tmp = get_movie_data(url)
        result.append(tmp)


    for item in result:
        Movie(title=item['title'],
              img=item['img'],
              summary=item['summary'],).save()

    return result

add_data()