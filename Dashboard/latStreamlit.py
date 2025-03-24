import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Dashboard Hasil Analisis Data Bike Sharing")

# Reading CSV
fileDay = pd.read_csv("day.csv")
df = pd.DataFrame(fileDay)

# Mapping bulan
df['mnth'] = df['mnth'].map({
    1: 'January', 2: 'February', 3: 'March', 4: 'April',
    5: 'May', 6: 'June', 7: 'July', 8: 'August',
    9: 'September', 10: 'October', 11: 'November', 12: 'December'
})
month_order = ['January', 'February', 'March', 'April', 'May', 'June',
               'July', 'August', 'September', 'October', 'November', 'December']
df['mnth'] = pd.Categorical(df['mnth'], categories=month_order, ordered=True)

# Sidebar
st.sidebar.header("📁 Menu Navigasi")
option = st.sidebar.selectbox("Pilih halaman:", ["Potensi", "Trend Pasar"])

# Halaman Potensi
if option == "Potensi":
    st.write("### 🌤️ Potensi Pasar Bike Sharing Berdasarkan Kondisi Cuaca")
    st.image("https://raw.githubusercontent.com/Occolus/latihanOlahData/83f0e0f1b038c077cf3eb63d378d8e4d92a9b96c/Data/Screenshot%202025-03-18%20144434.png")
    st.write("Dari data di atas dapat disimpulkan bahwa potensi penggunaan sepeda meningkat saat cuaca mendukung. "
             "Dengan perbedaan yang mencolok antara hari kerja dan hari libur, besar kemungkinan sepeda digunakan sebagai alat mobilitas utama saat bekerja.")

# Halaman Trend Pasar
elif option == "Trend Pasar":
    st.write("### 📈 Tren Pasar Berdasarkan Tahun")

    # Interaktif dropdown
    year_option = st.selectbox("Pilih tahun:", ["Keduanya", "2011", "2012"])

    # Grouping data
    data2011 = df[df['yr'] == 0].groupby('mnth')['cnt'].sum().sort_index()
    data2012 = df[df['yr'] == 1].groupby('mnth')['cnt'].sum().sort_index()

    # Plot
    fig, ax = plt.subplots(figsize=(10, 5))
    if year_option == "2011":
        ax.plot(data2011.index, data2011.values, label='2011', marker='o', color='orange')
    elif year_option == "2012":
        ax.plot(data2012.index, data2012.values, label='2012', marker='o', color='skyblue')
    else:
        ax.plot(data2011.index, data2011.values, label='2011', marker='o', color='orange')
        ax.plot(data2012.index, data2012.values, label='2012', marker='o', color='skyblue')

    ax.set_title("Total Bike Rentals per Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Total Rentals (cnt)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.write("Dari grafik di atas, terlihat adanya peningkatan signifikan dari tahun 2011 ke 2012, yang menunjukkan tren pasar yang positif.")

# Tombol download data
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Unduh CSV", csv, "day.csv", "text/csv")
