import xlsxwriter 
from bs4 import BeautifulSoup
import requests
import urllib


url = "https://finance.yahoo.com/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
# target = soup.find_all("span", attrs={"class":"Fz(s)"})
# target = soup.select('#marketsummary-itm-\^GSPC > h3 > span')
target = soup.find('span',attrs={'class': 'Trsdu(0.3s)'})


workbook = xlsxwriter.Workbook('Exxx.xlsx') 
worksheet = workbook.add_worksheet("Sheet1") 
row = 0
col = 0
# for i in range(5):
#     let = i+1
#     print(let)
names =(["HLB","100"],
        ["PBB","200"],
        ["MBB","200"],
        ["CIMB","200"],
        ["RHB","200"],
        ["HLB","200"]
        )

for name,number in (names):
    for let in target:
        len = str(len)
        worksheet.write(row, col, name) 
        worksheet.write(row, col+1, number) 
        worksheet.write(row, col+2, len)
        row += 1
    workbook.close() 

  
 
