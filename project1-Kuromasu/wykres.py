import pandas as pd
import matplotlib.pyplot as plt

# wczytanie danych
df = pd.read_csv('./dane.csv')

# podzielenie danych na dwie serie
df_5x5 = df[df['rozmiar']=='5x5']
df_10x10 = df[df['rozmiar']=='10x10']
df_15x15 = df[df['rozmiar']=='15x15']


# tworzenie wykresu
fig, ax = plt.subplots()
ax.scatter(df_5x5['czas'], df_5x5['wynik'], c='blue', label='5x5')
ax.scatter(df_10x10['czas'], df_10x10['wynik'], c='red', label='10x10')
ax.scatter(df_15x15['czas'], df_15x15['wynik'], c='green', label='15x15')

ax.set_xlabel('Czas')
ax.set_ylabel('Wynik')
ax.legend()
plt.show()
