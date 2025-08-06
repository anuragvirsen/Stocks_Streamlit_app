import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# Load data
df = pd.read_csv("Nifty_Stocks.csv")

# Streamlit title
st.title("Nifty Stocks Viewer")

# Category selection
category = st.selectbox("Select Category", df['Category'].unique())

# Filter based on category
filtered_cat = df[df['Category'] == category]

# Symbol selection
symbol = st.selectbox("Select Symbol", filtered_cat['Symbol'].unique())

# Filter based on symbol
filtered_symbol = filtered_cat[filtered_cat['Symbol'] == symbol]

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
sb.lineplot(x="Date", y="Close", data=filtered_symbol, ax=ax)
ax.set_title(f"{symbol} Closing Prices")
plt.xticks(rotation=45)

# Show in Streamlit
st.pyplot(fig)
