import itertools
import numpy as np
import matplotlib.pyplot as plt 
from shapely.geometry import LineString

def graphic_method(payment_matrix, ctx):
    def solve(payment_matrix):
        precision = 0.0001
        result_list = []
        for pair in itertools.combinations(payment_matrix[0], 2):
            index = 0
            first_index = int(*np.where(payment_matrix[0]==pair[0]))
            second_index = int(*np.where(payment_matrix[0]==pair[1]))
            temp1 = payment_matrix[:,first_index]
            temp2 = payment_matrix[:,second_index]
            x, y = LineString([(0, temp1[0]), (1, temp1[1])]).intersection(LineString([(0, temp2[0]), (1, temp2[1])])).xy
            for line in payment_matrix.transpose():
                try:
                    LineString([(0, line[0]), (1, line[1])]).intersection(LineString([(x[0], y[0]-precision), (x[0], 0)])).xy
                    index += 1
                except NotImplementedError:
                    continue
            if index == 0:
                result_list.append([y[0], x[0], first_index, second_index])
        return sorted(result_list)[-1]
        
    def draw(payment_matrix, first_line, second_line, x, y, ctx):
        ctx.plot(payment_matrix, color='gray')
        ctx.plot(first_line, color='r')
        ctx.plot(second_line, color='r')
        ctx.plot(x, y, 'o', color='black', zorder=2)
        ctx.plot([x, x], [y, 0], 'r--', color='r')
        ctx.plot([0, x], [0.2, 0.2], '--', color='b')
        ctx.plot([x, 1], [0.2, 0.2], '--', color='g')
        ctx.text(x/2, 0.3, 'p2 = '+str(x)[:4])
        ctx.text(x+(1-x)/2, 0.3, 'p1 = '+str(1-x)[:4])
        ctx.title('Game price = {}'.format(str(y)[:4]))
        ctx.show()
        
    result = solve(payment_matrix)
    draw(payment_matrix, payment_matrix[:,result[2]], payment_matrix[:,result[3]], result[1], result[0], ctx)
    
payment_matrix = np.array([
    [4, 3, 6],
    [5, 7, 2]
])
payment_matrix = np.array([
    [7, 12],
    [10, 9]
])
payment_matrix = np.array([
    [6, 8, 1, 2],
    [2, 1, 8, 6]
])
graphic_method(payment_matrix, plt)

