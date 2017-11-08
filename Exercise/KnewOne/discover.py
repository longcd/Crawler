import time
import requests
from bs4 import BeautifulSoup

url = 'https://knewone.com/discover?page='

def get_page(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    images = soup.select('header.cover > a > img')
    titles = soup.select('section.content > h4.title > a')
    links = soup.select('header.cover > a')

    for image, title, link in zip(images, titles, links):
        data = {
            'image': image.get('src'),
            'title': title.get_text(),
            'link': link.get('href')
        }
        print(data)

def get_more_pages(start, end):
    for one in range(start, end):
        get_page(url+str(one))
        time.sleep(2)
    
get_more_pages(1, 10)
