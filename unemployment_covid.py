"""
CSC110 Final Project: UnemploymentCovid Graph class

Module Description
==================
This module contains the code for the UnemploymentCovid Graph. It inherits from the abstract class Graph.

At the bottom of the file we've provided code to run doctest and python_ta.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of TAs and instructors
teaching CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Chenika Bukes, Krishna Cheemalapati, Aryan Goel, and Dhairya Khara.
"""
import datetime
import time
import pandas as pd
from pandas import DataFrame
from graph import Graph


class UnemploymentCovid(Graph):
    """ UnemploymentCovid class inheriting from parent class Graph

    Instance Attributes:
        - _ticker: a string of a stock ticker inputted by the user

    Representation Invariants:
        - len(self._ticker) > 0
    """
    _ticker: str

    def __init__(self, ticker: str) -> None:
        """Creates graph object with specified ticker"""
        Graph.__init__(self, ticker)

    def get_stock_data(self) -> DataFrame:
        """ Returns stock data for the specified stock ticker """
        period1 = int(time.mktime(datetime.datetime(2020, 4, 1, 0, 0).timetuple()))
        period2 = int(time.mktime(datetime.datetime(2021, 8, 30, 23, 59).timetuple()))

        query_string = f'https://query1.finance.yahoo.com/v7/finance/download/' \
                       f'{self._ticker}?period1={period1}&period2={period2}'

        return pd.read_csv(query_string)

    def get_values_of_independent_var(self) -> list:
        """ Returns a list of data points for the specified independent variable """
        list_so_far = []
        adf = pd.read_excel('Unemployment_Rates.xlsx', sheet_name='COVID')

        for _, row in adf.iterrows():
            list_so_far.append(row['Total'])
        return list_so_far


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'statistics', 'numpy', 'pandas', 'datetime', 'time', 'graph'],
        'max-line-length': 200,
        'disable': ['R1705', 'C0200']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
