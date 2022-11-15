from lesson3.question1 import Question1

"""
Create a new column that is the ratio of Self-Citations to Total Citations.
What is the maximum value for this new column, and what country has the highest ratio?

This function should return a tuple with the name of the country and the ratio.
"""


def answer_four():
    question1 = Question1()
    top15 = question1.answer_one()

    country = ''
    max_ratio = 0
    n = len(top15.iloc[:, 1])
    for i in range(n):
        ratio = top15.iloc[i, 4] / top15.iloc[i, 3]
        if ratio > max_ratio:
            country = top15.index[i]
            max_ratio = ratio

    return tuple((country, max_ratio),)


if __name__ == "__main__":
    print(answer_four())
