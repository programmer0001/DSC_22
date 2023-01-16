import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt


def check_count(dots):
    plt.axes()
    rectangle = plt.Rectangle((0, 0), 1, 1, fc='white', ec='black')
    circle = plt.Circle((0, 0), 1, fc='white', ec='black')
    plt.gca().add_patch(rectangle)
    plt.gca().add_patch(circle)
    plt.scatter(dots[0:-1, 0], dots[0:-1, 1])

    count = 0
    for i in tqdm(dots):
        count += ((i[0] ** 2 + i[1] ** 2) ** 0.5 <= 1)

    print(count * 4 / dots.shape[0])

    plt.axis('scaled')
    plt.show()


if __name__ == "__main__":
    dots1 = np.random.uniform(-1, 1, (999, 2))
    check_count(dots1)
