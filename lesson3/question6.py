import pandas as pd
from lesson3.question1 import Question1

"""
Create a column that estimates the number of citable documents per person.
What is the correlation between the number of citable documents per capita
and the energy supply per capita?
Use the .corr() method, (Pearson's correlation).

This function should return a single number.
"""


def answer_six():
    question1 = Question1()
    top15 = question1.answer_one()

    df = pd.DataFrame(columns=['docs_per_capita', 'energy_supply_per_capita'])
    n = len(top15.iloc[:, 1])
    for i in range(n):
        population = top15.iloc[i, 7] / top15.iloc[i, 8]
        if population > 0:
            docs_per_capita = top15.iloc[i, 2] / population
            energy_supply_per_capita = top15.iloc[i, 8]
            temp_df = pd.DataFrame({'docs_per_capita': [docs_per_capita],
                                    'energy_supply_per_capita': [energy_supply_per_capita]})
            # print(temp_df.to_string(), '\n')
            df = pd.concat([df, temp_df])

    # print(df.to_string(), '\n')

    return df.corr().iloc[0, 1]


if __name__ == "__main__":
    print(answer_six())
