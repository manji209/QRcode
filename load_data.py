import xlrd
import pandas as pd
import sqlite3

# Assign spreadsheet filename to `file`
file = 'inventory_list.xlsx'

# Load spreadsheet
df = pd.ExcelFile(file)

# Parse the Excel sheet into a pandas dataframe
df1 = df.parse('Inventory List Items')

# Make/Open a connection to the database
conn = sqlite3.connect('product.db')

cur = conn.cursor()

# Iterate through the dataframe by row and insert data into the database
for index, row in df1.iterrows():
    cur.execute('''INSERT INTO ProductInfo (ItemID, Description, InStock)
    VALUES (?,?,?)''', (row['SKU'], row['DESC-1'], row['IN STOCK']))


# Commit or write changes to the database
conn.commit()


