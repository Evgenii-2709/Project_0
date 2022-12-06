"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def random_predict_opti(number: int = 1) -> int:
    """Рандомно угадываем число по оптимизированному алгоритму.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    list_value = [] # список отсечения
    list_value.extend(range(1, 101)) # инициализация списка для отсечения
    count = 0    
    #print("задумали {}".format(number), end='\t')
    
    while len(list_value) > 1:
        count += 1
        predict_index = np.random.randint(1, len(list_value) )  # предполагаемый индекс для списка отсечения
        #print("[{}]={}".format(predict_index, list_value[predict_index-1]), end='\t')
     
        if number == list_value[predict_index-1] :
            break  # выход из цикла если угадали
        elif number < list_value[predict_index-1] :
            list_value = list_value[ :predict_index] # если число меньше, укорачиваем список отсечения <-
        else :
            list_value = list_value[predict_index: ] # если число больше, укорачиваем список отсечения ->
    
    #print("угадали {} кол-во {}".format( list_value[(predict_index-1) if len(list_value) > 1 else 0], count))
    return count

def predict_1_2(number: int = 1) -> int:
    """угадываем число по оптимизированному алгоритму делением диапазона на 2.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    min_value = 1 # стартовая минимальная границ
    max_value = 101 # стартовая максимальная граница    
    count = 0    
    #print("задумали {}".format(number), end='\t')
    
    while True:
        count += 1
        cur_value = min_value + int((max_value - min_value)/ 2)  # предполагаемый индекс для списка отсечения
        #print("[{}]={}".format(count, cur_value), end=' ')
     
        if number == cur_value :
            break  # выход из цикла если угадали
        elif number < cur_value :
            max_value = cur_value # если число меньше, уменьшаем верхнюю границу
        else :
            min_value = cur_value  # если число больше, увеличиваем нижнюю границу                        
        #print("{}<->{}".format(min_value, max_value), end='; ')
    
    #print("угадали {} кол-во {}".format( cur_value, count))
    return count


def score_game(func_calc) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint( 1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(func_calc(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(predict_1_2)
