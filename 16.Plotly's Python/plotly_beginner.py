__author__ = 'xilin'
import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('yydxlv', '29w25y7u88')
trace1 = Bar(
    x=['Marriott Hotels', 'Holiday Inn', 'Radisson', 'Sheraton', 'Westin', 'Hilton', 'Best Western', 'Double Tree', 'W Hotels', 'Crowne Plaza'],
    y=['40,091', 16246, 25129, 8598, 10360, 10008, 9444, 4402, 3946, 2634],
    error_x=ErrorX(
        copy_ystyle=True
    ),
    error_y=ErrorY(
        color='rgb(0, 67, 88)',
        thickness=1,
        width=1
    ),
    marker=Marker(
        color='rgb(19, 80, 91)',
        line=Line(
            color='#444',
            width=0
        )
    ),
    name='Positive',
    opacity=1,
    orientation='v',
    uid='f1c092'
)
trace2 = Bar(
    x=['Marriott Hotels', 'Holiday Inn', 'Radisson', 'Sheraton', 'Westin', 'Hilton', 'Best Western', 'Double Tree', 'W Hotels', 'Crowne Plaza'],
    y=['36,528', '29,539', '13,781', '14,070', '11,914', '10,759', '5,136', '4,831', '3,856', '4,230'],
    error_x=ErrorX(
        copy_ystyle=True
    ),
    error_y=ErrorY(
        color='rgb(31, 138, 112)',
        thickness=1,
        width=1
    ),
    marker=Marker(
        color='rgb(12, 116, 137)',
        line=Line(
            color='#444',
            width=0
        )
    ),
    name='Neutral',
    opacity=1,
    orientation='v',
    uid='376dc5'
)
trace3 = Bar(
    x=['Marriott Hotels', 'Holiday Inn', 'Radisson', 'Sheraton', 'Westin', 'Hilton', 'Best Western', 'Double Tree', 'W Hotels', 'Crowne Plaza'],
    y=[12473, 3938, 1621, 3648, 3626, 4253, 1988, 1503, 1166, 1117],
    error_x=ErrorX(
        copy_ystyle=True
    ),
    error_y=ErrorY(
        color='rgb(190, 219, 57)',
        thickness=1,
        width=1
    ),
    marker=Marker(
        color='rgb(17, 157, 164)',
        line=Line(
            color='#444',
            width=0
        )
    ),
    name='Negative',
    opacity=1,
    orientation='v',
    uid='6dd47d'
)
data = Data([trace1, trace2, trace3])
layout = Layout(
    autosize=False,
    bargap=0.2,
    bargroupgap=0,
    barmode='stack',
    barnorm='',
    dragmode='zoom',
    font=Font(
        color='#444',
        family='PT Sans Narrow, sans-serif',
        size=16
    ),
    height=600,
    hidesources=False,
    hovermode='x',
    legend=Legend(
        x=0.7479452054794521,
        y=0.9871794871794872,
        bgcolor='#fff',
        bordercolor='#444',
        borderwidth=0,
        font=Font(
            color='#444',
            family='PT Sans Narrow, sans-serif',
            size=16
        ),
        traceorder='normal'
    ),
    margin=Margin(
        b=125,
        l=100,
        pad=0
    ),
    paper_bgcolor='#fff',
    plot_bgcolor='#fff',
    separators='.,',
    showlegend=True,
    title='How Popular Hotel Chains Fare on Social Media',
    titlefont=dict(
        color='#444',
        family='Droid Serif, serif',
        size=22
    ),
    width=545,
    xaxis=XAxis(
        autorange=True,
        exponentformat='B',
        fixedrange=True,
        gridcolor='white',
        gridwidth=1,
        linecolor='rgba(152, 0, 0, 0.5)',
        linewidth=1.5,
        mirror=False,
        nticks=0,
        range=[-0.5, 9.5],
        rangemode='normal',
        showexponent='all',
        showgrid=False,
        showline=False,
        showticklabels=True,
        tickangle=-45,
        tickcolor='rgba(0, 0, 0, 0)',
        tickfont=dict(
            color='#444',
            family='PT Sans Narrow, sans-serif',
            size=16
        ),
        ticklen=6,
        tickmode='auto',
        ticks='',
        title='<br> <br>Source: <a href="http://www.crimsonhexagon.com">Crimson Hexagon</a><br>Chart by <a href="http://www.fortune.com/author/stacy-jones">Stacy Jones, DataEditor, Fortune.com</a>',
        titlefont=dict(
            color='#444',
            family='Droid Sans, sans-serif',
            size=10
        ),
        type='category',
        zeroline=False,
        zerolinewidth=1
    ),
    yaxis=YAxis(
        autorange=True,
        fixedrange=True,
        gridcolor='rgb(204, 204, 204)',
        gridwidth=1,
        linecolor='rgba(152, 0, 0, 0.5)',
        linewidth=1.5,
        mirror=False,
        nticks=0,
        range=[0, 93781.05263157895],
        rangemode='normal',
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickangle='auto',
        tickcolor='rgba(0, 0, 0, 0)',
        tickfont=dict(
            color='#444',
            family='PT Sans Narrow, sans-serif',
            size=16
        ),
        ticklen=6,
        tickmode='auto',
        ticks='',
        title='Tweets (Jan. 1, 2015- June 14, 2015)',
        titlefont=dict(
            color='#444',
            family='Droid Serif, serif',
            size=16
        ),
        type='linear',
        zeroline=True,
        zerolinecolor='#444',
        zerolinewidth=1
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)