def cost_performance(c_1, p_1, c_2, p_2):
    drink1 = c_1 / p_1
    drink2 = c_2 / p_2

    if drink1 > drink2:
        return 1
    else:
        return 2


c_1, p_1 = map(int, input().split())
c_2, p_2 = map(int, input().split()) 

result = cost_performance(c_1, p_1, c_2, p_2)
print(result)
