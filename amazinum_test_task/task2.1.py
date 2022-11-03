import random


def show_matrix(matrix):
    for row in range(len(matrix)):
        for cell in range(len(matrix)):
            print(matrix[row][cell], end=' ')
        print("")
    print("")


def generate_matrix():

    matrix = []

    for i in range(7):
        a = []
        for j in range(7):
            a.append(random.randint(0, 1))
        matrix.append(a)

    print("Generated matrix: ")
    show_matrix(matrix)

    # life(matrix_name, size, iterations)
    life(matrix, 7)


def life(matrix, size):
    # Array for counting of cell's neighbours
    neighbours = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]]

    while True:
        # This cycle counts neighbours
        for row in range(size):
            for cell in range(size):
                if matrix[row][cell] == 1:
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
        for row in range(size):
            for cell in range(size):
                if matrix[row][cell] == 1:
                    if neighbours[row][cell] <= 1 or neighbours[row][cell] >= 4:
                        matrix[row][cell] = 0
                if matrix[row][cell] == 0 and neighbours[row][cell] == 3:
                    matrix[row][cell] = 1

        answer = input("Generate the next iteration? (y/n) ")
        if answer == "y":
            print("Changed matrix: ")
            show_matrix(matrix)

            for var1 in range(len(neighbours)):
                for var2 in range(len(neighbours[var1])):
                    neighbours[var1][var2] = 0
        else:
            quit()


if __name__ == '__main__':
    generate_matrix()
