import xlrd
import pandas as pd
import sqlite3

# Assign spreadsheet filename to `file`
file = 'inventory_list.xlsx'

# Load spreadsheet
df = pd.ExcelFile(file)

df1 = df.parse('Inventory List Items')
#df = pd.DataFrame(columns=['ITEM ID', 'DESCRIPTION', 'IN STOCK'])
conn = sqlite3.connect('product.db')
cur = conn.cursor()
for index, row in df1.iterrows():
    cur.execute('''INSERT INTO ProductInfo (ItemID, Description, InStock)
    VALUES (?,?,?)''', (row['SKU'], row['DESC-1'], row['IN STOCK']))
    #print(row['SKU'], row['DESC-1'], row['IN STOCK'])


conn.commit()

'''

conn = sqlite3.connect('product.db')
cur = conn.cursor()
'''
