import pandas as pd

from lesson3.question1 import Question1

"""
Use the following dictionary to group the Countries by Continent, 
then create a dateframe that displays the sample size 
(the number of countries in each continent bin), 
and the sum, mean, and std deviation for the estimated population of each country.
"""


def answer_seven(ContinentDict):
    question1 = Question1()
    top15 = question1.answer_one()

    zeros = [0, 0, 0, 0, 0]
    countries_population = pd.DataFrame(index=['Asia', 'Australia', 'Europe',
                                               'North America', 'South America'],
                                        columns=ContinentDict.keys())
    final_df = pd.DataFrame({'Continent': ['Asia', 'Australia', 'Europe',
                                           'North America', 'South America'],
                             'size': zeros, 'sum': zeros,
                             'mean': zeros, 'std': zeros}).set_index(['Continent'])
    # print(final_df.to_string(), '\n')
    for i in ContinentDict:
        row_index = list(ContinentDict).index(i)
        population = top15.iloc[row_index, 7] / top15.iloc[row_index, 8]

        if population > 0:
            row_index = ContinentDict[i]
            countries_population.loc[row_index, i] = population
            final_df.loc[row_index, 'size'] += 1
            final_df.loc[row_index, 'sum'] += population
            final_df.loc[row_index, 'mean'] += final_df.loc[row_index, 'sum'] / final_df.loc[row_index, 'size']

    print(final_df.to_string(), '\n')
    print(countries_population.to_string(), '\n')
    n = len(countries_population.iloc[:, 1])
    # TODO: line 42: ValueError: Must have equal len keys and value when setting with an iterable
    for i in range(n):
        print(i, n)
        aa = countries_population[list(ContinentDict.keys())].std(axis=1, skipna=True)
        print(aa, "\n")
        print(final_df)
        final_df.iloc[i, 3] = aa[i]

    return final_df


if __name__ == "__main__":
    ContinentDict = {'China': 'Asia',
                     'United States': 'North America',
                     'Japan': 'Asia',
                     'United Kingdom': 'Europe',
                     'Russian Federation': 'Europe',
                     'Canada': 'North America',
                     'Germany': 'Europe',
                     'India': 'Asia',
                     'France': 'Europe',
                     'South Korea': 'Asia',
                     'Italy': 'Europe',
                     'Spain': 'Europe',
                     'Iran': 'Asia',
                     'Australia': 'Australia',
                     'Brazil': 'South America'}

    print(answer_seven(ContinentDict))
