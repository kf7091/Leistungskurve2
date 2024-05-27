import plotly.graph_objects as go
from my_functions import read_activity_data, create_powercurve

activity_data = read_activity_data()
power_curve = create_powercurve(activity_data['PowerOriginal'], activity_data['Time'])

# create figure
fig = go.Figure(data=go.Scatter(
    x=power_curve['Duration'],
    y=power_curve['Power'],
    mode='lines'
    ))
# add title to axis
fig.update_layout(
    title='Powercurve',
    xaxis_title='Zeit / s',
    yaxis_title='Leistung / W',
    )

fig.show()