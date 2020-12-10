import pandas as pd

import plotly.express as px

filepath = pd.read_csv("C:/Users/HOME/Downloads/datacovid.csv")

data = px.line(filepath, x="date", y="cases",color="country")

data.show()