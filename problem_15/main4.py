
GRID = (21,21)


def sum_inputs(x,y,grid):
    if x == 0 and y ==0:
        return 0
    elif x > 0 and y > 0:
        return grid[x-1][y] + grid[x][y-1]
    elif (x > 0 and y == 0) or (x == 0 and y > 0):
        return 1
    else:
        print(f'Неизвестное содержание параметра x= {x}, y= {y}: ')
        sys.exit("Error")




def main():
    grid = [[0 for x in range(GRID[0])] for y in range(GRID[1])] # Сама таблица - заполнена 0
    for row in range(GRID[1]):
        for col in range(GRID[0]):
            grid[row][col] = sum_inputs(row,col,grid)
    return grid[GRID[0]-1][GRID[1]-1]



if __name__ == "__main__":
    print(main())

