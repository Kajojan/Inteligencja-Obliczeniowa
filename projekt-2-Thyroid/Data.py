import re
import pandas as pd


data=pd.read_csv("thyroidDF.csv")
data = data.drop('patient_id', axis=1)
# print(data)
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

data['sex'] = data['sex'].replace({'F': 1.0, 'M': 0.0})

rs_encoder = { 'other' : 0, 'SVI' : 1, 'SVHC' : 2, 'STMW' : 3, 'SVHD' : 4, 'WEST' : 5}
data['referral_source'] = data['referral_source'].map(rs_encoder)

pattern = re.compile(r'([A-T])([A-T])')
data['target'] = data['target'].apply(lambda x: pattern.sub(r'\2', x))
pattern = re.compile(r'([A-T])[|]([A-T])')
data['target'] = data['target'].apply(lambda x: pattern.sub(r'\2', x))


diagnoses = {'-':"negative",
            'A': 'hyperthyroid', 
             'B': 'hyperthyroid', 
             'C': 'hyperthyroid', 
             'D': 'hyperthyroid',
             'E': 'hypothyroid', 
             'F': 'hypothyroid', 
             'G': 'hypothyroid', 
             'H': 'hypothyroid',
             "J": 'binding protein',
             "I": 'binding protein',
             "K" :'general health',
             "L" : 'replacement therapy',
             "M" : 'replacement therapy',
             "N" : 'replacement therapy',
             "O":'antithyroid treatment',
             "P":'antithyroid treatment',
             "Q":'antithyroid treatment',
             "R":'miscellaneous',
             "S":'miscellaneous',
             "T":'miscellaneous'}

data['target'] = data['target'].map(diagnoses) # re-mapping
data = data.fillna(0)


data2 = data
#usunięcie danych aby było proporcjolanie chory/zdrowy 
#data wiekszy % zdrowych 65/35
#data2 mniejszy % zdrowych 45/55
for i in range(0,1500):
   if data['target'][i] == "negative":
      data = data.drop(i, axis=0)


for i in range(0,5300):
   if data2['target'][i] == "negative":
      data2 = data2.drop(i, axis=0)

