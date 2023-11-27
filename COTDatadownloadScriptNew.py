#! pyton3
#Import needed modules 
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import requests
from pandas import read_html
import io
import openpyxl
import xlrd


# create column headers
col = ['Futures','col1','Date','col3','col4','col5','col6','col7','long','short','col10','col11','col12','col13','col14','col15']
# list of items to filter from futures
items = ['AUSTRALIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE','BRITISH POUND - CHICAGO MERCANTILE EXCHANGE','BRITISH POUND STERLING - CHICAGO MERCANTILE EXCHANGE','CANADIAN DOLLAR - CHICAGO MERCANTILE EXCHANGE','EURO FX - CHICAGO MERCANTILE EXCHANGE', 'JAPANESE YEN - CHICAGO MERCANTILE EXCHANGE','NZ DOLLAR - CHICAGO MERCANTILE EXCHANGE','NEW ZEALAND DOLLAR - CHICAGO MERCANTILE EXCHANGE','SWISS FRANC - CHICAGO MERCANTILE EXCHANGE','USD INDEX - ICE FUTURES U.S.','U.S. DOLLAR INDEX - ICE FUTURES U.S.']# colums needed for the dataframe
# colums needed for the dataframe

# updated 2/16/2022 : there was a change in some item names 
renameitem = {'BRITISH POUND - CHICAGO MERCANTILE EXCHANGE':'BRITISH POUND STERLING - CHICAGO MERCANTILE EXCHANGE','NZ DOLLAR - CHICAGO MERCANTILE EXCHANGE':'NEW ZEALAND DOLLAR - CHICAGO MERCANTILE EXCHANGE','USD INDEX - ICE FUTURES U.S.':'U.S. DOLLAR INDEX - ICE FUTURES U.S.' }           


columns = ['Futures','Date','long','short']
# target url contain required data
url ='https://www.cftc.gov/dea/newcot/deafut.txt'


#create request link
s=requests.get(url).content

df=pd.read_csv(io.StringIO(s.decode('utf-8')), header = None)
#create date format mm/dd/YYYY
df[2] =pd.to_datetime(df[2])
df[2] = df[2].apply(lambda x: x.strftime('%m/%d/%Y'))

#select needed  columns
df= df.iloc[:,0:16]
df.columns = col
#filter needed items from Futures column
df = df[df['Futures'].isin(items)]
#select needed columns for dataframe
df = df[columns]

#updated to rename the new item names to the standard item name 
for i in df.index:
    p = i
    c = df['Futures'][i] 
    if df['Futures'][i] in renameitem:
        df['Futures'].replace(df['Futures'][i], renameitem[c],inplace = True )

print("check for data")
print(df)      

#read excel file to pandas
nw = pd.read_excel(r'.\data\Forexdata3.xlsx',sheet_name = 'Sheet1', index_col=None)

#create date format
nw['Date'] =pd.to_datetime(nw['Date'])
nw['Date'] = nw['Date'].apply(lambda x: x.strftime('%m/%d/%Y'))

# append new data to pandas and drop duplicates
nw = nw._append(df, ignore_index=True)
nw=nw.drop_duplicates()
# save to excel 
nw.to_excel(r'.\data\Forexdata3.xlsx',index=False)
print('Completed')