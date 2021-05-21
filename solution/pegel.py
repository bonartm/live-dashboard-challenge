import locale
import pandas as pd
from sqlalchemy import create_engine
from bs4 import BeautifulSoup 

import requests


locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

url = 'https://www.stadt-koeln.de/interne-dienste/hochwasser/pegel_ws.php'

response = requests.get(url)


soup = BeautifulSoup(response.text, 'xml')
height = soup.find('Pegel').get_text()
height = height.replace(',', '.')
time = soup.find('Uhrzeit').get_text()
date = soup.find('Datum').get_text()



## postgres://<username>:<password>@<hostname>/<dbname>
uri = 'postgres://postgres:postgres@localhost/postgres'
engine = create_engine(uri)

df = pd.DataFrame({'timestamp': [date + ' ' + time], 'height': [float(height)]})

# 3. März 2020 20:23
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d. %b %Y %H:%M')


df.to_sql('data', engine, if_exists='append', index=False)


print('completed')

