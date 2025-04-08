import streamlit as st
import pandas as pd
import matplotlib.pyplot as ax

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
option = st.sidebar.selectbox("Pilih halaman:", ["Potensi", "Trend Tahunan"])

# Halaman Potensi
if option == "Potensi":
    fig, ax = ax.subplots(figsize=(10, 5)) 
    st.write("### 🌤️ Potensi Pasar Bike Sharing Berdasarkan Kondisi Cuaca")
    option2 = st.selectbox("Pilih Model Grafik:", [ "Perbulan", "Total"])

    if option2 == "Perbulan":
        # Mengelompokkan data berdasarkan cuaca
        mist_data = df[df['weathersit'] == 2].groupby('mnth')['cnt'].sum()
        clear_data = df[df['weathersit'] == 1].groupby('mnth')['cnt'].sum()
        lightrain_data = df[df['weathersit'] == 3].groupby('mnth')['cnt'].sum()
        Heavyrain_data = df[df['weathersit'] == 4].groupby('mnth')['cnt'].sum()

        ax.plot(mist_data.index, mist_data.values, label='Mist', marker='o', color='orange')
        ax.plot(clear_data.index, clear_data.values, label='Clear', marker='o', color='skyblue')
        ax.plot(lightrain_data.index, lightrain_data.values, label='Light Rain/Snow', marker='o', color='green')
        ax.plot(Heavyrain_data.index, Heavyrain_data.values, label='Heavy Rain/Snow', marker='o', color='red')

        ax.grid(True)

        ax.set_title('Total Bike Rentals per Month Based on Weather Conditions') 
        ax.set_xlabel('Month') 
        ax.set_ylabel('Total Bike Rentals (cnt)') 

        ax.legend()

        st.pyplot(fig) 

    if option2 == "Total":
        mist_data = df[df['weathersit'] == 2].groupby('mnth')['cnt'].sum()
        clear_data = df[df['weathersit'] == 1].groupby('mnth')['cnt'].sum()
        lightrain_data = df[df['weathersit'] == 3].groupby('mnth')['cnt'].sum()
        Heavyrain_data = df[df['weathersit'] == 4].groupby('mnth')['cnt'].sum()

        weather_data = {
            'Mist': mist_data.sum(),  
            'Clear': clear_data.sum(),
            'Light Rain/Snow': lightrain_data.sum(),
            'Heavy Rain/Snow': Heavyrain_data.sum(),
        }

        # Grafik Bar
        ax.bar(weather_data.keys(), weather_data.values(), color=['orange', 'skyblue', 'green', 'red'])  
        ax.set_title('Total Bike Rentals Based on Weather Conditions')  
        ax.set_xlabel('Weather Condition') 
        ax.set_ylabel('Total Users') 
        ax.legend()
        ax.ticklabel_format(axis='y',style='plain',scilimits=(0,0))
        st.pyplot(fig) 

   

    st.write("Berdasarkan analisis pengaruh cuaca terhadap penggunaan sepeda, terlihat bahwa cuaca cerah (Clear) memiliki pengaruh yang sangat signifikan terhadap tingginya penggunaan sepeda. Bulan September menunjukkan lonjakan drastis dalam penggunaan sepeda, dibandingkan dengan bulan November yang cenderung lebih rendah, terutama saat cuaca sedikit hujan atau hujan deras. Hal ini menyoroti tantangan terbesar bagi penyedia layanan bike-sharing, yaitu pengaruh cuaca yang kurang mendukung, di mana penggunaan sepeda menjadi jauh lebih sedikit saat cuaca buruk. Grafik yang menunjukkan penggunaan sepeda selama cuaca cerah dan hujan menunjukkan perbedaan yang jelas, dengan grafik hijau dan oranye yang mencerminkan penurunan penggunaan saat cuaca hujan.")

# Halaman Trend Pasar
elif option == "Trend Tahunan":
    st.write("### 📈 Tren Pasar Berdasarkan Tahun")

    year_option = st.selectbox("Pilih tahun:", ["Keduanya", "2011", "2012"])

    # Grouping data berdasarkan tahun
    data2011 = df[df['yr'] == 0].groupby('mnth')['cnt'].sum().sort_index()
    data2012 = df[df['yr'] == 1].groupby('mnth')['cnt'].sum().sort_index()

    fig, ax = ax.subplots(figsize=(10, 5))

    if year_option == "2011":
        ax.plot(data2011.index, data2011.values, label='2011', marker='o', color='orange')
        ax.set_title("Total Bike Rentals per Month (2011)")
    elif year_option == "2012":
        ax.plot(data2012.index, data2012.values, label='2012', marker='o', color='skyblue')
        ax.set_title("Total Bike Rentals per Month (2012)")
    else:
        ax.plot(data2011.index, data2011.values, label='2011', marker='o', color='orange')
        ax.plot(data2012.index, data2012.values, label='2012', marker='o', color='skyblue')
        ax.set_title("Total Bike Rentals per Month (2011 vs 2012)")

    ax.set_xlabel("Month")
    ax.set_ylabel("Total Rentals (cnt)")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.write("Tren Penggunaan Sepeda (2011 vs 2012): Setelah melakukan clustering terhadap data pengguna sepeda pada tahun 2011 dan 2012, dapat disimpulkan bahwa tren penggunaan sepeda menunjukkan peningkatan yang signifikan pada tahun 2012. Hal ini menunjukkan bahwa sepeda menjadi pilihan transportasi yang semakin populer di tahun berikutnya, yang mungkin disebabkan oleh faktor-faktor seperti peningkatan kesadaran akan gaya hidup sehat, kemudahan mobilitas, dan kebijakan yang mendukung penggunaan sepeda di kota-kota besar")

# Tombol download data
csv = df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Unduh CSV", csv, "day.csv", "text/csv")
