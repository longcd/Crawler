import requests
from bs4 import BeautifulSoup

# 获取房子基本信息
def fangzi_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    title = soup.select('div.pho_info > h4 > em')
    address = soup.select('span.pr5')
    price = soup.select('div.day_top clearfix')
    price = soup.select('div#pricePart')
    photo = soup.select('img#curBigImage')
    member = soup.select('.member_pic > a > img')
    name = soup.select('a.lorder_name')
    gender = soup.select('div.w_240 > h6 > span')

    data = {
        'title': title[0].get_text(),
        'address': address[0].get_text().strip(),
        'price': price[0].get_text().strip(),
        'photo': photo[0].get('src'),
        'member': member[0].get('src'),
        'name': name[0].get_text(),
        'gender': 'boy' if 'boy' in gender[0].get('class')[0] else 'girl' 
    }
    print(data)
    return data

page_link = [] # 每个详情页的链接都存在这里

# 获取列表页里的房子详情页URL
def get_page_link(page_number): # page_number 要获取列表页的页数
    for i in range(0, page_number):
        full_url = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(i+1)
        wb_data = requests.get(full_url)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        for link in soup.select('a.resule_img_a'): # 找到这个 class 样为 resule_img_a 的 a 标签即可
            page_link.append(link.get('href'))

# get_page_link(1)
# print(page_link)

get_page_link(10)
for url in page_link:
   fangzi_info(url) 
