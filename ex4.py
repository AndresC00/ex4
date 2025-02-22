import streamlit as st
import plotly.express as px
import pandas as pd

# Sample DataFrame (replace with your actual data)
data = {'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
        'Value': [10, 15, 12, 8, 18, 14]}
df = pd.DataFrame(data)

st.title("My Streamlit App with Plots")

# Bar chart
st.header("Bar Chart")
fig_bar = px.bar(df, x='Category', y='Value', title='Value by Category')
st.plotly_chart(fig_bar)


# Scatter plot (if you have x and y data)
st.header("Scatter Plot")
fig_scatter = px.scatter(df, x='Category', y='Value', title='Value vs Category')
st.plotly_chart(fig_scatter)
