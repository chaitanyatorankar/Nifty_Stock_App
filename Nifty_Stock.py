import pandas as pd
import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Nifty_Stocks.csv")

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar dropdown for sector selection
sector = st.selectbox("Select Sector", df['Category'].unique())

# Filter stocks by selected sector
filtered_df = df[df['Category'] == sector]

# Dropdown for stock symbol
stock = st.selectbox("Select Stock", filtered_df['Symbol'].unique())

# Filter by selected stock
stock_df = filtered_df[filtered_df['Symbol'] == stock].sort_values(by="Date")

# Calculate Moving Averages
stock_df['MA20'] = stock_df['Close'].rolling(window=20).mean()
stock_df['MA50'] = stock_df['Close'].rolling(window=50).mean()

# Performance Summary
latest_price = stock_df['Close'].iloc[-1]
highest_price = stock_df['Close'].max()
lowest_price = stock_df['Close'].min()
avg_price = stock_df['Close'].mean()

st.subheader(f"📌 Performance Summary for {stock}")
st.write(f"**Latest Price:** ₹{latest_price:.2f}")
st.write(f"**Highest Price:** ₹{highest_price:.2f}")
st.write(f"**Lowest Price:** ₹{lowest_price:.2f}")
st.write(f"**Average Price:** ₹{avg_price:.2f}")

# Plotting
st.subheader(f"📈 Closing Price Trend with Moving Averages for {stock}")
fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(data=stock_df, x='Date', y='Close', ax=ax, label='Close Price')
sb.lineplot(data=stock_df, x='Date', y='MA20', ax=ax, label='20-day MA', color='orange')
sb.lineplot(data=stock_df, x='Date', y='MA50', ax=ax, label='50-day MA', color='green')
plt.xticks(rotation=90)
plt.tight_layout()
plt.legend()

# Show plot in Streamlit
st.pyplot(fig)
