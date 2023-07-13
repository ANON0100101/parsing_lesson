# python3 -m venv venv -создание виртуального окружения
#  source ./venv/bin/activate -активация виртуального окружения
# pip freeze - показывает список установленных библиотек
#  deactivate -выйти из виртуального окружения 
# pip install requests
# lxml
# beautifulsoup4 



import requests
import csv
from bs4 import BeautifulSoup as BS

def get_html(url):
    response = requests.get(url)
    # print(response.status_code)
    return response.text


def get_data(html):
    soup = BS(html,'lxml')
    catalog = soup.find('div', class_='catalog-list')
    cars = catalog.find_all('a',class_='catalog-list-item')
    for car in cars:
        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
        except:
            title =''
        try:
            img =car.find('img', class_='catalog-item-cover-img').get('src')
        except:
            img =''
        with open('cars.csv', 'a')as file:
            fields = ['title','image']
            writer = csv.DictWriter(file, delimiter=',',fieldnames=fields)
            writer.writerow({'title': title, 'image':img})


def main():
    URL ='https://cars.kg/offers/'
    html = get_html(URL)
    get_data(html)

    
main()
