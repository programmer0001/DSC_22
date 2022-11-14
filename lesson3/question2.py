from lesson3.question1 import Question1
import pandas as pd


def answer_two():
    question1 = Question1()
    top15 = question1.answer_one()

    avgGDP = pd.Series(dtype='float64')
    n = len(top15.iloc[:, 1])
    for i in range(n):
        # TODO: what's better: make more understandable variables or less lines of code?
        country = tuple((top15.iloc[i, 1],))
        avg = top15.iloc[i, 10:].mean()
        new_element = pd.Series([avg], index=country)
        avgGDP = pd.concat([avgGDP, new_element])

    return avgGDP


if __name__ == "__main__":
    print(answer_two())
