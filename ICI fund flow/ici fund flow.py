import pandas as pd
import matplotlib.pyplot as plt


class ICIFundfLow:

    def __init__(self):
        self.data = pd.read_excel('mm_summary_data_2022.xls').set_index('Date')

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


ici = ICIFundfLow()
ici.value()
ici.change()
