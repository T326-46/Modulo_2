import pandas as pd

df = pd.read_csv('funcionarios.csv')

# Filtro simples — Boolean Indexing

# Numérico — maior que
print("Idade > 25:")
print(df[df['idade'] > 25])

# Numérico — maior ou igual
print("\nSalário >= 3000:")
print(df[df['salario'] >= 3000])

# Texto — igual a
print("\nCidade == Fortaleza:")
print(df[df['cidade'] == 'Fortaleza'])

# Texto — diferente de
print("\nCargo != Estagiario:")
print(df[df['cargo'] != 'Estagiario'])


# Operadores lógicos — AND, OR e NOT

# AND (&) — ambas as condições devem ser verdadeiras
print("\nIdade > 25 AND cidade == Natal:")
print(df[(df['idade'] > 25) & (df['cidade'] == 'Natal')])

# OR (|) — pelo menos uma condição deve ser verdadeira
print("\nCidade == Fortaleza OR cidade == Recife:")
print(df[(df['cidade'] == 'Fortaleza') | (df['cidade'] == 'Recife')])

# NOT (~) — inverte a condição
print("\nNOT cidade == Fortaleza:")
print(df[~(df['cidade'] == 'Fortaleza')])


# Múltiplas condições

# Duas condições AND
print("\nIdade > 25 AND cidade == Fortaleza:")
print(df[(df['idade'] > 25) & (df['cidade'] == 'Fortaleza')])

# Duas condições OR
print("\nSalário > 5000 OR cargo == Gerente:")
print(df[(df['salario'] > 5000) | (df['cargo'] == 'Gerente')])

# Três condições AND
print("\nIdade >= 18 AND ativo == True AND salário > 2000:")
print(df[(df['idade'] >= 18) & (df['ativo'] == True) & (df['salario'] > 2000)])

# Salvando máscaras em variáveis antes de combinar
mask1 = df['idade'] > 25
mask2 = df['cidade'] == 'Fortaleza'
print("\nMáscaras combinadas (idade > 25 AND cidade == Fortaleza):")
print(df[mask1 & mask2])


# Método .query() — sintaxe similar ao SQL

print("\n.query() — idade > 25 and cidade == Fortaleza:")
print(df.query('idade > 25 and cidade == "Fortaleza"'))

# Usando variável externa com @
idade_min = 25
print("\n.query() com variável @idade_min:")
print(df.query('idade > @idade_min'))


# Filtros de string (.str)

# Verifica se contém o texto
print("\nNome contém 'Silva':")
print(df[df['nome'].str.contains('Silva')])

# Verifica se começa com o texto
print("\nCidade começa com 'For':")
print(df[df['cidade'].str.startswith('For')])

# Verifica se o valor está em uma lista
cidades = ['Fortaleza', 'Recife']
print("\nCidade está em ['Fortaleza', 'Recife']:")
print(df[df['cidade'].isin(cidades)])


# Parte prática — combinando todos os filtros

# Filtro de string com case=False e na=False
print("\nNome contém 'silva' (sem distinção de maiúsculas):")
print(df[df['nome'].str.contains('silva', case=False, na=False)])

# Filtro por lista
print("\nCidade em ['Fortaleza', 'Recife', 'Natal']:")
print(df[df['cidade'].isin(['Fortaleza', 'Recife', 'Natal'])])

# Encadeando dois .query()
print("\nIdade > 18 AND salário >= 2000 AND cidade != Natal:")
print(df.query('idade > 18 and salario >= 2000').query('cidade != "Natal"'))
