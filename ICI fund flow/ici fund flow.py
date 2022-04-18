import pandas as pd
import matplotlib.pyplot as plt
import FundamentalAnalysis as fa
import datetime as dt
import json
from urllib.request import urlopen


class ICIFundfLow:
    def __init__(self):
        self.mmf = pd.read_excel('money_market_2022.xlsx').set_index('index')
        self.etf_mutual = pd.read_excel('etf_mutual_fund_2022.xlsx').set_index('index')

    def mmf_amount(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.mmf['INSTITUTIONAL'], label='Institutional')
        plt.plot(self.mmf['RETAIL'], label='Retail')
        plt.legend(loc='lower left')
        plt.show()

    def mmf_changes(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.mmf['change1'], label='Institutional % changes')
        plt.plot(self.mmf['change2'], label='Retail % changes')
        plt.legend(loc='lower right')
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

    def asset_classes(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.etf_mutual['equity'], label='equity')
        plt.plot(self.etf_mutual['bond'], label='bond')
        plt.plot(self.etf_mutual['commodity'], label='commodity')
        plt.title("Fund FLows of Asset CLasses and Estimates")
        plt.legend(loc='lower right')
        plt.show()

    def assets_pct(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.etf_mutual['change1'], label='equity')
        plt.plot(self.etf_mutual['change2'], label='bond')
        plt.plot(self.etf_mutual['change3'], label='commodity')
        plt.title("Pct Changes of Asset CLasses fund flows")
        plt.legend(loc='lower right')
        plt.show()

    def assets_pct_begin(self):
        from_date = '2021'
        etf_mutual = self.etf_mutual.loc[self.etf_mutual['Date'][from_date:]]
        plt.figure(figsize=(12, 6))
        plt.plot(etf_mutual['equity']/etf_mutual['equity'][0], label='equity')
        plt.plot(etf_mutual['bond']/etf_mutual['bond'][0], label='bond')
        plt.plot(etf_mutual['commodity']/etf_mutual['commodity'][0], label='commodity')
        plt.title(f"Pct Changes of Asset CLasses from {etf_mutual['Date'][0]}")
        plt.legend(loc='lower right')
        plt.show()


api_key = 'e95137f175e3fba84a1220c74e5ecd2a'
today = dt.date.today()

ici = ICIFundfLow()
ici.mmf_amount()
ici.mmf_changes()
ici.inst_vs_index()
ici.asset_classes()
ici.assets_pct()
ici.assets_pct_begin()