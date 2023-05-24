import matplotlib.pyplot as plt
from datetime import datetime
import json
import numpy as np
import pandas as pd

date_before =[]
values_before=[]
with open('./data/before.txt', 'r') as file:
    for line in file:  
        parsed_data = json.loads(line)
        # print(parsed_data['nltk'])
        values_before.append(parsed_data['nltk']['compound'])
        date_before.append(datetime.strptime(parsed_data["date"].strip('\"'), '%Y-%m-%dT%H:%M:%S+00:00').date())
date_during =[]
values_during=[]
with open('./data/durring.txt', 'r') as file:
    for line in file:  
        parsed_data = json.loads(line)
        # print(parsed_data['nltk'])
        values_during.append(parsed_data['nltk']['compound'])
        date_during.append(datetime.strptime(parsed_data["date"].strip('\"'), '%Y-%m-%dT%H:%M:%S+00:00').date())

date_after =[]
values_after=[]        
with open('./data/now.txt', 'r') as file:
    for line in file:  
        parsed_data = json.loads(line)
        # print(parsed_data['nltk'])
        values_after.append(parsed_data['nltk']['compound'])
        date_after.append(datetime.strptime(parsed_data["date"].strip('\"'), '%Y-%m-%dT%H:%M:%S+00:00').date())
        


# Tworzenie DataFrame z danymi
df_before = pd.DataFrame({'Data': date_before, 'Sentyment': values_before})
df_during = pd.DataFrame({'Data': date_during, 'Sentyment': values_during})
df_after = pd.DataFrame({'Data': date_after, 'Sentyment': values_after})


# Grupowanie i obliczanie średniej dla każdego dnia
df_before = df_before.groupby('Data').mean().reset_index()
df_during = df_during.groupby('Data').mean().reset_index()
df_after = df_after.groupby('Data').mean().reset_index()


# Tworzenie wykresu
# plt.plot(df['Data'], df['Sentyment'])

# Dodawanie tytułu i etykiet osi
plt.title('Zmiany emocji w czasie. Teraz 2023 ')
plt.xlabel('Data')
plt.ylabel('Średni sentyment')

# Formatowanie osi czasu
plt.xticks(rotation=25)  # Obrót etykiet osi x o 45 stopni

# Tworzenie wykresu z rozmyciem
# plt.plot(df_before['Data'], np.zeros(len(df_before['Sentyment'])))
# plt.plot(df_before['Data'], df_before['Sentyment'])

# plt.plot(df_during['Data'], np.zeros(len(df_during['Sentyment'])))
# plt.plot(df_during['Data'], df_during['Sentyment'])

plt.plot(df_after['Data'], np.zeros(len(df_after['Sentyment'])))
plt.plot(df_after['Data'], df_after['Sentyment'])


# Skalowanie osi Y
plt.ylim(-0.5, 0.5)
# Wyświetlanie wykresu
plt.show()