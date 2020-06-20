# import xlsxwriter module 
import xlsxwriter 
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

url="https://finance.yahoo.com/quote/%5EGSPC?p=%5EGSPC"
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")
target = soup.find("span", attrs={"class":"Fw(b)"})
# intet = target.append(target.text)
print (target.text)

workbook = xlsxwriter.Workbook(r'C:\Users\vnzoo\OneDrive\Desktop\Python\PyautoGUI\Selenium\Exxx.xlsx') 

# By default worksheet names in the spreadsheet will be 
# Sheet1, Sheet2 etc., but we can also specify a name. 
worksheet = workbook.add_worksheet("My sheet") 

# Some data we want to write to the worksheet. 
scores = ( 
	['ankit', target.text], 
	['rahul', 100], 
	['priya', 300], 
	['harshita', 50], 
) 

# Start from the first cell. Rows and 
# columns are zero indexed. 
row = 0
col = 0

# Iterate over the data and write it out row by row. 
for name, score in (scores): 
	worksheet.write(row, col, name) 
	worksheet.write(row, col + 1, score) 
	row += 1

workbook.close() 
