# Load pandas

import pandas as pd


# Webpage url                                                                                                               
url = 'https://ib.techcombank.com.vn/servlet/BrowserServlet'

# Extract tables
dfs = pd.read_html(url)

# Get first table                                                                                                           
df = dfs[0]

# Extract columns                                                                                                           
df2 = df[['Account Number','Available Balances']]
print(df2)

# Write to excel
df2.to_excel('python.xlsx')


