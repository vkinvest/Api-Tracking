import pandas as pd
import matplotlib.pyplot as plt
import FundamentalAnalysis as fa
import datetime as dt
import json
from urllib.request import urlopen


class ICIFundfLow:
    def __init__(self):
        self.data = pd.read_excel('mm_summary_data_2022.xls').set_index('index')

    def value(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['INSTITUTIONAL'])
        plt.plot(self.data['RETAIL'])
        plt.show()

    def change(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.data['change1'])
        plt.plot(self.data['change2'])
        plt.show()

    def inst_vs_index(self):
        def index():
            ticker = 'GSPC'
            api_key = 'e95137f175e3fba84a1220c74e5ecd2a'
            begin = '2021-08-25'
            end = "2022-03-30"

            data_formatted = {}
            response = urlopen(f"https://financialmodelingprep.com/api/v3/historical-price-full/%5E{ticker}"
                               f"?from={str(begin)}&to={str(end)}&apikey={api_key}")
            data = json.loads(response.read().decode("utf-8"))
            data_json = data['historical']

            for value in data_json:
                date = value['date']
                del value['date']
                data_formatted[date] = value
            data_formatted = pd.DataFrame(data_formatted).T
            adjclose = data_formatted['adjClose']
            return adjclose

        compare = pd.DataFrame()
        fig = plt.figure()
        compare['SP adjClose'] = index().sort_index()
        compare['Institutional MMF'] = self.data['change1']
        compare['Institutional MMF'].fillna(method='ffill', inplace=True)

        plt.figure(figsize=(12, 6))
        y1 = compare['SP adjClose'].plot()
        y2 = compare['Institutional MMF'].plot(secondary_y=True)
        y2.set_ylim(-0.04, 0.04)
        plt.show()


ticker = ['TSLA']
api_key = 'e95137f175e3fba84a1220c74e5ecd2a'
today = dt.date.today()


ici = ICIFundfLow()
# ici.value()
# ici.change()
ici.inst_vs_index()
