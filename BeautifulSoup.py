# import urllib.request
# from bs4 import BeautifulSoup

# soup = BeautifulSoup(urllib.request.urlopen("https://oto.com.vn/bang-gia-xe-o-to-audi-moi-nhat").read(), 'lxml')
# tbody = soup('table', {"class":"tblnormal"})[0].find_all('tr')
# for row in tbody:
#     cols =row.findChildren(recursive = False)
#     cols = [ele.text.strip() for ele in cols]
#     print(cols)
# soup = BeautifulSoup(urllib.request.urlopen("https://finance.yahoo.com/quote/%5EGSPC?p=^GSPC").read(), 'html.parser')
# # soup = BeautifulSoup(html,"html.parser")
# tex_found = soup.find("span",attrs={"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"}).text
# print(tex_found)

from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import xlsxwriter 

names=[]
url="https://finance.yahoo.com/"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
# target = soup.find("span", attrs={"class":"StretchedBox"})
# # intet = target.append(target.text)
# print (target.text)
for i in soup.find_all('tr', attrs={'class':'dt-row Bgc($hoverBgColor):h BdB Bdbc($seperatorColor) H(44px) '}):
    for name in i.find_all('td', attrs={'Va(t) Fz(14px) Whs(nw) Py(6px) Ta(start) Start(0) Pend(10px)'}):
      names.append(name.text)


workbook = xlsxwriter.Workbook('Example3.xlsx') 
worksheet = workbook.add_worksheet("My sheet") 
scores = ( 
    ['ankit', 1000], 
    ['rahul',   100], 
    ['priya',  300], 
    ['harshita',    50], 
) 
row = 0
col = 0
for name, score in (scores): 
    worksheet.write(row, col, name) 
    worksheet.write(row, col + 1, score) 
    row += 1
  
workbook.close() 



