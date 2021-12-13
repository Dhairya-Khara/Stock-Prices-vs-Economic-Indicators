"""User Interface"""
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import matplotlib

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from unemployment_before import UnemploymentBefore
from unemployment_covid import UnemploymentCovid
from job_openings_before import JobOpeningsBefore
from job_openings_covid import JobOpeningsCovid
from graph import get_r_squared, Graph

matplotlib.use("TkAgg")
graph_bg_color = '#343a40'
dots_color = '#f1faee'
trend_line_color = '#e63946'


def draw_graph(graph: Graph, title: str, x_label: str, y_label: str, starting_month: int) -> plt.Figure:
    """"Returns fig which is a MatPlotLib graph plotting the x_label vs the y_label beginning with the starting_month"""
    x, y = graph.return_info_to_graph(starting_month)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title(title,
              {'fontname': 'Franklin Gothic Medium'})
    plt.title(title)

    r_squared = round(get_r_squared(x, y), 2)
    r_squared_text = "r\N{SUPERSCRIPT TWO} = " + str(r_squared)

    font = {'fontname': 'Franklin Gothic Medium', 'color': 'white', 'size': 9}

    ax.text(1.01, 0.9, r_squared_text, transform=ax.transAxes, fontdict=font)

    plt.plot(x, y, 'o', color=dots_color)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b, color=trend_line_color)

    fig.set_dpi(70)
    ax.spines['left'].set_color('#EEEEEE')
    ax.spines['bottom'].set_color('#EEEEEE')
    ax.xaxis.label.set_color('#EEEEEE')
    ax.yaxis.label.set_color('#EEEEEE')
    ax.title.set_color('#EEEEEE')
    ax.tick_params(axis='x', colors='#EEEEEE')
    ax.tick_params(axis='y', colors='#EEEEEE')
    ax.set_facecolor(graph_bg_color)
    fig.patch.set_facecolor('#232323')
    return fig


def get_unemployment_covid(ticker: str, company_name: str) -> plt.Figure:
    """ Returns the graph of median monthly stock prices vs unemployment rate during COVID-19 with the company_name
        inputted into the graph axes and titles"""
    if len(company_name) > (len('s Median Monthly Stock Price vs Unemployment Rate (During COVID)') - 20):
        title = company_name + '\'s \n Median Monthly Stock Price vs Unemployment Rate (During COVID)'
    else:
        title = company_name + '\'s Median Monthly Stock Price \n vs Unemployment Rate (During COVID)'
    x_label = "Unemployment Rate"
    y_label = "Median Monthly Stock Price (USD)"
    return draw_graph(UnemploymentCovid(ticker), title, x_label, y_label, 4)


def get_unemployment_before(ticker: str, company_name: str) -> plt.Figure:
    """ Returns the graph of median monthly stock prices vs unemployment rate before COVID-19 with the company_name
        inputted into the graph axes and titles"""
    if len(company_name) > (len('s Median Monthly Stock Price vs Unemployment Rate (Before COVID)') - 20):
        title = company_name + '\'s \n Median Monthly Stock Price vs Unemployment Rate (Before COVID)'
    else:
        title = company_name + '\'s Median Monthly Stock Price \n vs Unemployment Rate (Before COVID)'
    x_label = "Unemployment Rate"
    y_label = "Median Monthly Stock Price (USD)"
    return draw_graph(UnemploymentBefore(ticker), title, x_label, y_label, 8)


def get_job_openings_covid(ticker: str, company_name: str) -> plt.Figure:
    """ Returns the graph of median monthly stock prices vs unemployment rate during COVID-19 with the company_name
        inputted into the graph axes and titles"""
    if len(company_name) > (len('s Median Monthly Stock Price vs Unemployed per Job Opening (During COVID)') - 20):
        title = company_name + '\'s \n Median Monthly Stock Price vs Unemployed per Job Opening (During COVID)'
    else:
        title = company_name + '\'s Median Monthly Stock Price \n vs Unemployed per Job Opening (During COVID)'
    x_label = "Unemployed Per Job Opening"
    y_label = "Median Monthly Stock Price (USD)"
    return draw_graph(JobOpeningsCovid(ticker), title, x_label, y_label, 4)


def get_job_openings_before(ticker: str, company_name: str) -> plt.Figure:
    """Returns the graph of median monthly stock prices vs unemployment rate during COVID-19 with the company_name
        inputted in the title"""
    if len(company_name) > (len('s Median Monthly Stock Price vs Unemployed per Job Opening (Before COVID)') - 20):
        title = company_name + '\'s \n Median Monthly Stock Price vs Unemployed per Job Opening (Before COVID)'
    else:
        title = company_name + '\'s Median Monthly Stock Price \n vs Unemployed per Job Opening (Before COVID)'
    x_label = "Unemployed Per Job Opening"
    y_label = "Median Monthly Stock Price (USD)"
    return draw_graph(JobOpeningsBefore(ticker), title, x_label, y_label, 8)


def error_fig() -> plt.Figure:
    """ Returns the error figure to draw when the stock ticker entered is not valid """
    fig = plt.figure()
    image = plt.imread('Error_image.jpg')
    plt.imshow(image)
    plt.axis('off')
    fig.patch.set_facecolor(graph_bg_color)
    fig.set_dpi(70)

    font = {'fontname': 'Franklin Gothic Medium', 'color': 'white', 'size': 12}
    plt.text(-75, 600, 'The ticker you have entered corresponds to a stock we do not have the data for.',
             fontdict=font)
    return fig


# Function to draw graph
def draw_figure(canvas: sg.Canvas.TKCanvas, figure: plt.Figure) -> FigureCanvasTkAgg:
    """ Returns figure on the given PySimpleGUI canvas"""
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


def main_loop(pe: FigureCanvasTkAgg, g1: FigureCanvasTkAgg, g2: FigureCanvasTkAgg,
              g3: FigureCanvasTkAgg, g4: FigureCanvasTkAgg) -> None:
    """ The main loop of the program which calls the functions to draw the canvases specific to the user's input """
    while True:
        # show it all again and get buttons
        event, values = window.read()
        if event in [sg.WIN_CLOSED, 'Exit']:
            break
        values['-INPUT-'] = ''.join(filter(str.isalnum, values['-INPUT-']))[:5]
        window['-INPUT-'].update(values['-INPUT-'])
        if event == 'Search':
            pe.get_tk_widget().forget()
            g1.get_tk_widget().forget()
            g2.get_tk_widget().forget()
            g3.get_tk_widget().forget()
            g4.get_tk_widget().forget()
            try:
                stock_query = values['-INPUT-'].upper()
                ticker = yf.Ticker(stock_query)
                company_name = ticker.info['longName'].removesuffix(', Inc.').removesuffix(' Inc.')

                g1 = draw_figure(window['-CANVAS1-'].TKCanvas,
                                 get_unemployment_covid(values['-INPUT-'], company_name))
                g2 = draw_figure(window['-CANVAS-'].TKCanvas,
                                 get_unemployment_before(values['-INPUT-'], company_name))
                g3 = draw_figure(window['-CANVAS3-'].TKCanvas,
                                 get_job_openings_covid(values['-INPUT-'], company_name))
                g4 = draw_figure(window['-CANVAS2-'].TKCanvas,
                                 get_job_openings_before(values['-INPUT-'], company_name))

            except Exception:
                pe.get_tk_widget().forget()
                g1.get_tk_widget().forget()
                g2.get_tk_widget().forget()
                g3.get_tk_widget().forget()
                g4.get_tk_widget().forget()
                pe = draw_figure(window['-CANVAS-'].TKCanvas, error_fig())


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'statistics', 'numpy', 'pandas', 'datetime', 'time',
                          'graph', 'PySimpleGUI', 'matplotlib.pyplot', 'matplotlib', 'unemployment_before',
                          'unemployment_covid', 'unemployment_covid', 'job_openings_before', 'job_openings_covid',
                          'matplotlib.backends.backend_tkagg', 'yfinance'],
        'max-line-length': 200,
        'disable': ['R1705', 'C0200']
    })
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
