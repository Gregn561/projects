import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a=1
df= pd.read_csv("creditcardtrans/credit_card_transQ1.csv")
df= pd.DataFrame(df)

x= df['category']
y= df['amount']

def plot(x, y, color="blue"):
    plt.bar(x, y, color = color)
    plt.xlabel("category")
    plt.ylabel("amount")
    plt.title("spending by category")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()

plot(x,y)