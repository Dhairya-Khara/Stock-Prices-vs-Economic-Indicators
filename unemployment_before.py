import datetime
import time
import pandas as pd
from numpy import *
import numpy as np
from pandas import DataFrame
from graph import Graph


class UnemploymentBefore(Graph):

    def __init__(self, ticker: str) -> None:
        """Creates graph object with specified ticker"""
        Graph.__init__(self, ticker)

    def get_stock_data(self) -> DataFrame:
        """ Returns stock data for the specified stock ticker """
        period1 = int(time.mktime(datetime.datetime(2018, 8, 1, 0, 0).timetuple()))
        period2 = int(time.mktime(datetime.datetime(2019, 12, 30, 23, 59).timetuple()))

        query_string = f'https://query1.finance.yahoo.com/v7/finance/download/' \
                       f'{self._ticker}?period1={period1}&period2={period2}'

        return pd.read_csv(query_string)

    def get_values_of_independent_variable(self) -> list:
        """ Returns a list of data points for the specified independent variable """
        list_so_far = []
        adf = pd.read_excel('Unemployment_Rates.xlsx', sheet_name='Before')

        for index, row in adf.iterrows():
            list_so_far.append(row['Total'])
        return list_so_far
