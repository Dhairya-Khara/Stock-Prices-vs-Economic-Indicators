import statistics
import datetime
import time
import numpy as np
import pandas as pd
from numpy import *
from pandas import DataFrame
from typing import *
from graph import Graph


class JobOpeningsCovid(Graph):
    """ Abstract class graph """
    _ticker: str

    def __init__(self, stock: str) -> None:
        """ Initialize a job openings graph """
        Graph.__init__(self, stock)

    def get_stock_data(self) -> DataFrame:
        """ Returns stock data for the specified stock ticker """
        period1 = int(time.mktime(datetime.datetime(2020, 4, 1, 0, 0).timetuple()))
        period2 = int(time.mktime(datetime.datetime(2021, 8, 30, 23, 59).timetuple()))

        query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{self._ticker}?period1={period1}&period2={period2}'

        return pd.read_csv(query_string)

    def get_values_of_independent_variable(self) -> list:
        """ Returns a list of data points for the specified independent variable """
        list_so_far = []
        adf = pd.read_excel('Unemployed_Per_Opening.xlsx', sheet_name='COVID')

        for _, row in adf.iterrows():
            list_so_far.append(row['Total'])

        return list_so_far

    def return_info_to_graph(self) -> tuple[ndarray, ndarray]:
        """ Returns a tuple of coordinates that matplotlib can graph """
        stock_info = self.get_stock_data()
        datetime_to_closing_prices = self.get_datetime_to_closing(stock_info)  # STEP 2
        monthly_closing_prices = self.get_monthly_closing_prices(4, datetime_to_closing_prices)  # STEP 3
        list_of_median_values = self.calculate_median_values(monthly_closing_prices)  # STEP 4
        list_of_independent_variable_values = self.get_values_of_independent_variable()  # STEP 5
        x = np.array(list_of_independent_variable_values)
        y = np.array(list_of_median_values)
        return x, y
