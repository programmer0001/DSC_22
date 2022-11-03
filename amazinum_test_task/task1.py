def input_matrix():
    a = [[], [], []]
    for i in range(3):
        print("Enter %d line of matrix A and divide nums by space: " % (i + 1))
        a[i] = list(map(int, input().split(" ")))

    b = input("Enter matrix B and divide nums by space: ").split(" ")
    b = list(map(int, b))

    calculate(a, b)


def calculate(a, b):
    determinant = a[0][0] * a[1][1] * a[2][2] + a[0][1] * a[1][2] * a[2][0] + a[0][2] * a[1][0] * a[2][1] - \
                  a[0][2] * a[1][1] * a[2][0] - a[0][1] * a[1][0] * a[2][2] - a[0][0] * a[1][2] * a[2][1]

    determinant1 = b[0] * a[1][1] * a[2][2] + b[1] * a[0][2] * a[2][1] + b[2] * a[0][1] * a[1][2] - \
                   b[2] * a[1][1] * a[0][2] - b[1] * a[0][1] * a[2][2] - b[0] * a[1][2] * a[2][1]

    determinant2 = (a[0][0] * b[1] * a[2][2]) + (a[1][0] * b[2] * a[0][2]) + (a[2][0] * b[0] * a[1][2]) - \
                   (a[0][2] * b[1] * a[2][0]) - (a[1][0] * b[0] * a[2][2]) - (a[0][0] * b[2] * a[1][2])

    determinant3 = a[0][0] * a[1][1] * b[2] + a[1][0] * a[2][1] * b[0] + a[2][0] * a[0][1] * b[1] - \
                   a[2][0] * a[1][1] * b[0] - a[0][1] * a[1][0] * b[2] - a[2][1] * a[0][0] * b[1]

    if determinant != 0:
        x = determinant1 / determinant
        y = determinant2 / determinant
        z = determinant3 / determinant
        print("X = (%d, %d, %d)" % (x, y, z))
    elif determinant == 0 and (determinant1 != 0 or
                               determinant2 != 0 or
                               determinant3 != 0):
        print("Matrix don't have solution.")
    elif determinant == 0 and determinant1 == 0 \
            and determinant2 == 0 and determinant3 == 0:
        print("Matrix have an infinite number of solutions.")


if __name__ == '__main__':
    input_matrix()
