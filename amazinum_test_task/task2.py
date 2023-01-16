def life(matrix1, rows, cells, lifeCycle):
    # Array for counting of cell's neighbours
    neighbours = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]

    for iteration in range(lifeCycle):
        # This cycle counts neighbours
        for row in range(rows):
            for cell in range(cells):
                if matrix1[row][cell] == 1:
                    if cell < 6:
                        neighbours[row][cell + 1] += 1
                    if cell > 0:
                        neighbours[row][cell - 1] += 1

                    for ncell in range(-1, 2):
                        position = cell + ncell
                        if row < 6 and 6 >= position >= 0:
                            neighbours[row + 1][position] += 1
                        if row > 0 and 6 >= position >= 0:
                            neighbours[row - 1][position] += 1

        # This cycle check neighbours' amount and change cell's status
        for row in range(rows):
            for cell in range(cells):
                if matrix1[row][cell] == 1:
                    if neighbours[row][cell] <= 1 or neighbours[row][cell] >= 4:
                        matrix1[row][cell] = 0
                if matrix1[row][cell] == 0 and neighbours[row][cell] == 3:
                    matrix1[row][cell] = 1

    # This cycle print matrix in console
    for row in range(rows):
        for cell in range(cells):
            print(matrix1[row][cell], end=' ')
        print("")


if __name__ == '__main__':
    matrix = [[1, 0, 0, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 1, 1],
              [1, 0, 0, 1, 0, 0, 1],
              [0, 1, 1, 0, 1, 1, 0],
              [1, 1, 1, 1, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1, 0, 1]]
    # life(matrix_name, rows in matrix, columns, iterations)
    life(matrix, len(matrix), len(matrix[0]), 7)
