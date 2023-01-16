from lesson3.question1 import Question1

"""
Create a column that estimates the population using Energy Supply and Energy Supply per capita. 
What is the third most populous country according to this estimate?

This function should return a single string value.
"""


def answer_five():
    question1 = Question1()
    top15 = question1.answer_one()

    population_list = []
    n = len(top15.iloc[:, 1])
    for i in range(n):
        population = top15.iloc[i, 7] / top15.iloc[i, 8]
        if population > 0:
            population_list.append([top15.index[i], int(population)])

    print(population_list, '\n')
    population_list.sort()
    temp = sorted(population_list, key=lambda population_list: population_list[1])
    print(temp, '\n')

    return temp[-3][0]


if __name__ == "__main__":
    print(answer_five())
