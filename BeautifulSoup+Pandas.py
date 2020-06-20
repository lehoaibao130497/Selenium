import pandas as pd
from bs4 import BeautifulSoup
import requests
from tabulate import tabulate

# # We can convert it to JSON with:
# res = requests.get("https://finance.yahoo.com/cryptocurrencies")
# soup = BeautifulSoup(res.content,'lxml')
# table = soup.find_all('table')[0] 
# df = pd.read_html(str(table))
# print(df[0].to_json(orient='records'))
# Converting to lists
res = requests.get("https://finance.yahoo.com/cryptocurrencies")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))[0]
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
print( tabulate(df[0], headers='keys', tablefmt='psql') )