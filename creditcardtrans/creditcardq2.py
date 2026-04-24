import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv('creditcardtrans/credit_card_transQ4.csv')

# Convert the 'month' column to datetime format
df['month'] = pd.to_datetime(df['month'], utc=True)

# Format the month as 'MM'
x = df['month'].dt.strftime('%b')  
x = x[::-1]  # Reverse the order of the months
y = df['amount']
y = y[::-1]  # Reverse the order of the amounts to match the reversed months

def plot(x,y):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Spending by Month')
    plt.grid(True)
    plt.show()

plot(x, y)
