import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("Aemf1.csv")

# Dashboard title
st.title("Airbnb Europe Dashboard")

# -------------------------------------------------
# 1. Price Distribution
# -------------------------------------------------
fig1 = px.histogram(df, x='Price', nbins=40,
                    title='Price Distribution of Listings')
st.plotly_chart(fig1)

# -------------------------------------------------
# 2. Top Cities by Number of Listings
# -------------------------------------------------
top_cities = df['City'].value_counts().head(10)
fig2 = px.bar(x=top_cities.values,
              y=top_cities.index,
              orientation='h',
              title='Top Cities by Number of Listings',
              labels={'x':'Listings','y':'City'})
st.plotly_chart(fig2)

# -------------------------------------------------
# 3. Bedrooms vs Price
# -------------------------------------------------
fig3 = px.scatter(df,
                  x='Bedrooms',
                  y='Price',
                  title='Bedrooms vs Price')
st.plotly_chart(fig3)

# -------------------------------------------------
# 4. Average Price by Room Type
# -------------------------------------------------
avg_price_room = df.groupby('Room Type')['Price'].mean().reset_index()
fig4 = px.bar(avg_price_room,
              x='Room Type',
              y='Price',
              title='Average Price by Room Type')
st.plotly_chart(fig4)

# -------------------------------------------------
# 5. Availability vs Price
# -------------------------------------------------
if 'Guest Satisfaction' in df.columns:
    fig5 = px.scatter(df,
                      x='Guest Satisfaction',
                      y='Price',
                      title='Reviews vs Price')
    st.plotly_chart(fig5)
