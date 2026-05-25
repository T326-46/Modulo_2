import pandas as pd

df = pd.read_csv('funcionarios.csv')

# Renomeando colunas — sintaxe básica 

# Renomear uma coluna (sem inplace, retorna novo DataFrame)
resultado = df.rename(columns={'nome': 'nome_funcionario'})
print("Renomear uma coluna:")
print(resultado.columns.tolist())

# Renomear múltiplas colunas de uma vez
resultado = df.rename(columns={
    'nome': 'Nome',
    'idade': 'Idade',
    'cidade': 'Cidade'
})
print("\nRenomear múltiplas colunas:")
print(resultado.columns.tolist())

# Renomear com inplace=True (modifica o DataFrame diretamente)
df.rename(columns={'nome': 'Nome'}, inplace=True)
print("\nApós inplace=True:")
print(df.columns.tolist())

# Padronizar nomes de colunas para minúsculas e substituir espaços por underscore
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ', '_')
print("\nColunas padronizadas (lower + underscore):")
print(df.columns.tolist())

# Renomear pelo índice das linhas
resultado = df.rename(index={0: 'primeiro', 1: 'segundo'})
print("\nRenomear índice das linhas:")
print(resultado.index.tolist())


# Reordenando e selecionando colunas

# Selecionar uma coluna (retorna Series)
print("\nUma coluna (Series):")
print(df['nome'])

# Selecionar múltiplas colunas (retorna DataFrame)
print("\nMúltiplas colunas (DataFrame):")
print(df[['nome', 'idade', 'salario']])

# Reordenar todas as colunas usando uma lista com nova ordem
nova_ordem = ['cidade', 'nome', 'salario']
df_reordenado = df[nova_ordem]
print("\nColunas reordenadas:")
print(df_reordenado.columns.tolist())

# Remover uma coluna com .drop()
resultado = df.drop(columns=['cargo'])
print("\nApós remover 'cargo':")
print(resultado.columns.tolist())

# Remover múltiplas colunas com .drop()
resultado = df.drop(columns=['cargo', 'ativo'])
print("\nApós remover 'cargo' e 'ativo':")
print(resultado.columns.tolist())


# Criando colunas derivadas 

# Calcular salário anual a partir do salário mensal
df['salario_anual'] = df['salario'] * 12
print("\nSalário anual:")
print(df[['nome', 'salario', 'salario_anual']])

# Criar coluna de nome completo concatenando nome e sobrenome
df['nome_completo'] = df['nome'] + ' ' + df['sobrenome']
print("\nNome completo:")
print(df[['nome', 'sobrenome', 'nome_completo']])

# Classificar funcionários por nível salarial usando apply e lambda
df['nivel'] = df['salario'].apply(lambda x: 'Alto' if x > 5000 else 'Baixo')
print("\nNível salarial:")
print(df[['nome', 'salario', 'nivel']])

# Calcular bônus multiplicando salário pelo percentual de bônus
df['bonus'] = df['salario'] * df['perc_bonus']
print("\nBônus calculado:")
print(df[['nome', 'salario', 'perc_bonus', 'bonus']])


# Parte prática — organizando um dataset completo 

df = pd.read_csv('funcionarios.csv')

# Ver nomes das colunas atuais
print("\nColunas originais:")
print(df.columns.tolist())

# Renomear colunas para padronizar
df.rename(columns={
    'nome': 'Nome',
    'idade': 'Idade',
    'cidade': 'Cidade',
    'salario': 'Salario'
}, inplace=True)

# Reordenar colunas
df = df[['Nome', 'Cidade', 'Idade', 'Salario']]

# Criar coluna derivada de salário anual
df['Salario_Anual'] = df['Salario'] * 12

# Remover coluna desnecessária
df.drop(columns=['Idade'], inplace=True)

print("\nDataset final organizado:")
print(df)
