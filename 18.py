import numpy as np

coeficientes = [1, -4, 6, -24]

raizes = np.roots(coeficientes)


valor_de_x = 2
polinomio_x = np.polyval(coeficientes, valor_de_x)