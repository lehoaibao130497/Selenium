
import requests
from bs4 import BeautifulSoup
import csv 
import pandas as pd 
import xlsxwriter 

names=[]
prices=[]
changes=[]
percentChanges=[]
marketCaps=[]
totalVolumes=[]
circulatingSupplys=[]
 
for i in range(0,10):
  CryptoCurrenciesUrl = "https://in.finance.yahoo.com/cryptocurrencies?offset="+str(i)+"&amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;amp;count=50"
  r= requests.get(CryptoCurrenciesUrl)
  data=r.text
  soup=BeautifulSoup(data,'lxml')
 
  for listing in soup.find_all('tr', attrs={'class':'SimpleDataTableRow'}):
    for name in listing.find_all('td', attrs={'aria-label':'Name'}):
      names.append(name.text)
    for price in listing.find_all('td', attrs={'aria-label':'Price (intraday)'}):
      prices.append(price.find('span').text)
    for change in listing.find_all('td', attrs={'aria-label':'Change'}):
      changes.append(change.text)
    for percentChange in listing.find_all('td', attrs={'aria-label':'% change'}):
      percentChanges.append(percentChange.text)
    for marketCap in listing.find_all('td', attrs={'aria-label':'Market cap'}):
      marketCaps.append(marketCap.text)
    for totalVolume in listing.find_all('td', attrs={'aria-label':'Total volume all currencies (24 hrs)'}):
      totalVolumes.append(totalVolume.text)
    for circulatingSupply in listing.find_all('td', attrs={'aria-label':'Circulating supply'}):
      circulatingSupplys.append(circulatingSupply.text)

workbook = xlsxwriter.Workbook('Example3.xlsx') 
worksheet = workbook.add_worksheet("My sheet") 
scores = ( 
    [names], 
    [prices], 
    [changes], 
    [percentChanges], 
) 
row = 0
col = 0
for name, score in (scores): 
    worksheet.write(row, col, name) 
    worksheet.write(row, col + 1, score) 
    row += 1
  
workbook.close() 