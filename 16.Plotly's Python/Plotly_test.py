__author__ = 'xilin'
import urllib       # (*) urllib2 for in-session downloads
from urllib.request import urlopen
import pandas as pd  # (*) pandas for dataframe manipulation
import plotly
import plotly.plotly as py
import plotly.tools as tls
from plotly.graph_objs import *
import numpy as np
import plotly.plotly as py
import matplotlib.pyplot as plt
# Package all mpl plotting commands inside one function
def plot_mpl_fig():
    # Make two time arrays
    t1 = np.arange(0.0, 2.0, 0.1)
    t2 = np.arange(0.0, 2.0, 0.01)

    # N.B. .plot() returns a list of lines.
    # The "l1, = plot" usage extracts the first element of the list
    # into l1 using tuple unpacking.
    # So, l1 is a Line2D instance, not a sequence of lines
    l1, = plt.plot(t2, np.exp(-t2), label='decaying exp.')
    l2, l3 = plt.plot(t2, np.sin(2 * np.pi * t2), '--go',
                      t1, np.log(1 + t1), '.')
    l4, = plt.plot(t2, np.exp(-t2) * np.sin(2 * np.pi * t2), 'rs-.')

    # Add axis labels and title
    plt.xlabel('time')
    plt.ylabel('volts')
    plt.title('Damped oscillation')
    return (l1, l2, l3, l4)  # return line objects (for legend, later)
if __name__=="__main__":
    plot_mpl_fig()
    mpl_fig1 = plt.gcf()
    py_fig1 = tls.mpl_to_plotly(mpl_fig1, verbose=True)
    print(py_fig1.to_string())
    for i in ['autosize', 'width', 'height']:
        print(i, py_fig1['layout'][i])
    py.iplot_mpl(mpl_fig1, filename='s6_damped_oscillation')
    py.iplot_mpl(mpl_fig1, strip_style=True, filename='s6_damped_oscillation-default-style')

# Import data file from URL into pd datafram in session
data_url = 'http://datasets.flowingdata.com/crimeRatesByState2005.csv'
data_file = urlopen(data_url)
df = pd.read_csv(data_file, sep=',')

df = df.drop(df.index[0])  # drop first row (US totals)
df = df[df['murder'] < 11] # drop out-of-range rows

mpl_fig_bubble = plt.figure()         # (!) set new mpl figure object
ax = mpl_fig_bubble.add_subplot(111)  # add axis

plt.axis([0,11,200,1280])
plt.xlabel('Murders per 100,000 population')
plt.ylabel('Burglaries per 100,000 population')

scatter = ax.scatter(
    df['murder'],
    df['burglary'],
    c=df['larceny_theft'],        # using some color scale
    s=np.sqrt(df['population']),
    linewidths=2,
    edgecolor='w',
    alpha=0.6
)

for i_X, X in df.iterrows():
    plt.text(
        X['murder'],
        X['burglary'],
        X['state'][0:8], # only the first 8 letters
        size=8,
        horizontalalignment='center'
    )
py.iplot_mpl(mpl_fig_bubble, filename='s6_bubble-chart')