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