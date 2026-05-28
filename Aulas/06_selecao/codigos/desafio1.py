import pandas as pd

dados = {   'Produto': ['Monitor', 'Teclado', 'Mouse'],    
            'Preço': [1200, 150, 80],   
            'Quantidade': [5, 10, 15]}

df = pd.DataFrame(dados)

resultado = df[['Produto', 'Quantidade']]
print(resultado)


