import numpy as np

if __name__ == "__main__":
    dots = np.random.uniform(-1, 1, (9999999, 2))

    count = 0
    for i in dots:
        count += (i[0] ** 2 + i[1] ** 2 <= 1)

    print(count * 4 / dots.shape[0])
