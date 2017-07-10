import numpy as np

def reduce_payment_matrix(payment_matrix):
    def custom_unique(array):
        b = np.ascontiguousarray(array).view(np.dtype((np.void, array.dtype.itemsize * array.shape[1])))
        _, idx = np.unique(b, return_index=True)
        return array[idx]

    def delete_matrix_row(payment_matrix, operation):
        item_index = None
        for index, value in enumerate(payment_matrix):
            for sub_index, sub_value in enumerate(payment_matrix):
                if index != sub_index:
                    if operation(value, sub_value).all():
                        item_index = index
                        break
            else:
                continue
            break
        return np.delete(payment_matrix, item_index, 0) if item_index != None else None
    
    def main_reduce(payment_matrix, operation):
        new_matrix = custom_unique(payment_matrix)[::-1]
        while True:
            temp_matrix = delete_matrix_row(new_matrix, operation)
            if np.all(temp_matrix) != None:
                new_matrix = temp_matrix
            else:
                break
        return new_matrix
    
    new_matrix = payment_matrix
    while True:
        old_matrix = new_matrix
        new_matrix = main_reduce(new_matrix, np.less_equal)
        new_matrix = main_reduce(new_matrix.transpose(), np.greater_equal)
        new_matrix = new_matrix.transpose()
        if np.all(old_matrix == new_matrix):
            break
    return payment_matrix if np.shape(new_matrix) == np.shape(payment_matrix) else new_matrix

payment_matrix = np.array([
    [8, 9, 9, 4],
    [6, 5, 8, 7],
    [3, 4, 8, 6],
    [8, 9, 9, 4]
])
payment_matrix = np.array([
    [4, 5, 6, 7],
    [3, 4, 6, 5],
    [7, 6, 10, 8],
    [8, 5, 4, 3]
])
payment_matrix = np.array([
    [8, 6, 4, 7, 7],
    [5, 4, 3, 4, 6],
    [4, 3, 2, 3, 4],
    [7, 2, 6, 5, 9]
])
payment_matrix = np.array([
    [16974, 18467, 12496],
    [-8483, -8488, -8469],
])

print(reduce_payment_matrix(payment_matrix))
