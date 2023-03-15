import pandas as pd
import matplotlib.pyplot as plt

miasta=pd.read_csv("lab01/miasta.csv")
miasta.loc[10]=[2010,460,555,405]

print(miasta)


plt.plot(miasta["Rok"],miasta["Gdansk"], '-ro')
plt.ylabel("Ludności")
plt.xlabel("Lata")
plt.show()

plt.plot(miasta["Rok"],  miasta["Gdansk"], "-ro" , miasta["Rok"],miasta["Poznan"], "-bs", miasta["Rok"],miasta["Szczecin"], '-g^' )
plt.ylabel("ludność")
plt.xlabel("Lata")
plt.legend()
# plt.show()


def standaryzacja(n):
    helper=n
    for i in n.columns:
        for j in range(0,len(n[i])):
            if(i != "Rok"):
                mean=sum(n[i])/len(n[i])
                std=n[i].std()
                helper.at[j, i]=((n[i][j]-mean)/std)
                

                
    return helper

miastaPoStandaryzacji=standaryzacja(miasta)
print(miastaPoStandaryzacji)

for i in miastaPoStandaryzacji.columns:
        if(i != "Rok"):
            mean=sum(miastaPoStandaryzacji[i])/len(miastaPoStandaryzacji[i])
            std=miastaPoStandaryzacji[i].std()
            print(i, "mean:" ,mean,"std: ", std)
                

def normalizacja(n):
    helper=n
    for i in n.columns:
        for j in range(0,len(n[i])):
            if(i != "Rok"):
                helper.at[j, i]=((n[i][j]-min(n[i]))/max(n[i])-min(n[i]))
                

                
    return helper

miastaPoNormalizacji=normalizacja(miasta)
print(miastaPoNormalizacji)

for i in miastaPoNormalizacji.columns:
        if(i != "Rok"):
            print(i, "min:" ,min(miastaPoNormalizacji[i]),"max: ", max(miastaPoNormalizacji[i]))
                