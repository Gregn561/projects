# world bank data visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

#
def low_income_loan_w_col():
    data = cleanworldbank()
    lowincome_borrowers_w_col = data[data['income'] == 'Low income'].sort_values(by=['ai30'], ascending=False)
    lowincome_borrowers_w_col =  lowincome_borrowers_w_col[['country','ai30']].dropna(subset=['ai30'])

    return lowincome_borrowers_w_col

def plot_low_income_loan_w_col():
    data = low_income_loan_w_col()
    country_order = data.groupby('country')['ai30'].mean().sort_values(ascending=False).index
    
    plt.figure(figsize=(15, 8))
    
    ax = sns.barplot(
        x='country', 
        y='ai30', 
        data=data, 
        palette='cividis', 
        hue='country', 
        order=country_order
    )
    
    plt.title('countries requiring percentage of collateral for loans in low income countries', fontsize=16)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Percentage of Collateral', fontsize=12)
    
    # 2. Expand y-axis limits to 115% so the error bar on 'Sudan' or 'Rwanda' doesn't cut off
    ax.set_ylim(0, 115)
    
    # 3. Add labels with a padding adjustment to clear the line caps
    for container in ax.containers:
        ax.bar_label(container, 
                     fmt='%.2f', 
                     fontsize=10,
                     color='white', 
                     padding=4, 
                     label_type='center', 
                     rotation=90)
        
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()

plot_low_income_loan_w_col()

#print(low_income_loan_w_col())