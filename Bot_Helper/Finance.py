import datetime
import requests
import xml.etree.ElementTree as ET
from datetime import date


class GetInfoAboutRate:

    def __init__(self):
        self.result = []

    def get_currency_rates(self):
        # Формируем URL запроса
        url = "http://www.cbr.ru/scripts/XML_daily.asp"
        params = {
            "date_req": date.today().strftime("%d/%m/%Y")
        }

        response = requests.get(url, params=params)
        root = ET.fromstring(response.content)
        currency_rates = {}

        for valute in root.findall(".//Valute"):
            code = valute.find("CharCode").text
            if code in ["USD", "EUR", "CNY", "JPY"]:
                rate = valute.find("Value").text
                currency_rates[code] = float(rate.replace(",", "."))
        self.result.append(f"Курсы валют на сегодняшний день: {datetime.datetime.now().strftime('%H:%M %d-%m-%Y')}")
        self.result.append("USD: {:.2f} RUB".format(currency_rates["USD"]))
        self.result.append("EUR: {:.2f} RUB".format(currency_rates["EUR"]))
        self.result.append("CNY: {:.2f} RUB".format(currency_rates["CNY"]))
        self.result.append("JPY: {:.2f} RUB".format(currency_rates["JPY"]))
        return self.result


def get_currency_rates():
    # Формируем URL запроса
    url = "http://www.cbr.ru/scripts/XML_daily.asp"
    params = {
        "date_req": date.today().strftime("%d/%m/%Y")
    }

    response = requests.get(url, params=params)
    root = ET.fromstring(response.content)
    currency_rates = {}

    for valute in root.findall(".//Valute"):
        code = valute.find("CharCode").text
        if code in ["USD", "EUR", "CNY", "JPY"]:
            rate = valute.find("Value").text
            currency_rates[code] = float(rate.replace(",", "."))
    return currency_rates


currency_rates = get_currency_rates()
print(f"Курсы валют на сегодняшний день: ({datetime.datetime.now().strftime('%Y-%m-%d %H:%M')})")
print("USD: {:.2f} RUB".format(currency_rates["USD"]))
print("EUR: {:.2f} RUB".format(currency_rates["EUR"]))
print("CNY: {:.2f} RUB".format(currency_rates["CNY"]))
print("JPY: {:.2f} RUB".format(currency_rates["JPY"]))
