locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

from bs4 import BeautifulSoup 

height = height.replace(',', '.')

## postgres://<username>:<password>@<hostname>/<dbname>
uri = 'postgres://postgres:postgres@localhost/postgres'

df.to_sql(???, ???, if_exists='append', index=False)

date = soup.find('Datum').get_text()

import locale

df = pd.DataFrame({'timestamp': [date + ' ' + time], 'height': [float(???)]})

import pandas as pd

print('completed')

from sqlalchemy import ???

url = 'https://www.stadt-koeln.de/interne-dienste/hochwasser/pegel_ws.php'

# 3. März 2020 20:23
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d. %b %Y %H:%M')

import requests

soup = BeautifulSoup(response.text, 'xml')

height = soup.find(???).get_text()

engine = create_engine(uri)

time = soup.find(???).get_text()

response = requests.get(???)
