import pandas as pd


df = pd.read_csv('funcionarios.csv')


# Métodos básicos de agregação

# Média salarial
print(df['salario'].mean())

# Soma total de vendas
print(df['vendas'].sum())

# Maior salário
print(df['salario'].max())

# Menor salário
print(df['salario'].min())

# Contagem de valores não nulos
print(df['salario'].count())


# Contando valores únicos — .value_counts()

# Frequência de cada cidade
print(df['cidade'].value_counts())

# Frequência em proporção percentual
print(df['cidade'].value_counts(normalize=True))


# Resumo estatístico completo — .describe()

print(df['salario'].describe())


# Agrupamento com groupby()

# Média salarial por cidade
print(df.groupby('cidade')['salario'].mean())

# Total de vendas por cargo
print(df.groupby('cargo')['vendas'].sum())

# Contagem de funcionários por cidade
print(df.groupby('cidade')['nome'].count())


# Agregações múltiplas com .agg()

# Média, máximo e mínimo salarial por cargo
print(df.groupby('cargo')['salario'].agg(['mean', 'max', 'min']))


# Parte prática — combinando todas as agregações

# Métodos básicos na coluna salário
print(df['salario'].mean())
print(df['salario'].sum())
print(df['salario'].max())
print(df['salario'].min())

# Frequência de cidades
print(df['cidade'].value_counts())

# Resumo estatístico completo
print(df['salario'].describe())

# Agrupamento: média salarial por cidade
print(df.groupby('cidade')['salario'].mean())

# Agrupamento com múltiplas funções
print(df.groupby('cargo')['salario'].agg(['mean', 'max', 'min']))
