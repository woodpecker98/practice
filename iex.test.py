import matplotlib.pyplot as plt
import pandas as pd
from iexfinance.stocks import Stock


# set parameters so all plots are consistent
plt.rcParams['figure.figsize'] = (20, 8)

# prettier plotting with seaborn
import seaborn as sns;

sns.set(font_scale=1.5)
sns.set_style("whitegrid")

tickerSymbol = input("Ticker Symbol: ")  ## taking in stock name

token = "pk_b5d625633a9c414cad4afd764bea92b5"
df_temp = pd.read_json('https://cloud.iexapis.com/stable/stock/' + tickerSymbol + '/chart/1y?token=' + token + '')

companyInfo = Stock(tickerSymbol)
stockPrice = companyInfo.get_price()

print("Current Stock Price:", stockPrice)
