import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import urllib
from tkinter import font
import yfinance as yf
# Note the matplot tk canvas import
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
from unemployment_before import UnemploymentBefore
from unemployment_covid import UnemploymentCovid
from job_openings_before import JobOpeningBefore
from job_openings_covid import JobOpeningsCovid


matplotlib.use("TkAgg")


def get_graph():
    font = {'family': 'serif',
            'color': 'darkred',
            'weight': 'normal',
            'size': 16,
            }

    x = np.linspace(0.0, 5.0, 100)
    y = np.cos(2 * np.pi * x) * np.exp(-x)
    fig = plt.figure()

    plt.plot(x, y, 'k')
    plt.title('Damped exponential decay', fontdict=font)
    plt.text(2, 0.65, r'$\cos(2 \pi t) \exp(-t)$', fontdict=font)
    plt.xlabel('time (s)', fontdict=font)
    plt.ylabel('voltage (mV)', fontdict=font)

    # Tweak spacing to prevent clipping of ylabel
    plt.subplots_adjust(left=0.15)
    return fig


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


figure_x, figure_y, figure_w, figure_h = get_graph().bbox.bounds


layout = [[sg.Canvas(size=(figure_w, figure_h * 0.9), key='-CANVAS-', background_color='#232323')]]
window = sg.Window('Trial',
                   layout, force_toplevel=True, finalize=True, background_color='#232323')


draw_figure(window['-CANVAS-'].TKCanvas, get_graph())

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()


