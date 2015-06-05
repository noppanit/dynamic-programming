coins = [1, 3, 5]
sum = []
sum.append(0)

for min_of_i in range(11):
    sum.append(1000)
    for coin in coins:
        if coin <= min_of_i and ( sum[min_of_i - coin] + 1 < sum[min_of_i] ):
                sum[min_of_i] = sum[min_of_i - coin] + 1


print sum
