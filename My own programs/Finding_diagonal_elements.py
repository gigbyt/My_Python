import numpy as np

array = np.arange(1,10).reshape(3,3)
diagonal_elements = np.diagonal(array)
print("3x3 Array:")
print(array)
print("\nDiagonal Element")
print(diagonal_elements)
