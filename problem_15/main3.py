
import sys


GRID= (12,13)

def get_routes(point_x,point_y):
    # print(f"get_routes(point_x = {point_x},point_y = {point_y})")
    res = ''
    if point_x == GRID[0]-1 and point_y < GRID[1]-1: res = 'down' #Только вниз
    elif point_y == GRID[1]-1 and point_x < GRID[0]-1: res = 'right' #Только вправо
    elif point_x == GRID[0]-1 and point_y == GRID[1]-1 : res = 'No' #Путей нет
    else: res = 'both' # Вниз и вправо
    # print("have route: ",res)
    return res


def add_who_need(point_x,point_y,grid,tbl,r):
    """
    получает точку текущего положения курсора, саму таблицу и результирующую, направления
    """
    tmp = tbl[grid[point_y][point_x]][:]
    if r == 'both':
        for i in range(len(tmp)):
            tmp.append(tmp[i][:])
        next_point1 = grid[point_y][point_x + 1]
        next_point2 = grid[point_y+1][point_x]
        next_point = next_point1

        for i in range(len(tmp)):
            tmp[i].append(next_point)

            if next_point == next_point1:
                next_point = next_point2
            else:
                next_point = next_point1

    elif r == 'right':
        for i in range(len(tmp)):
            tmp[i].append(grid[point_y][point_x + 1])
    elif r == 'down':
        for i in range(len(tmp)):
            tmp[i].append(grid[point_y+1][point_x])
    else:
        print(f"Больше нет места для движения все маршруты готовы, количество маршрутов {len(tbl[GRID[0]*GRID[1]-1])}")
        sys.exit("The happy end")



    for i in range(len(tmp)):
        k = tmp[i][-1]
        if not (k in tbl.keys()):
            tbl[k] = []
        tbl[k].append(tmp[i])

    del(tbl[grid[point_y][point_x]])

    return tbl



# def id_needed_lists(tabl,num):
#     # print(f"id_needed_lists <- {num}, {tabl}")
#     res = []
#     for i in range(len(tabl)):
#         if tabl[i][-1] == num:
#             res.append(i)
#     print(f"id_needed_lists -> len(res) = {len(res)}")
#     return res


def main():
    res = {0:[[0],]}
    grid = [[x + y*GRID[0] for x in range(GRID[0])] for y in range(GRID[1])] # Сама таблица - пока узел True через него можно идти, иначе идем через другой

    # for y in range(GRID[1]):
    #     for x in range(GRID[0]):
    #         grid[y][x] = x + y*GRID[0]

    print(grid)
    # return grid

    #memory_grid = [[0 for x in range(GRID[0])] for y in range(GRID[1])] #Сюда буду записывать интересные данные, типа сколько раз через каждый узел прошел
    # grid[0][2] = False
    for row in range(GRID[1]):
        if GRID//2 >= row:
            print(row, res)
        for col in range(GRID[0]):
            r = get_routes(col,row)
            res = add_who_need(col,row,grid,res,r)
            # print(res)
    return res


if __name__ == "__main__":
    main()






