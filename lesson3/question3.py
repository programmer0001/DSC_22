from lesson3.question2 import answer_two
from lesson3.question1 import Question1

"""
Question 3
By how much had the GDP changed over the 10-year span for the country with the 6th largest average GDP?

This function should return a single number.
"""


def answer_three():
    question1 = Question1()

    avg_gdp = answer_two()  # Series of avg_gdp
    avg_gdp = avg_gdp.sort_values(ascending=True)
    sixth_gdp_country = avg_gdp.index[5]  # name of sixth country
    gdps_data = question1.answer_one().loc[sixth_gdp_country]
    # print(gdps_data.to_string(), '\n')
    # TODO: Do I have to return absolute value or change in percent?
    balance = gdps_data.loc['2015'] - gdps_data.loc['2005']

    return balance


if __name__ == "__main__":
    print(answer_three())
