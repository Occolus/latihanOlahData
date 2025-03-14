import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Dashboard Hasil dari Analisis data Bike Sharing")

# Sidebar
st.sidebar.header("Menu")
option = st.sidebar.selectbox("Pilih opsi:", ["Potensi", "Trend Pasar"])

# Halaman Beranda
if option == "Potensi":
    st.write("### Potensi Pasar Bike Sharing berdasarkan kondisi cuaca.")
    st.image(r"D:\ML Dicoding\latihanOlahData\Data\total user cuaca.png")
    st.image(r"D:\ML Dicoding\latihanOlahData\Data\Screenshot 2025-03-14 235730.png")
    st.write("dari data diatas dapat disimpulkan bahwa potensi penggunaan Bike digunakan saat cuaca mendukung.")

# Halaman Data
elif option == "Trend Pasar":
    st.write("### Data Hasil dari Explore Data untuk mengidentifikasi Trend pasar berdasarkan kondisi pengguna")
    st.image(r"D:\ML Dicoding\latihanOlahData\Data\perbandingan workholi.png")
    st.write("dari data diatas dapat disimpulkan bahwa Bike cenderung digunakan saat kondisi pengguna sedang bekerja..")
   
        
        # # Download Data
        # csv = df.to_csv(index=False).encode('utf-8')
        # st.download_button("Unduh CSV", csv, "data.csv", "text/csv")

  

