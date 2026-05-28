import pandas as pd

dados_alunos = {   
                "Nome": ['Ana', 'Bruno', 'Carla'],
                "Notas": [9.5, 7, 8.2],
                "faltas": [2, 0, 5]}

df_alunos = pd.DataFrame(dados_alunos)
x = df_alunos.iloc[1,0]

print(x)