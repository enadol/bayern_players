"""import packages"""
import pandas as pd
import openpyxl

# read file bayern_players.xlsx
df = pd.read_excel('bayern_players.xlsx')
print(df.head())

print(df.columns)

# print data for Harry Kane
