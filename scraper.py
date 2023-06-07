import requests
from bs4 import BeautifulSoup
import csv

hotele = []
samoloty = []

URL = "https://www.coraltravel.pl/wczasy/wyniki-wyszukiwania/termin:20.03.2023+do+20.06.2023/dorosli:2/noce:7+do+14/"

for i in range(0, 5):
    if i == 0:
        page = requests.get(URL)
    else:
        page = requests.get(URL + str(i*20) + "/")

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("div", class_="row result")

    for offer in results:
        hotel_name = offer.find("input", class_="hotelNameForArray")['value']
        print("Hotel name: " + hotel_name)
        hotel_pic = offer.find("img", class_="resultPic lazyload")['data-src']
        print("Hotel picture: " + hotel_pic)
        hotel_stars = offer.select_one('div[class*="stars "]')['class']
        print("Hotel stars: " + hotel_stars[1].split("_")[1])
        hotel_region = offer.find("div", class_="resultRegion").text.strip()
        hotel_region = hotel_region.split(',')
        print("Hotel country: " + hotel_region[0])
        print("Hotel city: " + hotel_region[1].strip())
        flight = offer.find("div", class_="resultFlight").text.strip()
        flight = flight.split('-')
        print("Flight departure: " + flight[0].split(':')[1].strip())
        print("Flight arrival: " + flight[1].strip())

        print("\n")

        hotele.append({'Nazwa':hotel_name, 'Zdjecie':hotel_pic, 'Gwiazdki':hotel_stars[1].split("_")[1], 'Region':hotel_region[0], 'Miasto':hotel_region[1].strip()})
        samoloty.append({'Odlot':flight[0].split(':')[1].strip(), 'Przylot':flight[1].strip(), 'PrzylotKraj':hotel_region[0]})

hotele = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in hotele)]
samoloty = [dict(tupleized) for tupleized in set(tuple(item.items()) for item in samoloty)]

hoteleCSV = open('hoteleBaza.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(hoteleCSV)
writer.writerow(['Nazwa', 'Zdjecie', 'Gwiazdki', 'Region', 'Miasto'])
for hotel in hotele:
    writer.writerow(hotel.values())
hoteleCSV.close()

lotyCSV = open('lotyBaza.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(lotyCSV)
writer.writerow(['Odlot', 'Przylot', 'PrzylotKraj'])
for lot in samoloty:
    writer.writerow(lot.values())
lotyCSV.close()

print(len(hotele))
print(len(samoloty))
print("\n")
