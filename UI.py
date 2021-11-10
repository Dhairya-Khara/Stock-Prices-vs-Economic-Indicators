import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt

# Note the matplot tk canvas import
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph1 import return_info_to_graph


# Mat Plot Lib, get x and y values from graph1.py
def get_fig(stock_ticker):
    x, y = return_info_to_graph(stock_ticker)
    fig = plt.figure()
    plt.title(stock_ticker + '\'s Median Monthly Stock Price vs Unemployment Rate ')
    plt.plot(x, y, 'o')
    plt.xlabel("Unemployment Rate")
    plt.ylabel("Median Monthly Stock Price")
    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)
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
          [sg.Input(key='-INPUT-'), sg.Button('Search')],
          [sg.Canvas(size=(figure_w, figure_h), key='-CANVAS-')]]

# logic for window
window = sg.Window('Stock Correlation',
                   layout, force_toplevel=True, finalize=True)

# add the plot to the window
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, get_fig("AAPL"))

while True:
    # show it all again and get buttons
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Search':
        fig_photo.get_tk_widget().forget()
        fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, get_fig(values['-INPUT-']))
