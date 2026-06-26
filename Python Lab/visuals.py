import numpy as np 
import pandas as pd
import requests
import io

import requests


def load_canada_data():
    url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx'
    resp = requests.get(url)
    text = io.BytesIO(resp.content)
    df_can = pd.read_excel(text, sheet_name = 'Canada by Citizenship', skiprows = 20, skipfooter = 2)
    return df_can

df_can = load_canada_data()

# df_can.info(verbose = False)
# verbose = False will print only the column names, data types and non-null values count. True will print all the information about the DataFrame. By default, verbose is set to True. Setting it to False can help reduce the amount of information printed, especially for large DataFrames.

# print(df_can.columns.to_list())
# print (df_can.index.to_list())

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis = 1, inplace = True)
# print(df_can.head())

df_can.rename(columns = {'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace = True)
# print(df_can.head())

# df_can['total'] = df_can.sum(axis = 1)

# df_can.isnull().sum()

# df_can.describe()

# indexing and slicing









