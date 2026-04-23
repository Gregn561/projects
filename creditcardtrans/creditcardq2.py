import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('creditcardtrans/credit_card_transQ4.csv')

x = df['month']
y = df['amount']

def plot(x,y):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Spending by Month')
    plt.grid(True)
    plt.show()

plot(x, y)
