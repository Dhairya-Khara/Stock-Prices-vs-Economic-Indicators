"""User Interface"""
import statistics
import urllib.error
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from unemployment_before import UnemploymentBefore
from unemployment_covid import UnemploymentCovid
from job_openings_before import JobOpeningsBefore
from job_openings_covid import JobOpeningsCovid
from graph import get_r_squared, Graph

matplotlib.use("TkAgg")
plt.rcParams.update({'figure.max_open_warning': 0})

GRAPH_BG_COLOUR = '#343a40'
DOTS_COLOUR = '#f1faee'
TREND_LINE_COLOUR = '#e63946'


def draw_graph(graph: Graph, title: str, x_label: str, y_label: str, starting_month: int) -> plt.Figure:
    """"Returns fig which is a MatPlotLib graph plotting the x_label vs the y_label beginning with the starting_month"""
    x, y = graph.return_info_to_graph(starting_month)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title(title,
              {'fontname': 'Franklin Gothic Medium'})
    plt.title(title)

    r_squared = round(get_r_squared(x, y), 2)
    r_squared_text = "R\N{SUPERSCRIPT TWO} = " + str(r_squared)

    font = {'fontname': 'Franklin Gothic Medium', 'color': 'white', 'size': 9}

    ax.text(1.01, 0.9, r_squared_text, transform=ax.transAxes, fontdict=font)

    plt.plot(x, y, 'o', color=DOTS_COLOUR)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    m, b = np.polyfit(x, y, 1)
    plt.plot(x, m * x + b, color=TREND_LINE_COLOUR)

    fig.set_dpi(60)
    ax.spines['left'].set_color('#EEEEEE')
    ax.spines['bottom'].set_color('#EEEEEE')
    ax.xaxis.label.set_color('#EEEEEE')
    ax.yaxis.label.set_color('#EEEEEE')
    ax.title.set_color('#EEEEEE')
    ax.tick_params(axis='x', colors='#EEEEEE')
    ax.tick_params(axis='y', colors='#EEEEEE')
    ax.set_facecolor(GRAPH_BG_COLOUR)
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
    fig.patch.set_facecolor(GRAPH_BG_COLOUR)
    fig.set_dpi(70)

    font = {'fontname': 'Franklin Gothic Medium', 'color': 'white', 'size': 12}
    plt.text(140, 585, 'Cannot find stock. Try a different ticker.',
             fontdict=font)
    return fig


# Function to draw graph
def draw_figure(canvas: sg.Canvas.TKCanvas, figure: plt.Figure) -> FigureCanvasTkAgg:
    """ Returns figure on the given PySimpleGUI canvas"""
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


FIGURE_X, FIGURE_Y, FIGURE_W, FIGURE_H = get_unemployment_covid("AAPL", "Apple").bbox.bounds

LAYOUT = [
    [sg.Text('Enter Stock Ticker', font='Franklin_Gothic_Medium', background_color='#232323', text_color='#EEEEEE')],
    [sg.Input(key='-INPUT-', background_color='#757575', text_color='#000000'),
     sg.Button('Search', button_color=('#000000', '#757575'))],
    [sg.Canvas(size=(FIGURE_W, FIGURE_H * 0.9), key='-CANVAS-', background_color='#232323'),
     sg.Canvas(size=(FIGURE_W, FIGURE_H * 0.9), key='-CANVAS1-', background_color='#232323')],

    [sg.Canvas(size=(FIGURE_W, FIGURE_H * 0.9), key='-CANVAS2-', background_color='#232323'),
     sg.Canvas(size=(FIGURE_W, FIGURE_H * 0.9), key='-CANVAS3-', background_color='#232323')]]

# logic for window
WINDOW = sg.Window('Stock Correlation',
                   LAYOUT, force_toplevel=True, finalize=True, background_color='#232323', resizable=True)

# add the plot to the window

PHOTO_ERROR = PHOTO_UNEMPLOYMENT_COVID = draw_figure(WINDOW['-CANVAS1-'].TKCanvas,
                                                     get_unemployment_covid("AAPL", "Apple"))
PHOTO_UNEMPLOYMENT_BEFORE = draw_figure(WINDOW['-CANVAS-'].TKCanvas, get_unemployment_before("AAPL", "Apple"))
PHOTO_JOB_OPENINGS_COVID = draw_figure(WINDOW['-CANVAS3-'].TKCanvas, get_job_openings_covid("AAPL", "Apple"))
PHOTO_JOB_OPENINGS_BEFORE = draw_figure(WINDOW['-CANVAS2-'].TKCanvas, get_job_openings_before("AAPL", "Apple"))


def clear_ui(pe: FigureCanvasTkAgg, g1: FigureCanvasTkAgg, g2: FigureCanvasTkAgg,
             g3: FigureCanvasTkAgg, g4: FigureCanvasTkAgg) -> None:
    """Clears the UI"""
    pe.get_tk_widget().forget()
    g1.get_tk_widget().forget()
    g2.get_tk_widget().forget()
    g3.get_tk_widget().forget()
    g4.get_tk_widget().forget()


def main_loop(pe: FigureCanvasTkAgg, g1: FigureCanvasTkAgg, g2: FigureCanvasTkAgg,
              g3: FigureCanvasTkAgg, g4: FigureCanvasTkAgg) -> None:
    """ The main loop of the program which calls the functions to draw the canvases specific to the user's input """
    while True:
        # show it all again and get buttons
        event, values = WINDOW.read()
        if event in [sg.WIN_CLOSED, 'Exit']:
            break
        values['-INPUT-'] = ''.join(filter(str.isalnum, values['-INPUT-']))[:5]
        WINDOW['-INPUT-'].update(values['-INPUT-'])
        if event == 'Search':
            clear_ui(pe, g1, g2, g3, g4)
            try:
                stock_query = values['-INPUT-'].upper()
                ticker = yf.Ticker(stock_query)
                company_name = ticker.info['longName'].removesuffix(', Inc.').removesuffix(' Inc.')

                g1 = draw_figure(WINDOW['-CANVAS1-'].TKCanvas,
                                 get_unemployment_covid(values['-INPUT-'], company_name))
                g2 = draw_figure(WINDOW['-CANVAS-'].TKCanvas,
                                 get_unemployment_before(values['-INPUT-'], company_name))
                g3 = draw_figure(WINDOW['-CANVAS3-'].TKCanvas,
                                 get_job_openings_covid(values['-INPUT-'], company_name))
                g4 = draw_figure(WINDOW['-CANVAS2-'].TKCanvas,
                                 get_job_openings_before(values['-INPUT-'], company_name))

            except KeyError:
                clear_ui(pe, g1, g2, g3, g4)
                pe = draw_figure(WINDOW['-CANVAS-'].TKCanvas, error_fig())
            except statistics.StatisticsError:
                clear_ui(pe, g1, g2, g3, g4)
                pe = draw_figure(WINDOW['-CANVAS-'].TKCanvas, error_fig())
            except AttributeError:
                clear_ui(pe, g1, g2, g3, g4)
                pe = draw_figure(WINDOW['-CANVAS-'].TKCanvas, error_fig())
            except urllib.error.HTTPError:
                clear_ui(pe, g1, g2, g3, g4)
                pe = draw_figure(WINDOW['-CANVAS-'].TKCanvas, error_fig())
            except urllib.error.URLError:
                clear_ui(pe, g1, g2, g3, g4)
                pe = draw_figure(WINDOW['-CANVAS-'].TKCanvas, error_fig())


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
