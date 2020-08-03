import pandas as pd
sym = "TSLA"
token = "pk_b5d625633a9c414cad4afd764bea92b5"

df_temp = pd.read_json('https://cloud.iexapis.com/stable/stock/'+sym+'/chart/1y?token='+token+'')

df_temp.head(3)
print(df_temp.head(3))