import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set title
st.title("Dashboard dengan Streamlit")

# Sidebar
st.sidebar.header("Pengaturan")
option = st.sidebar.selectbox(
    "Pilih Visualisasi:",
    ("Histogram", "Scatter Plot", "Line Chart")
)

# Generate data
data = pd.DataFrame(
    {
        "x": np.random.randn(100),
        "y": np.random.randn(100)
    }
)

# Plot data berdasarkan pilihan pengguna
st.subheader(option)
if option == "Histogram":
    fig = px.histogram(data, x="x")
    st.plotly_chart(fig)
elif option == "Scatter Plot":
    fig = px.scatter(data, x="x", y="y")
    st.plotly_chart(fig)
elif option == "Line Chart":
    fig = px.line(data, y="y")
    st.plotly_chart(fig)

# Menampilkan data
st.subheader("Data Sample")
st.write(data.head())