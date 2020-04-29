def game_core_v3(number):
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