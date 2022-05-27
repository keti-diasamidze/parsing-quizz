import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint

file = open('vinyl_albums.csv', 'w', encoding='utf-8_sig', newline='\n')
file_obj = csv.writer(file)
file_obj.writerow(['Album name/Type', 'Artist', 'Year', 'Price', 'image'])
ind = 0

while ind<=5:
    ind = ind + 1
    url = 'https://recordsale.de/en/featured/rare-and-expensive' + '?page=' + str(ind)
    resp = requests.get(url)
    # print(resp)
    soup = BeautifulSoup(resp.text, 'html.parser')
    section = soup.find('div', class_="l-releaseList l-releaseList--withSidebar")
    albums = section.find_all('div', class_='l-listItem')

    for album in albums:
        img_link = album.find('div', class_='release-content')
        features = album.find('div', class_='release-details')
        # print(features)
        name = features.find('div', class_='release-name').text
        year = features.find('date', class_='release-date').text.strip()
        img = img_link.find('div',  class_="release-image")
        new_image = img.find('div', class_='record-thumb').img.attrs.get('src')
        artist = features.find('div', class_='release-artist').text
        year_list = (year.split())
        if len(year_list) == 0:
            year_list.append('None')
        else:
            pass

        try:
            price = features.find('div', class_="reducedPrice campaignDiscount discount").text
            file_obj.writerow([name,artist,year_list[0], price, new_image])
        except AttributeError:
            file_obj.writerow([name, artist, year_list[0], 'None', new_image])



    sleep(randint(5, 10))

file.close()
