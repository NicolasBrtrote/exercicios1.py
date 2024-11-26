import numpy as np
import matplotlib.pyplot as plt

alturas = np.random.normal(loc=170, scale=10, size=100)

percentil_25 = np.percentile(alturas, 25)
mediana = np.percentile(alturas, 50)
percentil_75 = np.percentile(alturas, 75)

print(percentil_25)
print(mediana)
print(percentil_75)

acima_180 = np.sum(alturas > 180)
print(acima_180)

plt.hist(alturas, bins=10, edgecolor='black', alpha=0.7)
plt.title('Histograma')
plt.xlabel('Altura em cm')
plt.ylabel('Frequência')
plt.show()