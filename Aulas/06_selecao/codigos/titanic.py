import  pandas as pd

df = pd.read_csv('titanic.csv')
# df = pd.read_excel('titanic.xlsx', sheet_name='nome_aba_da_planilha')


#print(df.head(5)) # mostra as 5 primeiras linhas do DataFrame


df = df.rename(columns={
    'PassengerId': 'ID',
    'Survived': 'Sobreviveu',
    'Pclass': 'Classe',
    'Name': 'Nome',
    'Sex': 'Sexo',
    'Age': 'Idade',
    'SibSp': 'SibSp',
    'Parch': 'Parch',
    'Ticket': 'Bilhete',
    'Fare': 'tarifa',
    'Cabin': 'Cabine',
    'Embarked': 'Embarcou'
})

# print(df.head(5))
#df.columns = ['ID', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade', 'SibSp', 'Parch', 'Bilhete', 'tarifa', 'Cabine', 'Embarcou']

#print(df.columns.to_list())

#print(df[['Nome', 'Idade', 'Sexo']])


#print(df.iloc[1]) # Acessa a primeira linha (index 0) e a quarta coluna (index 3) do DataFrame, que corresponde ao nome do primeiro passageiro.

print(df.iloc[:, 0:3])


maiores_de_30 = df[df['Idade'] > 30]
print(maiores_de_30[['Nome', 'Idade']])
