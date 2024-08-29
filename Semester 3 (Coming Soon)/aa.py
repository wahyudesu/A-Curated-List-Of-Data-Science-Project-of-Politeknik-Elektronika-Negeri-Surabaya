import pandas as pd
import random
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("sidoarjo.csv", delimiter=";")
data['kategori'] = data.apply(lambda x: random.randint(1, 3), axis=1)

# display estimation parameter data
st.title("QUICK COUNT PROJECT")
st.write("This project aims to provide a quick count analysis of election data, offering insights into the distribution of votes across different groups.")

col1, col2 = st.columns(2)

kategori_counts = data['kategori'].value_counts()
fig, ax = plt.subplots(figsize=(4, 4))  # Adjusted figure size for smaller plot
ax.pie(kategori_counts, labels=kategori_counts.index, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Plot pemilu')
col1.pyplot(fig)

# Expander
with col2.expander("🧩 Nama Kelompok", False):
  st.write("Wahyu")
  st.write("Wahyu")
  st.write("Wahyu")
  st.write("Wahyu")
