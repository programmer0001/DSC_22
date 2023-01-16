from lesson3.question1 import Question1
import pandas as pd

"""
Question 2
What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)

This function should return a Series named avgGDP with 15 countries and their average GDP sorted in descending order.
"""


def answer_two():
    question1 = Question1()
    top15 = question1.answer_one()
    # print(top15.to_string(), '\n')

    avgGDP = pd.Series(dtype='float64')
    n = len(top15.iloc[:, 1])
    for i in range(n):
        # TODO: what's better: make more understandable variables or less lines of code?
        # TODO: why this code doesn't work in jupyter
        country = tuple((top15.index[i],))
        avg = top15.iloc[i, 10:].mean()
        new_element = pd.Series([avg], index=country)
        avgGDP = pd.concat([avgGDP, new_element])

    # print(avgGDP.to_string(), '\n')
    return avgGDP


if __name__ == "__main__":
    a2 = answer_two()
    print(a2)
    a2.to_excel("answer2.xlsx")
