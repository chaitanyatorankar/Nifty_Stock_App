import pandas as pd
import streamlit as st
import plotly.graph_objects as go

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

# Candlestick Chart
fig = go.Figure(data=[
    go.Candlestick(
        x=stock_df['Date'],
        open=stock_df['Open'],
        high=stock_df['High'],
        low=stock_df['Low'],
        close=stock_df['Close'],
        name='Candlesticks'
    )
])

# Add Volume as bar chart
fig.add_trace(
    go.Bar(
        x=stock_df['Date'],
        y=stock_df['Volume'],
        name='Volume',
        marker_color='lightblue',
        opacity=0.4,
        yaxis='y2'
    )
)

# Layout for dual y-axis
fig.update_layout(
    title=f"💹 {stock} - Interactive Candlestick with Volume",
    xaxis_rangeslider_visible=False,
    yaxis_title='Price (₹)',
    yaxis2=dict(
        overlaying='y',
        side='right',
        showgrid=False,
        title='Volume'
    ),
    template="plotly_dark",
    height=700
)

# Show chart
st.plotly_chart(fig, use_container_width=True)
