# https://plot.ly/python/offline/
import plotly
from plotly.graph_objs import *
import numpy as np
import plotly.plotly as py
import pandas as pd
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import cufflinks as cf
init_notebook_mode()
plotly.offline.init_notebook_mode()  # run at the start of every notebook
# plotly.offline.iplot({
#     "data": [{
#         "x": [1, 2, 3],
#         "y": [4, 2, 5]
#     }],
#     "layout": {
#         "title": "hello world"
#     }
# })
# iplot([Box(y = np.random.randn(50), showlegend=False) for i in range(45)], show_link=False)

# df = pd.read_csv('https://plot.ly/~etpinard/191.csv')
# data=[
#         Scatter(x=df[continent+'_Life Expentancy [in years]'],
#                 y=df[continent+'_Gross Domestic Product per Capita [in USD of the year 2000]'],
#                 text=df[continent+'_text'],
#                 marker=Marker(size=df[continent+'_marker.size'], sizemode='area', sizeref=131868,),
#                 mode='markers',
#                 name=continent) for continent in ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
#     ]
# layout=Layout(xaxis=XAxis(title='Life Expectancy'), yaxis=YAxis(title='GDP per Capita', type='log'))
# fig = Figure(data=data, layout=layout)
# plot_url = py.plot(fig)

# df_airports = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
# df_airports.head()
#
# df_flight_paths = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_aa_flight_paths.csv')
# df_flight_paths.head()
#
# airports = [ dict(
#         type = 'scattergeo',
#         locationmode = 'USA-states',
#         lon = df_airports['long'],
#         lat = df_airports['lat'],
#         hoverinfo = 'text',
#         text = df_airports['airport'],
#         mode = 'markers',
#         marker = dict(
#             size=2,
#             color='rgb(255, 0, 0)',
#             line = dict(
#                 width=3,
#                 color='rgba(68, 68, 68, 0)'
#             )
#         ))]
#
# flight_paths = []
# for i in range( len( df_flight_paths ) ):
#     flight_paths.append(
#         dict(
#             type = 'scattergeo',
#             locationmode = 'USA-states',
#             lon = [ df_flight_paths['start_lon'][i], df_flight_paths['end_lon'][i] ],
#             lat = [ df_flight_paths['start_lat'][i], df_flight_paths['end_lat'][i] ],
#             mode = 'lines',
#             line = dict(
#                 width = 1,
#                 color = 'red',
#             ),
#             opacity = float(df_flight_paths['cnt'][i])/float(df_flight_paths['cnt'].max()),
#         )
#     )
#
# layout = dict(
#         title = 'Feb. 2011 American Airline flight paths<br>(Hover for airport names)',
#         showlegend = False,
#         height = 800,
#         geo = dict(
#             scope='north america',
#             projection=dict( type='azimuthal equal area' ),
#             showland = True,
#             landcolor = 'rgb(243, 243, 243)',
#             countrycolor = 'rgb(204, 204, 204)',
#         ),
#     )
# fig = Figure(data=flight_paths + airports, layout=layout)
# plot_url = py.plot(fig)

plot_url = py.plot(cf.datagen.lines().iplot(asFigure=True,kind='scatter',xTitle='Dates',yTitle='Returns',title='Returns'))