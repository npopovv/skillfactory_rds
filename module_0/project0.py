<<<<<<< HEAD
def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
=======
def game_core_v3(number):
    '''Каждый раз при угадывании выбрасывается часть, в которой точно нет нужного числа'''
    predict = np.random.randint(1,101)
    count = 1
    a=1
    b=101
    while number != predict:
        if number > predict:
            a = predict
        else:
            b = predict
        predict = np.random.randint(a,b)
        count+=1
    return count
   from math import ceil
def game_core_v4(number):
    """При каждой итеграции в цикле while смещаются границы возможного нахождения числа, если границы совпали
    -значит, угадываемое числа - одна из границ"""
    bottom = 0
    top = 100
    count = 1
    while bottom != top:
        sep = number - bottom
        half = ceil((top-bottom)/2)
        if sep > half:
            bottom += half
        elif sep < half:
            top -= half
        elif sep == half:
            bottom = bottom + sep
    predict = bottom
    while predict != number:
        predict += 1
        count += 1
    return count
>>>>>>> test
