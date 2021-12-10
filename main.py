from user_interface import *
import yfinance as yf

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    values['-INPUT-'] = ''.join(filter(str.isalnum, values['-INPUT-']))[:5]
    window['-INPUT-'].update(values['-INPUT-'])
    if event == 'Search':
        photo_error.get_tk_widget().forget()
        photo_unemployment_covid.get_tk_widget().forget()
        photo_unemployment_before.get_tk_widget().forget()
        photo_job_openings_covid.get_tk_widget().forget()
        photo_job_openings_before.get_tk_widget().forget()
        try:
            stock_query = values['-INPUT-'].upper()
            ticker = yf.Ticker(stock_query)
            company_name = ticker.info['longName'].removesuffix(', Inc.').removesuffix(' Inc.')
            photo_unemployment_covid = draw_figure(window['-CANVAS1-'].TKCanvas,
                                                   get_unemployment_covid(values['-INPUT-'], company_name))
            photo_unemployment_before = draw_figure(window['-CANVAS-'].TKCanvas,
                                                    get_unemployment_before(values['-INPUT-'], company_name))
            photo_job_openings_covid = draw_figure(window['-CANVAS3-'].TKCanvas,
                                                   get_job_openings_covid(values['-INPUT-'], company_name))
            photo_job_openings_before = draw_figure(window['-CANVAS2-'].TKCanvas,
                                                    get_job_openings_before(values['-INPUT-'], company_name))
        except KeyError:
            photo_error.get_tk_widget().forget()
            photo_unemployment_covid.get_tk_widget().forget()
            photo_unemployment_before.get_tk_widget().forget()
            photo_job_openings_covid.get_tk_widget().forget()
            photo_job_openings_before.get_tk_widget().forget()
            print('The ticker you have entered is not an actual stock.')
            photo_error = draw_figure(window['-CANVAS-'].TKCanvas, error_fig())
        except statistics.StatisticsError:
            photo_error.get_tk_widget().forget()
            photo_unemployment_covid.get_tk_widget().forget()
            photo_unemployment_before.get_tk_widget().forget()
            photo_job_openings_covid.get_tk_widget().forget()
            photo_job_openings_before.get_tk_widget().forget()
            print('The ticker you have entered corresponds to a new stock that we don\'t have data for yet.')
            photo_error = draw_figure(window['-CANVAS-'].TKCanvas, error_fig())
