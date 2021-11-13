import http.client
import Autocomplete

import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib

# Note the matplot tk canvas import
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph1 import return_info_to_graph
from graph3 import return_unemployed_per_opening_to_graph
from CCI import return_info_to_graph_cci


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib

matplotlib.use("TkAgg")

tickers = Autocomplete.get_stocks()
autocompleted_stocks_list = []

# Mat Plot Lib, get x and y values from graph1.py
def get_fig(stock_ticker):
    x, y = return_info_to_graph(stock_ticker)
    fig = plt.figure()
    plt.axis('on')
    plt.title(stock_ticker + '\'s Median Monthly Stock Price vs Unemployment Rate ')
    plt.plot(x, y, 'o')
    plt.xlabel("Unemployment Rate")
    plt.ylabel("Median Monthly Stock Price")
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)
    return fig



# Mat Plot Lib, get x and y values from graph1.py
def get_fig_2(stock_ticker):
    p, q = return_info_to_graph_cci(stock_ticker)
    fig_2 = plt.figure()
    plt.title(stock_ticker + '\'s Median Monthly Stock Price vs CCI ')
    plt.plot(p, q, 'o')
    plt.xlabel("CCI")
    plt.ylabel("Median Monthly Stock Price")
    m, b = np.polyfit(p, q, 1)
    plt.plot(p, m * p + b)
    return fig_2


def get_fig3(stock_ticker):
    x, y = return_unemployed_per_opening_to_graph(stock_ticker)
    fig3 = plt.figure()
    plt.title(stock_ticker + '\'s Median Monthly Stock Price vs Unemployed per Job Opening Ratio')
    plt.plot(x, y, 'o')
    plt.xlabel("Unemployed per Job Opening")
    plt.ylabel("Median Monthly Stock Price")
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)
    return fig3

# Function to draw our error image
def error_fig():
    fig = plt.figure()
    image = plt.imread('Error_image.jpg')
    plt.imshow(image)
    plt.axis('off')
    return fig



# Function to draw graph
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


sg.theme('Light Brown 3')

figure_x, figure_y, figure_w, figure_h = get_fig("AAPL").bbox.bounds

# define the window layout, the third element is the actual graph
layout = [[sg.Text('Enter Stock Ticker', font='Any 18')],
          # [sg.Combo(autocompleted_stocks_list, default_value='AAPL', key='Auto')],
          [sg.Input(key='-INPUT-'), sg.Button('Search')],
          [sg.Canvas(size=(figure_w, figure_h * 0.9), key='-CANVAS-'), sg.Canvas(size=(figure_w, figure_h * 0.9), key='-CANVAS1-')],

          [sg.Canvas(size=(figure_w, figure_h * 0.9), key='-CANVAS2-')]]

# logic for window
window = sg.Window('Stock Correlation',
                   layout, force_toplevel=True, finalize=True)

# add the plot to the window
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, get_fig("AAPL"))
fig_photo_2 = draw_figure(window['-CANVAS2-'].TKCanvas, get_fig_2("AAPL"))
fig_photo3 = draw_figure(window['-CANVAS1-'].TKCanvas, get_fig3("AAPL"))

while True:
    # show it all again and get buttons
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    values['-INPUT-'] = ''.join(filter(str.isalnum, values['-INPUT-']))[:5]
    window['-INPUT-'].update(values['-INPUT-'])
    # autocompleted_stocks_list = Autocomplete.get_top_five_stocks(values['-INPUT-'], tickers)
    # print(autocompleted_stocks_list)
    # window['Auto'].update(autocompleted_stocks_list)
    if event == 'Search':
        fig_photo.get_tk_widget().forget()
        fig_photo_2.get_tk_widget().forget()
        fig_photo3.get_tk_widget().forget()
        try:
            fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, get_fig(values['-INPUT-']))
            fig_photo_2 = draw_figure(window['-CANVAS2-'].TKCanvas, get_fig_2(values['-INPUT-']))
            fig_photo3 = draw_figure(window['-CANVAS1-'].TKCanvas, get_fig3(values['-INPUT-']))
        except urllib.error.URLError:
            print('Bruh that ain\'t a stock')
            fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, error_fig())
