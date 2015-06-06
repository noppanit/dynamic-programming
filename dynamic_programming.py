import sys
coins = [1, 3, 5]
min_coin = [sys.maxint] * 20
min_coin[0] = 0

for min_of_i in range(20):
    for coin in coins:
        if coin <= min_of_i and (min_coin[min_of_i - coin] + 1 < min_coin[min_of_i]):
                min_coin[min_of_i] = min_coin[min_of_i - coin] + 1


print min_coin
