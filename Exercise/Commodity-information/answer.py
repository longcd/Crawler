from bs4 import BeautifulSoup

path = './homework-required/index.html'
with open(path, 'r') as wb_data: # 使用open函数打开本地文件
    soup = BeautifulSoup(wb_data, 'lxml') # 解析网页内容
    # print(soup)

    images = soup.select('div.col-sm-4 > div.thumbnail > img')
    titles = soup.select('div.col-sm-4 > div.thumbnail > div.caption > h4 > a') 
    prices = soup.select('div.col-sm-4 > div.thumbnail > div.caption > h4.pull-right') 
    descriptions = soup.select('div.col-sm-4 > div.thumbnail > div.caption > p')
    stars = soup.select('div.col-sm-4 > div.thumbnail > div.ratings > p:nth-of-type(2)')
    reviews = soup.select('div.col-sm-4 > div.thumbnail > div.ratings > p.pull-right')
    # print(images, titles, prices, descriptions, stars, reviews)

info = []
for image, title, price, description, star, review in zip(images, titles, prices, descriptions, stars, reviews):
    data = {
        'image': image.get('src'),
        'title': title.get_text(),
        'price': price.get_text(),
        'description': description.get_text(),
        'star': len(star.find_all('span', {'class': 'glyphicon-star'})),
        'review': review.get_text()
    }
    info.append(data)

for item in info:
    print('image: ', item['image'])
    print('title: ', item['title'])
    print('price: ', item['price'])
    print('description: ', item['description'])
    print('star: ', item['star'])
    print('review: ', item['review'])
    print('====================')
