# Surprisingly there are only three numbers that can be
# written as the sum of fourth powers of their digits:

# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.

# The sum of these numbers is 1634 + 8208 + 9474 = 19316.

# Find the sum of all the numbers that can be written as
# the sum of fifth powers of their digits.
import time

def sl(min_range, max_range, power):
    res = []
    for i in range(min_range, max_range):
        s = sum([int(x)**power for x in list(str(i))])
        # print(i, s)
        if i == int(s):
            res.append(i)
    return res


if __name__ == "__main__":
    start = time.time()
    ans = sl(2,1000000,5)
    total = time.time() - start
    print(ans)
    print(f'Ответ: {sum(ans)}\nВыполнено за {total} сек')


# Ответ: 443839
# Выполнено за 6.126229286193848 сек
