import requests
import csv
from bs4 import BeautifulSoup as bs
from random import randint
from time import sleep

for page in range(1, 150):
    url = "https://www.landsearch.com/industrial/united-states/p"
    page = requests.get(url + str(page) + '/')
    soup = bs(page.content, 'lxml')


    landplots = soup.find_all('div', class_='preview-content')  # .find_all('div',class_="preview-media")

    for l in landplots:
        row = []
        try:
            plot_county = l.find('h2', class_='-g-truncated preview__subterritory').find_next(text=True).text
            plot_price = l.find('span', {"class": 'preview__price'}).find_next(text=True).get_text(strip=True)
            plot_square = l.find('span', {"class": 'preview__size'}).find_next(text=True).get_text(strip=True)
            plot_location = l.find('span', class_='preview__locality -g-truncated').find_next(text=True).text

            row.append(plot_county)
            row.append(plot_price)
            row.append(plot_square)
            row.append(plot_location)

            print(plot_county)
            print(plot_price)
            print(plot_square)
            print(plot_location)
            print()
        except AttributeError:
            continue


        with open("parsing05.csv", 'a', newline = '') as f:
            writer = csv.writer(f)
            writer.writerow(row)