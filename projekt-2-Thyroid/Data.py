import pandas as pd


data=pd.read_csv("thyroidDF.csv")
data = data.drop('patient_id', axis=1)
data['on_thyroxine'] = data['on_thyroxine'].replace({'t': 1.0, 'f': 0.0})
data['query_on_thyroxine'] = data['query_on_thyroxine'].replace({'t': 1.0, 'f': 0.0})
data['hypopituitary'] = data['hypopituitary'].replace({'t': 1.0, 'f': 0.0})
data['on_antithyroid_meds'] = data['on_antithyroid_meds'].replace({'t': 1.0, 'f': 0.0})
data['sick'] = data['sick'].replace({'t': 1.0, 'f': 0.0})
data['pregnant'] = data['pregnant'].replace({'t': 1.0, 'f': 0.0})
data['thyroid_surgery'] = data['thyroid_surgery'].replace({'t': 1.0, 'f': 0.0})
data['I131_treatment'] = data['I131_treatment'].replace({'t': 1.0, 'f': 0.0})
data['query_hypothyroid'] = data['query_hypothyroid'].replace({'t': 1.0, 'f': 0.0})
data['query_hyperthyroid'] = data['query_hyperthyroid'].replace({'t': 1.0, 'f': 0.0})
data['lithium'] = data['lithium'].replace({'t': 1.0, 'f': 0.0})
data['goitre'] = data['goitre'].replace({'t': 1.0, 'f': 0.0})
data['tumor'] = data['tumor'].replace({'t': 1.0, 'f': 0.0})
data['psych'] = data['psych'].replace({'t': 1.0, 'f': 0.0})
data['TSH_measured'] = data['TSH_measured'].replace({'t': 1.0, 'f': 0.0})
data['T3_measured'] = data['T3_measured'].replace({'t': 1.0, 'f': 0.0})
data['TT4_measured'] = data['TT4_measured'].replace({'t': 1.0, 'f': 0.0})
data['T4U_measured'] = data['T4U_measured'].replace({'t': 1.0, 'f': 0.0})
data['FTI_measured'] = data['FTI_measured'].replace({'t': 1.0, 'f': 0.0})
data['TBG_measured'] = data['TBG_measured'].replace({'t': 1.0, 'f': 0.0})

data['sex'] = data['TBG_measured'].replace({'F': 1.0, 'M': 0.0})

data = data.drop('referral_source', axis=1)
data = data.fillna(0)
data2 = data
#usunięcie danych aby było proporcjolanie chory/zdrowy 
#data wiekszy % zdrowych 65/35
#data2 mniejszy % zdrowych 45/55
for i in range(0,2500):
   if data['target'][i] == "-":
      data = data.drop(i, axis=0)


for i in range(0,6000):
   if data2['target'][i] == "-":
      data2 = data2.drop(i, axis=0)


print(data2['target'].value_counts()[0]/len(data2))
# print(data2)
# print(data)
# print(data['target'].value_counts()[0]/len(data))


