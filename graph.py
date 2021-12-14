"""
CSC110 Final Project: Graph class

Module Description
==================
This module contains the code for the abstract class Graph. It also contains related top-level
functions that make our user interface possible.

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
import statistics
import datetime
from numpy import ndarray, array, corrcoef
from pandas import DataFrame


def get_datetime_to_closing(stock_info: DataFrame) -> list[tuple[datetime, float]]:
    """ Returns a list of tuples from stock_info where the first index is the date (datetime object)
    and the second index is the closing price of that day """
    list_so_far = []
    for _, row in stock_info.iterrows():
        datetime_obj = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
        list_so_far.append((datetime_obj, row['Close']))
    return list_so_far


def get_monthly_closing_prices(starting_month: int, datetime_to_closing: list[tuple]) -> list[list]:
    """ Returns a list where each element is a list of closing prices acquired from datetime_to_closing.
    Each inner list contains the prices for a specific month.
    The first inner list contains the stock prices of each day in starting_month

    Preconditions:
        - 1 <= starting_month <= 12
    """
    current_month = starting_month
    temp_list = []
    list_so_far = []
    for day in datetime_to_closing:
        if day[0].month == current_month:
            temp_list.append(day[1])
        else:
            list_so_far.append(temp_list)
            current_month = day[0].month
            temp_list = []
    list_so_far.append(temp_list)
    return list_so_far


def calculate_median_values(monthly_closing_prices: list[list[float]]) -> list:
    """ Return median stock price for each month in monthly_closing_prices"""
    list_so_far = []
    for i in monthly_closing_prices:
        list_so_far.append(statistics.median(i))
    return list_so_far


def get_r_squared(x: ndarray, y: ndarray) -> float:
    """ Returns r^2 value based on x, y

    Preconditions:
        - x.size == y.size

    >>> ind_var = array([0.9, 0.8, 0.8, 0.8, 0.9, 0.9, 0.9, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.9, 0.9])
    >>> dep_var = array([213.320007, 221.185005, 220.2249985, 189.1050035, 164.709999, 153.5550005, 171.154999,\
      186.324997, 200.3600005, 188.660004,  194.809998, 204.5, 204.160004 , 218.820007 , 236.040001 ,\
      262.640015 ,279.589996 ])
    >>> get_r_squared(ind_var, dep_var)
    0.000629732010597634
    """
    correlation_matrix = corrcoef(x, y)
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy ** 2
    return r_squared


class Graph:
    """ Abstract class Graph

    Instance Attributes:
        - _ticker: a string of a stock ticker inputted by the user

    Representation Invariants:
        - len(self._ticker) > 0
    """
    _ticker: str

    def __init__(self, ticker: str) -> None:
        """Initializes a Graph"""
        self._ticker = ticker

    def get_stock_data(self) -> DataFrame:
        """ Returns stock data for the specified stock ticker """
        raise NotImplementedError

    def get_values_of_independent_var(self) -> DataFrame:
        """ Returns a list of data points for the specified independent variable """
        raise NotImplementedError

    def return_info_to_graph(self, starting_month: int) -> tuple[ndarray, ndarray]:
        """ Returns a tuple where first element is an ndarray of the independent variable and the second element is
        an ndarray of the dependent variable. Passes starting_month to get_monthly_closing_prices

        Preconditions:
            - 1 <= starting_month <= 12
        """
        stock_info = self.get_stock_data()
        datetime_to_closing_prices = get_datetime_to_closing(stock_info)  # STEP 2
        monthly_closing_prices = get_monthly_closing_prices(starting_month, datetime_to_closing_prices)  # STEP 3
        list_of_x_values = calculate_median_values(monthly_closing_prices)  # STEP 4
        list_of_y_values = self.get_values_of_independent_var()  # STEP 5
        x = array(list_of_x_values)
        y = array(list_of_y_values)
        return x, y


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'statistics', 'numpy', 'pandas', 'datetime'],
        'max-line-length': 200,
        'disable': ['R1705', 'C0200']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
