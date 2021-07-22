import requests
import schedule
import time
import json


def func():
    r = requests.get('https://flight.yatra.com/lowest-fare-service/dom2/get-fare?origin=DEL&destination=CJB&from=02-07-2021&to=22-07-2021&tripType=O&airlines=all&_i=1410119548731&src=srp',headers={'User-Agent': 'Mozilla/5.0'})
    package_json = r.json()
    lowestfare = package_json['day']['2021-07-12']['lf'] #find lowest price from the json from the Yatra site API
    print(lowestfare)
    if lowestfare < 9368:
        print("Book Ticket")


schedule.every(5).seconds.do(func) #run func() after every 5 seconds

while True:
    schedule.run_pending()
    func()
    time.sleep(5)
