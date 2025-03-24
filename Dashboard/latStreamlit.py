import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title
st.title("Dashboard Hasil dari Analisis Data Bike Sharing")

# Reading CSV
fileDay = pd.read_csv("day.csv")
df = pd.DataFrame(fileDay)

# Sidebar
st.sidebar.header("Menu")
option = st.sidebar.selectbox("Pilih opsi:", ["Potensi", "Trend Pasar"])

# Halaman Beranda
if option == "Potensi":
    st.write("### Potensi Pasar Bike Sharing berdasarkan kondisi cuaca.")
    st.image("https://raw.githubusercontent.com/Occolus/latihanOlahData/83f0e0f1b038c077cf3eb63d378d8e4d92a9b96c/Data/Screenshot%202025-03-18%20144434.png")
    st.write("Dari data di atas dapat disimpulkan bahwa potensi penggunaan Bike digunakan saat cuaca mendukung."
    "Dengan kontras yang sangat jauh antara pengguna setelah melakukan perbandingan antara Workingday dan Holiday, Kemungkinan besar pengguna Menggunakannya untuk kemudahan mobilitas mereka saat bekerja. ")


# Halaman Data
elif option == "Trend Pasar":
    st.write("### Data Hasil dari xplore Data untuk mengidentifikasi Trend pasar berdasarkan kondisi pengguna")
    st.image("https://raw.githubusercontent.com/Occolus/latihanOlahData/main/Data/Screenshot%202025-03-24%20123546.png") 
    st.write("Dari data di atas berdasarkan tahunnya, dapat disimpulkan tren tersebut naik jika dibangdingkan dengan tahun sebelumnya.")

# Download Data
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("Unduh CSV", csv, "day.csv", "text/csv")
