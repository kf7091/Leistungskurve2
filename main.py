import pandas as pd
import plotly.graph_objects as go
from my_functions import read_activity_data

activity_data = read_activity_data()

fig = go.Figure(data=go.Scatter(x=activity_data.index, y=activity_data['PowerOriginal'], mode='lines'))
fig.show()