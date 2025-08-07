import pandas as pd
import streamlit as st
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../Dataset/Nifty_Stocks.csv")

# Convert 'Date' column to datetime (if not already)
df['Date'] = pd.to_datetime(df['Date'])

# Sidebar dropdown for sector selection
sector = st.selectbox("Select Sector", df['Category'].unique())

# Filter stocks by selected sector
filtered_df = df[df['Category'] == sector]

# Dropdown for stock symbol
stock = st.selectbox("Select Stock", filtered_df['Symbol'].unique())

# Filter by selected stock
stock_df = filtered_df[filtered_df['Symbol'] == stock]

# Plotting
st.subheader(f"Closing Price Trend for {stock}")
fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(data=stock_df, x='Date', y='Close', ax=ax)
plt.xticks(rotation=90)
plt.tight_layout()

# Show plot in Streamlit
st.pyplot(fig)
