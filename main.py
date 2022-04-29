import csv
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
 #pro

df = pd.read_csv('data.csv')
fig = ff.create_distplot([df['Avg Rating'].tolist()], ['Avg Rating'])
fig.show()