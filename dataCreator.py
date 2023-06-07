import csv
import datetime
import random

def randDate():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

hotele = []
samoloty = []
wyzywienie = ["onlyBreakfast", "breakfastAndDinner", "allInclusive"]
typPokoju = ["small", "medium", "large", "apartment", "studio"]
zniżki = [10, 25, 50]
dni = [7, 10, 14]
wyzywienieRatio = {"allInclusive": 1.25, "onlyBreakfast": 1, "breakfastAndDinner": 1.1}
starsPrice = {'1': 75, '2': 150, '3': 300, '4': 500, '5': 1000}

hoteleCSV = open('hoteleBaza.csv', 'r', encoding="utf-8")
reader = csv.DictReader(hoteleCSV, skipinitialspace=True)
for hotel in reader:
    hotele.append(hotel)
hoteleCSV.close()

lotyCSV = open('lotyBaza.csv', 'r', encoding="utf-8")
reader = csv.DictReader(lotyCSV, skipinitialspace=True)
for lot in reader:
    samoloty.append(lot)
lotyCSV.close()

hoteleOferty = []
samolotyOferty = []

for hotel in hotele:
    i = random.randint(0, 100)
    for x in range(i):
        tmp = hotel.copy()
        ww = randDate()
        znizka = random.randint(0, 100)
        tmp['Start'] = ww
        durat = random.choice(dni)
        tmp['Koniec'] = ww + datetime.timedelta(days=durat)
        tmp['Dorosli'] = random.randint(1, 4)
        tmp['Dziecko3'] = random.randint(0, 2)
        tmp['Dziecko10'] = random.randint(0, 2)
        tmp['Dziecko18'] = random.randint(0, 2)
        tmp['Wyzywienie'] = random.choice(wyzywienie)
        tmp['Typ_pokoju'] = random.choice(typPokoju)
        if znizka < 5:
            tmp['Znizka'] = random.choice(zniżki)
        else:
            tmp['Znizka'] = 0
        tmp['Cena'] = durat * starsPrice[tmp['Gwiazdki']] * wyzywienieRatio[tmp['Wyzywienie']] * (tmp['Dorosli'] + (0.25 * tmp['Dziecko3']) + (0.5 * tmp['Dziecko10']) + (0.75 * tmp['Dziecko18'])) * ((100 - tmp['Znizka'])/100)
        hoteleOferty.append(tmp)

lotPolska = []
lotInne = []

for lot in samoloty:
    lotPolska.append(lot['Odlot'] + ":Polska")
    lotInne.append(lot['Przylot'] + ":" + lot['PrzylotKraj'])

lotPolska = list(dict.fromkeys(lotPolska))
lotInne = list(dict.fromkeys(lotInne))

for lot in lotPolska:
    i = random.randint(0, 100)
    for x in range(i):
        ww = randDate()
        przylot = random.choice(lotInne)
        samolotyOferty.append({'OdlotKraj':lot.split(":")[1], 'Odlot':lot.split(":")[0], 'PrzylotKraj':przylot.split(":")[1], 'Przylot':przylot.split(":")[0], 'Data':ww, 'WolneMiejsca':random.randint(0, 200)})

for lot in lotInne:
    i = random.randint(0, 100)
    for x in range(i):
        ww = random.randint(1, 52)
        przylot = random.choice(lotPolska)
        samolotyOferty.append({'OdlotKraj':lot.split(":")[1], 'Odlot':lot.split(":")[0], 'PrzylotKraj':przylot.split(":")[1], 'Przylot':przylot.split(":")[0], 'Data':ww})

hoteleOfertyCSV = open('hoteleOfertyBaza.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(hoteleOfertyCSV)
writer.writerow(['Nazwa', 'Zdjecie', 'Gwiazdki', 'Region', 'Miasto', 'Start', 'Koniec', 'Dorosli', 'Dziecko3', 'Dziecko10', 'Dziecko18', 'Wyzywienie', 'Typ_pokoju', "Znizka", "Cena"])
for hotel in hoteleOferty:
    writer.writerow(hotel.values())
hoteleOfertyCSV.close()

lotyOfertyCSV = open('lotyOfertyBaza.csv', 'w', encoding="utf-8", newline='')
writer = csv.writer(lotyOfertyCSV)
writer.writerow(['OdlotKraj', 'Odlot', 'PrzylotKraj', 'Przylot', 'Data', 'WolneMiejsca'])
for lot in samolotyOferty:
    writer.writerow(lot.values())
lotyOfertyCSV.close()

print("dsad")