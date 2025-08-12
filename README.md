# Nifty_Stock_App

# Project Description

This project is an interactive stock visualization dashboard built using Streamlit and Plotly, designed to analyze and explore Nifty stock market data. The application allows users to filter stocks by sector and symbol, providing an intuitive interface for targeted analysis. Once a stock is selected, the app displays an interactive candlestick chart that visualizes price movements over time, along with an overlaid volume chart to assess trading activity. The dual-axis design enables users to easily correlate price trends with trading volumes. 

# Dataset Fields:

-Date: Purpose: x-axis for charts / time index. (e.g. 2024-01-15)

-Category (sector): Purpose: sidebar filter (st.selectbox) to choose sector. (e.g. Financials, IT).

-Symbol: Purpose: dropdown to select the stock (drives which rows to plot). (e.g. RELIANCE, TCS).

-Open: Purpose: candlestick open price. float (numeric).

-High: Purpose: candlestick high price. float.

-Low: Purpose: candlestick low price. float.

-Close: Purpose: candlestick close price (used for trend/analysis). float.

-Volume: Purpose: overlaid bar chart on secondary y-axis to show trading activity. integer (or numeric).

-Optional fields: Purpose: can be shown as extra metrics, hover info, or additional charts. e.g. Adj Close, Turnover, PE


# Key Focus Area

-Sector-based Filtering: Users can narrow down data by selecting a specific stock market sector (Category), making analysis targeted and efficient.

-Stock-specific Analysis: Ability to drill down into a single stock (Symbol) within the selected sector to view historical performance.

-Candlestick Chart Visualization: Interactive candlestick plots for Open, High, Low, and Close prices to analyze daily market trends.

-Volume Tracking: Overlaid volume bar chart on a secondary y-axis to correlate trading activity with price changes.

-Dual Y-axis Layout: Price (₹) on the left, Volume on the right, for easy side-by-side interpretation.

-Interactive & Responsive UI: Built with Streamlit and Plotly, offering tooltips, zoom, hover data, and real-time chart updates based on selections.

-Data-driven Insights: Enables traders and analysts to quickly identify patterns, spikes, and anomalies in Nifty stock data.

-User-Friendly Filtering Tools: Sidebar dropdowns for sector and stock selection without manual code changes.

-Dark Theme for Better Readability: Improves visual clarity and makes charts look professional.

-Extensibility: Framework supports adding moving averages, RSI, or other indicators for deeper technical analysis in the future.
