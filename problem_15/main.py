import sys

GRID= (3,3)


def have_in_open_doors(x,y,grid):
    print(f"have_in_open_doors(x={x},y={y},grid)")
    # if x == 0 and y ==0:
    #     return False, False
    # elif x > 0 and y > 0:
    #     return grid[y][x-1],grid[y-1][x]
    # elif x > 0 and y == 0:
    #     return grid[y][x-1],False
    # elif x == 0 and y > 0:
    #     return False,grid[y-1][x]
    # else:
    #     print(f'Неизвестное содержание параметра x= {x}, y= {y}: ')
    #     sys.exit("Error")
    print(grid)
    res = True,True,2
    if x == 0 and y ==0:
        res = res
    elif x > 0 and y > 0:
        res = grid[y][x-1],grid[y-1][x], 2 if grid[y][x-1] and grid[y-1][x] else 1
    elif x > 0 and y == 0:
        res = grid[y][x-1],False, 1 if grid[y][x-1] or grid[y-1][x] else 0
    elif x == 0 and y > 0:
        res = False,grid[y-1][x], 1 if grid[y][x-1] or grid[y-1][x] else 0
    else:
        print(f'Неизвестное содержание параметра x= {x}, y= {y}: ')
        sys.exit("Error")
    return res #True если входов нет вообще или входов 2, иначе False
    pass

def have_out_open_door(x,y,route,grid):
    print(f"have_out_open_door(x={x},y={y},route={route},grid)")
    print(grid)
    if route =='down':
        # print("have door down?")
        return None,grid[y+1][x],1
    elif route == 'right':
        # print("have door right?")
        return grid[y][x+1],None,1
    elif route == 'both':
        # print("have both door?")
        return grid[y][x+1],grid[y+1][x], 2 if grid[y][x+1] and grid[y+1][x] else 1
    else:
        print('Неизвестное содержание параметра route: ', route)
        sys.exit("Error")

    pass

def get_routes(point_x,point_y):
    print(f"get_routes(point_x = {point_x},point_y = {point_y})")
    res = ''
    if point_x == GRID[0]-1 and point_y < GRID[1]-1: res = 'down' #Только вниз
    elif point_y == GRID[1]-1 and point_x < GRID[0]-1: res = 'right' #Только вправо
    elif point_x == GRID[0]-1 and point_y == GRID[1]-1 : res = 'No' #Путей нет
    else: res = 'both' # Вниз и вправо
    print("have route: ",res)
    return res


def move(x,y,grid,mgrid): # Нужен еще counter когда нет путей
    print(f"move(x={x},y={y},grid,mgrid)")
    mgrid[y][x] += 1 # Зашли в узел добавили проход по нему
    print(mgrid)
    r = get_routes(x,y)
    ### ЕСЛИ ВХОД 1 и ВЫХОД 1 - закрываем узел have_in_open_doors
    if r == 'No':
        return grid,mgrid
    if r == 'both':
        ans_1 = have_out_open_door(x,y,r, grid)
        if (ans_1[2] == 1 and have_in_open_doors(x,y,grid)[2] != 2) or (have_in_open_doors(x,y,grid)[2] == 0): # 1 вход и выход закр
            grid[y][x] = False
        if ans_1[0]: # Есть дорога вправо?
            move(x+1,y,grid,mgrid)
        elif ans_1[1]:
            move(x,y+1,grid,mgrid)
        else:
            print(grid)
            sys.exit('Быть такого не может') # Хотя наверное может вконце!!!!

    elif r == 'right':
        if have_out_open_door(x,y,r, grid): # Есть дорога вправо?
            if have_in_open_doors(x,y,grid)[2] in [0,1]: grid[y][x] = False
            move(x+1,y,grid,mgrid)
        else:
            print(grid)
            sys.exit('Быть такого не может') # Хотя наверное может вконце!!!!
    elif r == 'down':
        if have_out_open_door(x,y,r, grid): # Есть дорога вниз?ъ
            if have_in_open_doors(x,y,grid)[2] in [0,1]: grid[y][x] = False
            move(x,y+1,grid,mgrid)
        else:
            print(grid)
            sys.exit('Быть такого не может') # Хотя наверное может вконце!!!!
    else:
        print("Странный ответ от функции get_route: ", r)
        sys.exit("Error")






def main():
    grid = [[True for x in range(GRID[0])] for y in range(GRID[1])] # Сама таблица - пока узел True через него можно идти, иначе идем через другой
    memory_grid = [[0 for x in range(GRID[0])] for y in range(GRID[1])] #Сюда буду записывать интересные данные, типа сколько раз через каждый узел прошел
    # grid[0][2] = False
    x, y = 0, 0
    while grid[0][1] == True and grid[1][0] == True:
        move(x,y,grid,memory_grid)

    print(grid)

    print(memory_grid)



if __name__ == "__main__":
    main()