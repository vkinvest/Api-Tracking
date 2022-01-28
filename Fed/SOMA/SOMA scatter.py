import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as go



url1 = 'https://markets.newyorkfed.org/api/soma/summary.csv'
soma = pd.read_csv(url1)
soma.set_index('As Of Date').sort_index()


def scatter():
    charts_list = []

    for col in soma.columns[1:]:
        charts_bar = go.Scatter(
            name=col,
            x=soma['As Of Date'],
            y=soma[col]
        )
        print(col)
        charts_list.append(charts_bar)
    fig_is = go.Figure(data=charts_list, layout=go.Layout(barmode='stack'))
    py.plot(fig_is, filename='Tesla historical PE ratios')


scatter()
