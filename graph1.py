"""Stock Data"""
import time
import datetime
import pandas as pd
from pprint import pprint
import statistics
import matplotlib.pyplot as plt
import numpy as np


# STEP 1 - Get Stock Data from April 1 to Aug 30
def get_stock_data(ticker):
    period1 = int(time.mktime(datetime.datetime(2020, 4, 1, 0, 0).timetuple()))
    period2 = int(time.mktime(datetime.datetime(2021, 8, 30, 23, 59).timetuple()))
    interval = '1d'

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&' \
                   'interval={interval}&events=history&includeAdjustedClose=true'

    return pd.read_csv(query_string)


# STEP 2 - Parse DataFrame object, i.e. make a list where each element is a tuple, first index is the date,
# second index is the closing price
def get_datetime_to_closing_prices():
    list_so_far = []
    for index, row in df.iterrows():
        datetime_obj = datetime.datetime.strptime(row['Date'], '%Y-%m-%d')
        list_so_far.append((datetime_obj, row['Close']))
    return list_so_far


# STEP 3 - Make a 2D List (list of lists) s.t. every element is a list of all the closing prices of a month
def get_monthly_closing_prices(startingMonth):
    current_month = startingMonth
    temp_list = []
    list_so_far = []
    for day in datetime_to_closing_prices:
        if day[0].month == current_month:
            temp_list.append(day[1])
        else:
            list_so_far.append(temp_list)
            current_month = day[0].month
            temp_list = []
    list_so_far.append(temp_list)
    return list_so_far


# STEP 4 - Calculate Median for each month
def calculate_median_values():
    list_so_far = []
    for i in range(len(monthly_closing_prices)):
        list_so_far.append(statistics.median(monthly_closing_prices[i]))
    return list_so_far


# Step 5 - Get independent variables in a list, Unemployment Rate in this case.
def get_list_of_unemployment_rates():
    list_so_far = []
    adf = pd.read_excel('Unemployment_Rates.xlsx', sheet_name='Required_Rates')

    for index, row in adf.iterrows():
        list_so_far.append(row['Total'])
    return list_so_far


# STEP 6 - Linear Regression.
def get_r_squared():
    correlation_matrix = np.corrcoef(x, y)
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy ** 2
    return r_squared


# STEP 7 - Plot the Graph
def plot_the_graph():
    plt.plot(x, y, 'o')
    plt.xlabel("Unemployment Rate")
    plt.ylabel("Median Stock Price")
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)
    plt.show()


df = get_stock_data('AAPL')  # STEP 1
datetime_to_closing_prices = get_datetime_to_closing_prices()  # STEP 2
monthly_closing_prices = get_monthly_closing_prices(4)  # STEP 3
list_of_median_values = calculate_median_values()  # STEP 4
list_of_unemployment_rates = get_list_of_unemployment_rates()  # STEP 5
x = np.array(list_of_unemployment_rates)
y = np.array(list_of_median_values)
pprint(get_r_squared())  # STEP 6
plot_the_graph()  # STEP 7
