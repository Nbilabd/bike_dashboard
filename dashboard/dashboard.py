import streamlit as st
import pandas as pd

# Memuat data
file_name = "day.csv"
bike_data = pd.read_csv(file_name)

# Judul dashboard
st.title("Dashboard Analisis Data Peminjaman Sepeda")

