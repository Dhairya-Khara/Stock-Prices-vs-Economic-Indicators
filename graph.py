""" Graph class """
import statistics
from numpy import *
from pandas import DataFrame
from typing import *
import datetime
import numpy as np


class Graph:
    """ Abstract class graph """
    _ticker: str

    def __init__(self, ticker: str) -> None:
        """Creates graph object with specified ticker"""
        self._ticker = ticker

    def get_stock_data(self) -> DataFrame:
        """ Returns stock data for the specified stock ticker """
        raise NotImplementedError

    def get_datetime_to_closing(self, stock_info: DataFrame) -> list[tuple[datetime, Any]]:
        """ Returns the data """
        list_so_far = []
        for _, row in stock_info.iterrows():
            datetime_obj = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
            list_so_far.append((datetime_obj, row['Close']))
        return list_so_far

    def get_monthly_closing_prices(self, starting_month: int, datetime_to_closing: list[tuple]) -> list[list]:
        """ Returns a list of closing prices """
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

    def calculate_median_values(self, monthly_closing_prices: list[list[float]]) -> list:
        """ Return median stock price for each month """
        list_so_far = []
        for i in range(len(monthly_closing_prices)):
            list_so_far.append(statistics.median(monthly_closing_prices[i]))
        return list_so_far

    def get_values_of_independent_variable(self) -> DataFrame:
        """ Returns a list of data points for the specified independent variable """
        raise NotImplementedError

    def get_r_squared(self, x, y) -> None:
        """ Returns r^2 value based on x, y"""
        correlation_matrix = np.corrcoef(x, y)
        correlation_xy = correlation_matrix[0, 1]
        r_squared = correlation_xy ** 2
        return r_squared

    def return_info_to_graph(self, starting_month) -> tuple[ndarray, ndarray]:
        """ Returns a tuple of coordinates that matplotlib can graph """
        stock_info = self.get_stock_data()
        datetime_to_closing_prices = self.get_datetime_to_closing(stock_info)  # STEP 2
        monthly_closing_prices = self.get_monthly_closing_prices(starting_month, datetime_to_closing_prices)  # STEP 3
        list_of_median_values = self.calculate_median_values(monthly_closing_prices)  # STEP 4
        list_of_independent_variable_values = self.get_values_of_independent_variable()  # STEP 5
        x = np.array(list_of_independent_variable_values)
        y = np.array(list_of_median_values)
        return x, y

