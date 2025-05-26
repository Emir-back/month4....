import requests
from bs4 import BeautifulSoup as BS 

url = 'https://filmix.my/'

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0"
 }

def get_html(url,params=''):
    request = requests.get(url,headers=HEADERS,params=params)
    return request 

def get_data(html):
    bs = BS(html, features='html.parser')
    items = bs.find_all('div', class_='container category_slider')
    filmix_list = []

    for item in items:
        title_block = item.find("div", class_='shortstory-title')
        if title_block:
            title = title_block.get_text(strip=True)
            filmix_list.append({
                'title': title
            })
        else:
            print("⚠️ 'shortstory-title' не найден в элементе.")
    
    return filmix_list


def parsing_filmix():
    response = get_html(url)
    if response.status_code == 200:
        filmix_list_2 = []
        for page in range(1,10):
            response = get_html('https://filmix.my/seria/', params={'page':page})
            filmix_list_2.extend(get_data(response.text))
        return filmix_list_2
    else:
        print('Error')  

    