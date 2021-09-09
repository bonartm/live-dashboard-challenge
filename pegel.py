import locale
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import requests

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

# scrape the public API
url = 'https://www.stadt-koeln.de/interne-dienste/hochwasser/pegel_ws.php'
response = requests.get(url)

# extract information from xml doc
soup = BeautifulSoup(response.text, 'xml')
height = soup.find('Pegel').get_text()
height = height.replace(',', '.')
time = soup.find('Uhrzeit').get_text()
date = soup.find('Datum').get_text()

# create a dataframe
df = pd.DataFrame({
    'timestamp': [date + ' ' + time],
    'height': [float(height)]
})
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d. %B %Y %H:%M')

# send data to sql server

# postgresql://<username>:<password>@<hostname>/<dbname>
uri = 'postgresql://postgres:postgres@localhost/postgres'
engine = create_engine(uri)

df.to_sql('pegel', engine, if_exists='append', index=False)
print(f"fetched new data at {datetime.now()}")
