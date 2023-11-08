def nonConstructibleChange(coins):
    change = 1
    coins.sort()
    if change in coins:
        for coin in coins:
            if coin >= change + 1:
                return change
            change += coin

    return change

def nonConstructibleChange(coins):
    coins.sort()
    change = 0

    for coin in coins:
        if coin > change + 1:
            return change + 1  # you can replace this with a break and will jump to the last line
        change += coin

    return change + 1


