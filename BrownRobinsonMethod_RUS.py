# -*- coding: utf-8 -*
# подключем модуль numpy с математическими операциями над матрицами
import numpy as np

# определяем точку входа в программу
def главная_функция():
    #  np.array - создаем экземпляр класса numpy.array [массив с дополнительными свойствами]
    платежная_матрица = np.array([
        [6, 1, 4],
        [2, 4, 2],
        [4, 3, 5]
    ])
    # присваиваем переменной результат работы функции-алгоритма с заданными параметрами
    результат = метод_брауна_робинсона(
        платежная_матрица,
        количество_итераций=20,
        номер_начальной_стратегии=0,
        вывод_итераций=True
    )
    # print - функция вывода данных в поток [консоль]
    print('\nЦена игры: W =', результат['цена_игры'])
    print('Оптимальная смешанная стратегия игрока A: P =', результат['оптимальная_смешанная_стратегия_игрока_a'])
    print('Оптимальная смешанная стратегия игрока B: Q =', результат['оптимальная_смешанная_стратегия_игрока_b'])

# функция которая реализует алгоритм Брауна-Робинсона
def метод_брауна_робинсона(платежная_матрица, количество_итераций=20, номер_начальной_стратегии=0, вывод_итераций=False):
    степень_округления = 2
    номер_текущей_стратегии_игрока_a = номер_начальной_стратегии
    # np.argmin - получаем индекс минимального елемента массива
    номер_текущей_стратегии_игрока_b = платежная_матрица[номер_текущей_стратегии_игрока_a].argmin()
    смешанные_стратегии_игрока_a = np.array(платежная_матрица[номер_текущей_стратегии_игрока_a])
    # [:,i] - получаем столбец из матрицы по индексу i
    смешанные_стратегии_игрока_b = np.array(платежная_матрица[:,номер_текущей_стратегии_игрока_b])
    # np.zeros - создаем массив заполненный нулями размером len(matrix)
    # len - функция, возвращающая длину массива
    частота_выбора_стратегий_игрока_a = np.zeros(len(платежная_матрица))
    частота_выбора_стратегий_игрока_b = np.zeros(len(платежная_матрица[0]))  
    
    # range - функция, возвращающая последовательность чисел от n до m с шагом s
    for номер_итерации in range(1, количество_итераций+1):
        частота_выбора_стратегий_игрока_a[номер_текущей_стратегии_игрока_a] += 1
        частота_выбора_стратегий_игрока_b[номер_текущей_стратегии_игрока_b] += 1
        # min - функция, возвращающая минимальный елемент массива
        нижняя_оценка_игры = min(смешанные_стратегии_игрока_a)/номер_итерации
        # max - функция, возвращающая максимальный елемент массива
        верхняя_оценка_игры = max(смешанные_стратегии_игрока_b)/номер_итерации
        if вывод_итераций:
            print(
                номер_итерации,
                номер_текущей_стратегии_игрока_a+1,
                смешанные_стратегии_игрока_a,
                номер_текущей_стратегии_игрока_b+1,
                смешанные_стратегии_игрока_b,
                # round - функция, округляющая число до заданной степени
                round(нижняя_оценка_игры, степень_округления),
                round(верхняя_оценка_игры, степень_округления),
                round((нижняя_оценка_игры+верхняя_оценка_игры)/2, степень_округления),
                # sep - параметр, задающий разделитель вывода в консоли
                sep=' | '
            )
        # np.argmax - получаем индекс максимального елемента массива
        номер_текущей_стратегии_игрока_a = смешанные_стратегии_игрока_b.argmax()
        смешанные_стратегии_игрока_a += платежная_матрица[номер_текущей_стратегии_игрока_a]
        номер_текущей_стратегии_игрока_b = смешанные_стратегии_игрока_a.argmin()
        смешанные_стратегии_игрока_b += платежная_матрица[:,номер_текущей_стратегии_игрока_b]
    
    # возвращаем ассоциативный массив [словарь]
    return {
        'цена_игры': (нижняя_оценка_игры+верхняя_оценка_игры)/2,
        # делим каждый елемент массива на число [перегруженный оператор деления /]
        'оптимальная_смешанная_стратегия_игрока_a': частота_выбора_стратегий_игрока_a/количество_итераций,
        'оптимальная_смешанная_стратегия_игрока_b': частота_выбора_стратегий_игрока_b/количество_итераций
    }

# вызываем точку входа
главная_функция()