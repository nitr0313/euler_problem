
DIGS = (1,2,3,4,5,6,7,8,9,10) #2520
# DIGS = (11,12,13,14,15,16,17,18,19,20) #232792560

def check_num(num):

    for i in DIGS:
        if num%i != 0:
            return False
    return num


def product(lst):
    res = 1
    for i in lst:
        if i == 0:
            return 0
        res *= i
    return res


def main():
    lengs = 0
    for i in range(max(DIGS)**2, product(DIGS)):
        res = check_num(i)
        if len(str(i))>lengs:
            print(i)
            lengs = len(str(i))
        if res:
            return res

    return "Ничего не нашел"


if __name__ == "__main__":
    print(main())