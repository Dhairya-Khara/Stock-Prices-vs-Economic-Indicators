import pandas as pd
import requests

headers = {
    'authority': 'api.nasdaq.com',
    'accept': 'application/json, text/plain, */*',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36',
    'origin': 'https://www.nasdaq.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nasdaq.com/',
    'accept-language': 'en-US,en;q=0.9',
}
params = (
    ('tableonly', 'true'),
    ('limit', '25'),
    ('offset', '0'),
    ('download', 'true'),
)


def get_stocks():
    r = requests.get('https://api.nasdaq.com/api/screener/stocks', headers=headers, params=params)
    data = r.json()['data']
    df = pd.DataFrame(data['rows'], columns=data['headers'])
    df_filtered = df[~df['symbol'].str.contains("\.|\^")]
    return df_filtered['symbol'].tolist()


def get_top_five_stocks(stock_substring, tickers):
    """stuff"""
    top_five = []
    first_match_found = False
    try:
        for stock in tickers:
            if stock_substring in stock and len(top_five) < 5:
                first_match_found = True
                top_five.append(stock)
            else:
                if first_match_found:
                    break
        return top_five
    except ValueError or IndexError:
        return top_five

# Testing codes
# print(get_top_five_stocks('AA', tickers))
