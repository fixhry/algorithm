from utils import *


def coin_change(n, cache=None):
    if cache is None:
        cache = {}

    coin_list = [1, 2, 5, 8, 13]
    coins = []
    if n == 0:
        return coins
    else:
        # 子问题
        for i in coin_list:
            if i <= n:
                cs = [i]
                # 先判断在不在缓存中
                cached = cache.get(n, None)
                if cached:
                    log('coin_change use cache', n)
                    tmp = cached
                else:
                    tmp = coin_change(n - i, cache)
                cs += tmp
                l1 = len(cs)
                l2 = len(coins)
                if l2 == 0 or l1 < l2:
                    coins = cs
            else:
                break
        # 缓存这一次求值的结果
        cache[n] = coins
        return coins


# 割钢条
def cut_rod(n, cache=None):
    if cache is None:
        cache = {}

    limit = 10
    price_list = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

    # 割 0 次就等于自己的价格
    if n <= limit:
        price = price_list[n]
    else:
        price = 0
    if n == 0:
        return price
    i = 1
    while i <= limit:
        j = n
        # 价格
        p = 0
        # 第一段价格
        p1 = price_list[i]
        p += p1
        if j >= i:
            j -= i
            # 剩下的最优价格
            p2 = cache.get(j, None)
            if p2 is None:
                log('cut_rod use cache', n)
                p2 = cut_rod(j, cache)
            p += p2
            if p > price:
                price = p
        else:
            break
        i += 1
    cache[n] = price
    return price


if __name__ == '__main__':
    r2 = coin_change(2)
    r3 = coin_change(3)
    r4 = coin_change(4)
    r5 = coin_change(5)
    r6 = coin_change(6)
    r100 = coin_change(100)
    log(r2)
    log(r3)
    log(r4)
    log(r5)
    log(r6)
    log(r100)

    a1 = cut_rod(1)
    a2 = cut_rod(2)
    a3 = cut_rod(3)
    a4 = cut_rod(4)
    a5 = cut_rod(5)
    a6 = cut_rod(6)
    log(a1)
    log(a2)
    log(a3)
    log(a4)
    log(a5)
    log(a6)
    a100 = cut_rod(100)
    log(a100)
