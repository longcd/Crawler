import time
import random
import requests
from bs4 import BeautifulSoup

# 纽约市景点New York City
url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html#ATTRACTION_LIST'
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#ATTRACTION_LIST'.format(str(i)) for i in range(30, 1140, 30)]

headers = {
    'User-Agent': '',
    'Cookie': ''
}

def get_attractions(url):
    wb_data = requests.get(url)
    time.sleep(random.randint(0, 10))
    soup = BeautifulSoup(wb_data.text, 'lxml')
    titles = soup.select('div.listing_title > a[target="_blank"]')
    images = soup.select('img[width="180"]')
    categories = soup.select('div.attraction_element > div > div > div > div > div > div.p13n_reasoning_v2')

    for title, image, category in zip(titles, images, categories):
        data = {
            'title': title.get_text(),
            'image': image.get('src'),
            'category': [i for i in list(category.stripped_strings) if i != ',']
        }
        print(data)

get_attractions(url)
for url in urls:
    get_attractions(url)
