import datetime
import time
import pandas as pd
from numpy import *
import numpy as np
from pandas import DataFrame
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
