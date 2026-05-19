import os
import sqlite3
import pandas as pd
import yfinance as yf

script_dir = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(script_dir, 'data', 'raw')
os.makedirs(folder_path, exist_ok=True)

file_path = os.path.join(folder_path, 'sp500_prices.csv')

ticker = ('AAPL', 'MSFT', '^GSPC')
all_data = []

for t in ticker:
    df = yf.download(t, start='2015-01-01')
    # Flatten the columns if they are multi-indexed (e.g., due to adjustments)
    df.columns = df.columns.get_level_values(0)
    # Add a 'Symbol' column to identify the stock
    df['Symbol'] = t
    # Reset index to have 'Date' as a column instead of index
    df.reset_index(inplace=True)
    # Append the dataframe to the list
    all_data.append(df)

# Concatenate all dataframes
raw_data = pd.concat(all_data, ignore_index=True)

# Save CSV
raw_data.to_csv(file_path, index=False)

# Read CSV
df = pd.read_csv(file_path)

# SQLite connection
conn = sqlite3.connect(':memory:')

# Load into SQL table
df.to_sql('stocks', conn, index=False, if_exists='replace')

# top 10 closing prices for AAPL
q1result = pd.read_sql("""
select Symbol, Date, Close
from stocks
where symbol = 'AAPL'
order by Close DESC
limit 10
""", conn
)

#average volume for each stock
q2result = pd.read_sql(
    """
    select symbol, avg(volume) as avg_volume
    from stocks
    group by symbol
    """, conn
)

# stocks with more than 100 days of closing price above 200
q3result = pd.read_sql(
    """
    select Symbol
    from stocks
    where Close > 200
    group by Symbol
    having count(*) > 100
    """, conn
)

# stocks with intraday volatility (high - low) / open > 5%
q4result = pd.read_sql(
    """
    SELECT Date, (high - low) / open * 100 AS intraday_volatility
    FROM stocks
    where intraday_volatility > 5
    limit 10
    """, conn)

print(q4result)
# print(df.head())