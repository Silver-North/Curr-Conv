from requests import get


def get_currency():
    data = get(url="https://api.exchangerate-api.com/v4/latest/USD").json()
    return data.get('rates')


def exec_converter(from_curr, to_curr, curr):
    return round(get_currency()[to_curr] / get_currency()[from_curr] * curr, 2)
