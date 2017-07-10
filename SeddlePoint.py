import numpy as np

def get_seddle_point(payment_matrix):
    lower_price = payment_matrix.min(axis=1)
    upper_price = payment_matrix.max(axis=0)
    seddle_point = np.intersect1d(lower_price, upper_price)
    return int(seddle_point) if seddle_point else None

payment_matrix = np.array([
    [8, 7, 0, 6],
    [6,	8, 5, 10]
])
'''# payment matrix without seddle point
payment_matrix = np.array([
    [16974, -23326, 12496],
    [-8483, -8351, -8469]
])'''

print(get_seddle_point(payment_matrix))
