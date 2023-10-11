import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup as soup
import csv

s = HTMLSession()
query='paris'
url=f'https://www.google.com/search?q=weather+{query}'

r=s.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'})
if r.status_code == 200:
    value=(r.html.find('span#wob_tm',first=True).text)
    unit=(r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text)
    describe=(r.html.find('div.VQF4g',first=True).find('span#wob_dc',first=True).text)
    weather = f"{query} - Temperature: {value} {unit}, {describe}"
    print(weather)
    webpage = soup(weather, features="html.parser")
    with open('weather.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if csvfile.tell() == 0:
            writer.writerow(['Location', 'Temperature', 'Description'])
        writer.writerow([query, f"{value} {unit}", describe])
    
else:
    print("Failed to retrieve weather")