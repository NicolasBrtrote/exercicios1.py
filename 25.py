import numpy as np

array = np.random.randint(1, 11, size=(4, 3))

soma_total = np.sum(array)

linha_produto = np.prod(array, axis=1)