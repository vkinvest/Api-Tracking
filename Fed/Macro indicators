import quandl
import matplotlib.pyplot as plt


def potential_gdp():
    gdp = quandl.get("FRED/GDP", authtoken=token)
    plt.figure(figsize=(12, 6))
    plt.title('Real Potential GDP', fontsize=14)
    plt.plot(gdp.Value)
    plt.show()

def gdp_growth():
    fomc_pred = quandl.get("FRED/GDPC1MD", authtoken=token)
    plt.figure(figsize=(12, 6))
    plt.title('FOMC Prediction of Real GDP Growth', fontsize=14)
    plt.plot(fomc_pred.Value)
    plt.show()

def unemployment():
    short_term = quandl.get("FRED/NROUST", authtoken=token)
    long_term = quandl.get("FRED/NROU", authtoken=token)
    plt.figure(figsize=(12, 6))
    plt.title('Rate of Unemployment', fontsize=14)
    plt.plot(short_term.Value)
    plt.plot(long_term.Value)
    plt.show()

def cpi():
    cpi = quandl.get("FRED/PCECTPIMD", authtoken=token)
    core_cpi = quandl.get("FRED/JCXFEMD", authtoken=token)
    plt.figure(figsize=(12, 6))
    plt.title('FOMC Prediction of Inflation Rate', fontsize=14)
    plt.plot(cpi.Value)
    plt.plot(core_cpi.Value)
    plt.show()


def fed_rate():
    mid = quandl.get("FRED/FEDTARRM", authtoken=token)
    low = quandl.get("FRED/FEDTARRL", authtoken=token)
    high = quandl.get("FRED/FEDTARRH", authtoken=token)
    plt.figure(figsize=(12, 6))
    plt.title('FOMC Prediction of Fed Funds Rate', fontsize=14)
    plt.plot(mid.Value)
    plt.plot(low.Value)
    plt.plot(high.Value)
    plt.show()

token ='9TqZsnUWPvsBMUoyRvKx'

potential_gdp()
gdp_growth()
unemployment()
cpi()
fed_rate()
