import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
from unemployment_before import UnemploymentBefore
from unemployment_covid import UnemploymentCovid
from job_openings_before import JobOpeningBefore
from job_openings_covid import JobOpeningsCovid

matplotlib.use("TkAgg")


def draw_graph(graph, title, x_label, y_label):
    x, y = graph.return_info_to_graph()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title(title,
              {'fontname': 'Franklin Gothic Medium'})
    plt.title(title)

    r_squared = round(graph.get_r_squared(x, y), 2)
    r_squared_text = "r\N{SUPERSCRIPT TWO} = " + str(r_squared)

    font = {'fontname': 'Franklin Gothic Medium', 'color': 'white', 'size': 8}

    ax.text(1.01, 0.9, r_squared_text, transform=ax.transAxes, fontdict=font)

    plt.plot(x, y, 'o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b)

    fig.set_dpi(70)
    ax.spines['left'].set_color('#EEEEEE')
    ax.spines['bottom'].set_color('#EEEEEE')
    ax.xaxis.label.set_color('#EEEEEE')
    ax.yaxis.label.set_color('#EEEEEE')
    ax.title.set_color('#EEEEEE')
    ax.tick_params(axis='x', colors='#EEEEEE')
    ax.tick_params(axis='y', colors='#EEEEEE')
    ax.set_facecolor('#757575')
    fig.patch.set_facecolor('#232323')
    return fig


def get_unemployment_covid(ticker, company_name):
    if len(company_name) > (len('s Median Monthly Stock Price vs Unemployment Rate (During COVID)') - 20):
        title = company_name + '\'s \n Median Monthly Stock Price vs Unemployment Rate (During COVID)'
    else:
        title = company_name + '\'s Median Monthly Stock Price \n vs Unemployment Rate (During COVID)'
    x_label = "Unemployment Rate"
    y_label = "Median Monthly Stock Price (USD)"
    return draw_graph(UnemploymentCovid(ticker), title, x_label, y_label)


def get_unemployment_before(ticker, company_name):
    if len(company_name) > (len('s Median Monthly Stock Price vs Unemployment Rate (During COVID)') - 20):
        title = company_name + '\'s \n Median Monthly Stock Price vs Unemployment Rate (During COVID)'
    else:
        title = company_name + '\'s Median Monthly Stock Price \n vs Unemployment Rate (During COVID)'
    x_label = "Unemployment Rate"
    y_label = "Median Monthly Stock Price (USD)"
    return draw_graph(UnemploymentBefore(ticker), title, x_label, y_label)


def get_job_openings_covid(ticker, company_name):
    if len(company_name) > (len('s Median Monthly Stock Price vs Unemployment Rate (During COVID)') - 20):
        title = company_name + '\'s \n Median Monthly Stock Price vs Unemployment Rate (During COVID)'
    else:
        title = company_name + '\'s Median Monthly Stock Price \n vs Unemployment Rate (During COVID)'
    x_label = "Unemployed Per Job Opening"
    y_label = "Median Monthly Stock Price (USD)"
    return draw_graph(JobOpeningsCovid(ticker), title, x_label, y_label)


def get_job_openings_before(ticker, company_name):
    if len(company_name) > (len('s Median Monthly Stock Price vs Unemployment Rate (During COVID)') - 20):
        title = company_name + '\'s \n Median Monthly Stock Price vs Unemployment Rate (During COVID)'
    else:
        title = company_name + '\'s Median Monthly Stock Price \n vs Unemployment Rate (During COVID)'
    x_label = "Unemployed Per Job Opening"
    y_label = "Median Monthly Stock Price (USD)"
    return draw_graph(JobOpeningBefore(ticker), title, x_label, y_label)


def error_fig():
    fig = plt.figure()
    image = plt.imread('Error_image.jpg')
    plt.imshow(image)
    plt.axis('off')
    fig.patch.set_facecolor('#232323')
    fig.set_dpi(70)
    return fig


# Function to draw graph
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


figure_x, figure_y, figure_w, figure_h = get_unemployment_covid("AAPL", "Apple").bbox.bounds

layout = [
    [sg.Text('Enter Stock Ticker', font='Franklin_Gothic_Medium', background_color='#232323', text_color='#EEEEEE')],
    [sg.Input(key='-INPUT-', background_color='#757575', text_color='#000000'),
     sg.Button('Search', button_color=('#000000', '#757575'))],
    [sg.Canvas(size=(figure_w, figure_h * 0.9), key='-CANVAS-', background_color='#232323'),
     sg.Canvas(size=(figure_w, figure_h * 0.9), key='-CANVAS1-', background_color='#232323')],

    [sg.Canvas(size=(figure_w, figure_h * 0.9), key='-CANVAS2-', background_color='#232323'),
     sg.Canvas(size=(figure_w, figure_h * 0.9), key='-CANVAS3-', background_color='#232323')]]

# logic for window
window = sg.Window('Stock Correlation',
                   layout, force_toplevel=True, finalize=True, background_color='#232323')

# add the plot to the window
photo_error = photo_unemployment_covid = draw_figure(window['-CANVAS1-'].TKCanvas,
                                                     get_unemployment_covid("AAPL", "Apple"))
photo_unemployment_before = draw_figure(window['-CANVAS-'].TKCanvas, get_unemployment_before("AAPL", "Apple"))
photo_job_openings_covid = draw_figure(window['-CANVAS3-'].TKCanvas, get_job_openings_covid("AAPL", "Apple"))
photo_job_openings_before = draw_figure(window['-CANVAS2-'].TKCanvas, get_job_openings_before("AAPL", "Apple"))
