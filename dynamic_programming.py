import sys

def get_min_coins(coins, target_amount):
    n = len(coins)
    min_coins = [0] + [sys.maxint] * target_amount
    for i in range(1, n + 1):
        for j in range(coins[i - 1], target_amount + 1):
            min_coins[j] = min(min_coins[j - coins[i - 1]] + 1, min_coins[j])
    return min_coins

print get_min_coins([1,3,5], 11)
