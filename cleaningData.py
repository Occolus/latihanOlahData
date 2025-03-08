import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

#inisialisasi csv customer
customers_df = pd.read_csv(r"D:\ML Dicoding\latihanCleaningData\customers.csv")
#print(customers_df.head())

#inisialisasi csv order
order_df = pd.read_csv(r"D:\ML Dicoding\latihanCleaningData\orders.csv")
#print(order_df.head)

#inisialisasi csv product
product_df = pd.read_csv(r"D:\ML Dicoding\latihanCleaningData\products.csv")
#print(product_df.head)

#inisialisasi csv sales
sales_df = pd.read_csv(r"D:\ML Dicoding\latihanCleaningData\sales.csv")
# print(sales_df.head)
# print(customers_df.info())
print(customers_df.isna().sum())
# print("Jumlah duplikasi: ", customers_df.duplicated().sum())
print(customers_df.describe())