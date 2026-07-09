# world bank data visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests

wb_data = pd.read_excel("financialanalysis/data/raw/Worldbank-global-financial-development-database.xlsx", sheet_name="Data-August2022")

def cleanworldbank():
    # Clean the data
    wb_data_cleaned = wb_data.dropna(
        axis=1,
        how='all'
    )  # Drop rows where all elements are NaN
    wb_data_cleaned = wb_data_cleaned.dropna(
        subset=wb_data.columns[7:],
        how='all'
    )  # Drop columns where all elements are NaN

    return wb_data_cleaned

def worldbank2010data():
    # Get cleaned data, then filter for year 2010
    wb_data_cleaned = cleanworldbank()
    data2010 = wb_data_cleaned[wb_data_cleaned['year'] == 2010]
    return data2010

print(worldbank2010data())