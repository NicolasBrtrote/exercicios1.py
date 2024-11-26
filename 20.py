import numpy as np 

dados = np.random.rand(50, 3)

media = np.mean(dados, axis=0, )
desvio_padrao = np.std(dados, axis=0)

valor_min = np.min(dados)
valor_max = np.max(dados)

dados_normalizados = (dados - valor_min) / (valor_max - valor_min)
    
print("Médias:", media)
print("Desvios Padrão:", desvio_padrao)
print("Valores Máximos:", valor_max)
print("Valores Mínimos:", valor_min)
print("Dados Normalizados:\n", dados_normalizados)