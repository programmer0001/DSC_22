import random
import numpy as np
import matplotlib.pyplot as plt


def generate_matrix():
    matrix = []

    for i in range(7):
        a = []
        for j in range(7):
            a.append(random.randint(0, 1))
        matrix.append(a)

    print("Generated matrix: ")
    show_matrix(matrix)
    show_matrix_chart(matrix)

    # life(matrix_name, size, iterations)
    life(matrix, 7, 1)


def life(matrix, size, lifeCycle):
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

    print("Changed matrix: ")
    show_matrix(matrix)
    show_matrix_chart(matrix)
    ask_user()


def show_matrix(matrix):
    for row in range(len(matrix)):
        for cell in range(len(matrix)):
            print(matrix[row][cell], end=' ')
        print("")
    print("")


def show_matrix_chart(matrix):
    fig = plt.figure(figsize=(7, 7))
    ax1 = fig.add_subplot(projection='3d')

    _x = np.arange(7)
    _y = np.arange(7)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    _tup = np.array(matrix)
    top = _tup[x, y]
    bottom = np.zeros_like(top)
    width = depth = 0.9

    z2 = np.linspace(0, 8)
    x2 = np.sin(z2)
    y2 = np.cos(z2)

    ax1.bar3d(x, y, bottom, width, depth, top, color='#98FB98')
    ax1.plot3D(x2, y2, z2, '#f5f5f5')
    ax1.set_title('Task 2.2')

    plt.show()


def ask_user():
    answer = input("Generate the next matrix? (y/n) ")
    if answer == "y":
        generate_matrix()
    else:
        quit()


if __name__ == '__main__':
    generate_matrix()
