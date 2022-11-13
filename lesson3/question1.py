import pandas as pd
import numpy as np
from tabulate import tabulate


class Question1:

    def _query_energy(self):
        energy = pd.read_excel('Energy.xlsx', header=None,
                               names=['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
                               usecols='C:F', skiprows=18, nrows=228, engine='openpyxl')

        energy = energy.replace(['...'], np.nan)
        energy['Energy Supply'] *= 1000000

        source_countries_names = ['Republic of Korea', 'United States of America20',
                                  'United Kingdom of Great Britain and Northern Ireland',
                                  'China, Hong Kong Special Administrative Region',
                                  'Bolivia (Plurinational State of)', 'Switzerland17']
        final_countries_names = ['South Korea', 'United States', 'United Kingdom',
                                 'Hong Kong', 'Bolivia', 'Switzerland']
        energy['Country'] = energy['Country'].replace(source_countries_names, final_countries_names)

        return energy

    def _query_gdp(self):
        gdp = pd.read_csv('world_bank.csv', sep=',', header=0,
                          dtype=None, skiprows=4, encoding='utf-8')

        scn_gdp = ['Korea, Rep.', 'Iran, Islamic Rep.', 'Hong Kong SAR, China']  # source country names
        fcn_gdp = ['South Korea', 'Iran', 'Hong Kong']  # final country names
        gdp['Country'] = gdp['Country'].replace(scn_gdp, fcn_gdp)

        return gdp

    def _query_scimen(self):
        scim_en = pd.read_excel('scimEn.xlsx', header=0,
                                engine='openpyxl')
        return scim_en

    def answer_one(self):
        energy = self._query_energy()
        gdp = self._query_gdp()
        scim_en = self._query_scimen()

        energy.set_index('Country')
        gdp.set_index('Country')
        scim_en.set_index('Country')

        temp_df = pd.merge(scim_en, energy, on='Country', how='left')
        final_df = pd.merge(temp_df, gdp, on='Country', how='left')

        final_df.drop(final_df.tail(196).index, inplace=True)
        final_df.drop(final_df.iloc[:, 1:3], axis=1, inplace=True)
        final_df.drop(final_df.iloc[:, 10:58], axis=1, inplace=True)
        final_df.drop(final_df.iloc[:, 21:28], axis=1, inplace=True)

        return final_df


if __name__ == "__main__":
    question1 = Question1()
    qa1 = question1.answer_one()
    print(tabulate(qa1, tablefmt='psql'))
    qa1.to_excel('answer1.xlsx')
