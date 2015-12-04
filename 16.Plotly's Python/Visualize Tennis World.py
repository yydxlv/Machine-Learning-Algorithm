# coding:utf-8
from random import shuffle
import colorsys
import pandas as pd
from plotly.offline import init_notebook_mode, iplot
from plotly.graph_objs import *
import plotly.plotly as py
py.sign_in('yydxlv', '29w25y7u88')

init_notebook_mode()
# There is nothing fancy in the code. We just did the following things:
#
# Loaded ATP players dataset into Pandas Dataframe
# We need to assign different random colors to each country. So created random RGB values
# Created a Scatter kind of plot with markers mode
# Created a layout with axis details
# plotted data and layout using iplot method of plotly library.

# Load players into players dataframe
players = pd.read_csv('data/atp_players.csv',skip_footer=1)

# Find top 20 countries with more player frequncies
countries = players.groupby(['country_code']).size()
selected_countries = countries.sort_values(ascending=False)[:20]

# Generating 20 random color palettes for plotting each country.
N = 20
HSV_tuples = [(x*1.0/N, 0.5, 0.5) for x in range(N)]
RGB_tuples = list(map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples))
shuffle(RGB_tuples)

plot_colors=RGB_tuples
""" Plot.ly plotting code. A plot.ly iplot needs data and a layout
    So now we prepare data and then layout. Here data is a scatter plot
"""
trace0 = Scatter(
    x = list(selected_countries.index),
    y = list(selected_countries.values),
    mode = 'markers',
    marker={'color': plot_colors, 'size': [30] * N}
)

# Data can be a list of plot types. You can have more than one scatter plots on figure
data = [trace0]

# layout has properties like x-axis label, y-axis label, background-color etc
layout = Layout(
    xaxis = {'title':"Country"}, # x-axis label
    yaxis = {'title':" No of ATP players produced"}, # y-axis label
    showlegend=False,
    height=600,  # height & width of plot
    width=600,
    paper_bgcolor='rgb(233,233,233)',
    plot_bgcolor='rgb(233,233,233)',  # background color of plot layout
)

# Build figure from data, layout and plot it.
# fig = Figure(data=data, layout=layout)
# iplot(fig)

fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)