
# Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# Можно убедиться, что сумма чисел в диагоналях равна 101.

# Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способо


import time

############# СПОСОБ 1 ##########################

def create_matrix(a,b):
    return [ [0 for _ in range(a)] for _ in range(b)]

def rotate_matrix(mt):  # left-rotate
    res = [ [mt[a][b] for a in range(len(mt[b]))] for b in range(len(mt)-1, -1, -1)]
    return res

def print_mt(mt):
    if len(mt) > 19:
        return
    print('\t', '_'*len(mt)*5)
    for row in mt:
        print('\t',end='|')
        for col in row:
            print(f'{col:^5d}', end='')
        print('', end='|')
        print()
    print('\t', '-'*len(mt)*5)
    print()

def load_matrix(mt):
    col = len(mt)//2
    row = len(mt[0])//2
    lst = [x for x in range(len(mt)*len(mt[0]),0,-1)]

    mt[row][col] = lst.pop()
    print_mt(mt)
    col += 1
    mt[row][col] = lst.pop()
    row += 1
    mt[row][col] = lst.pop()
    mt = rotate_matrix(mt)
    mt = rotate_matrix(mt)

    st_x, st_y = -1, -1
    col, row = (len(mt)//2)+st_x, (len(mt[0])//2)+st_y
    rotate_index = 0
    while len(lst) > 0:
        # print_mt(mt)
        col += 1
        mt[row][col] = lst.pop()
        # print_mt(mt)
        if mt[row+1][col] == 0:
            mt = rotate_matrix(mt)
            rotate_index += 1
            if rotate_index == 3:
                st_y -= 1
            elif rotate_index == 4:
                rotate_index = 0
                st_x -= 1
            col, row = len(mt)//2+st_x, len(mt[0])//2+st_y
        continue
    return mt

def sum_diag(mt):
    start = time.time()
    res = sum([ mt[x][x] for x in range(len(mt))])
    res += sum([ mt[x][y] for y, x in enumerate(range(len(mt)-1,-1,-1)) ] )-1
    print(f'Подсчет диаганалей в матрице занял {time.time() - start} секунд')
    return res

############# СПОСОБ 2 ##########################

def sum_diag2(a: int):
    '''
    the sum of the numbers on the diagonals in spiral is formed
    param: a: int - размерность массива
    return: int
    '''
    start = time.time()
    lst = [x for x in range(1, a*a+1)]

    index_boom = 2
    index = 0
    res = 0
    res += lst[index]
    while index < len(lst):
        for i in range(4):
            index += index_boom
            res += lst[index]
        index_boom += 2
        if index + index_boom > len(lst):
            break
    return res

def main(a,b, algorithm=2):
    if algorithm == 1:
        mt = create_matrix(a,b)
        mt = load_matrix(mt)
        print_mt(mt)
        return sum_diag(mt)
    else:
        return sum_diag2(a)


if __name__ == "__main__":
    a,b = 1001,1001
    start = time.time()
    ans = main(a,b,algorithm=2)  # по первому алгоритму будет работать секунд 300
    total = time.time() - start
    print(f'Ответ: {ans}\nВремени заняло: {total}')


# Ответ: 669171001
# Времени заняло: 0.13191771507263184
