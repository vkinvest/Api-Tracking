import pandas as pd
import matplotlib.pyplot as plt
import FundamentalAnalysis as fa
import datetime as dt
import json
from urllib.request import urlopen


class ICIFundfLow:
    def __init__(self):
        self.mmf = pd.read_excel('mm_summary_data_2022.xls').set_index('index')

    def mmf_amount(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.mmf['INSTITUTIONAL'], label='Institutional')
        plt.plot(self.mmf['RETAIL'], label='Retail')
        leg = plt.legend(loc='lower right')
        plt.show()

    def mmf_changes(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.mmf['change1'], label='Institutional % changes')
        plt.plot(self.mmf['change2'], label='Retail % changes')
        leg = plt.legend(loc='lower right')
        plt.show()

    @staticmethod
    def asset_classes():
        plt.figure(figsize=(12, 6))
        plt.plot(etf_mutual['equity'], label='equity')
        plt.plot(etf_mutual['bond'], label='bond')
        plt.plot(etf_mutual['commodity'], label='commodity')
        leg = plt.legend(loc='lower right')
        plt.title("Fund FLows of Asset CLasses and Estimates")
        plt.show()

    def inst_vs_index(self):
        def spx_hist_close():
            ticker = 'GSPC'
            begin = '2021-08-25'

            data_formatted = {}
            response = urlopen(f"https://financialmodelingprep.com/api/v3/historical-price-full/%5E{ticker}"
                               f"?from={str(begin)}&apikey={api_key}")
            data = json.loads(response.read().decode("utf-8"))

            data_json = data['historical']
            for value in data_json:
                date = value['date']
                del value['date']
                data_formatted[date] = value

            data_formatted = pd.DataFrame(data_formatted).T.sort_index()
            adjclose = data_formatted['adjClose']
            return adjclose

        compare = pd.DataFrame()
        compare['SP adjClose'] = spx_hist_close()
        compare['Institutional MMF'] = self.mmf['change1']
        compare.fillna(method='ffill', inplace=True)

        plt.figure(figsize=(12, 6))
        compare['SP adjClose'].plot(label='SP adjClose')
        y2 = compare['Institutional MMF'].plot(secondary_y=True, label='Institutional MMF %change')
        y2.set_ylim(-0.04, 0.04)
        plt.legend(loc='lower right')
        plt.title("Institutional MMF flows vs SP500 index")
        plt.show()


api_key = 'e95137f175e3fba84a1220c74e5ecd2a'
today = dt.date.today()
etf_mutual = pd.read_excel('combined_flows_data_2022-2.xls').set_index('index')

ici = ICIFundfLow()
ici.mmf_amount()
ici.mmf_changes()
ici.inst_vs_index()
ici.asset_classes()
