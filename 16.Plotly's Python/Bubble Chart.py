__author__ = 'xilin'
# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/
# You can reproduce this figure in Python with the following code!
# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

from plotly.graph_objs import *
py.sign_in('yydxlv', '29w25y7u88')
import plotly.plotly as py
trace1 = Scatter(
    x=[6223.367465, 4797.231267, 1441.284873, 12569.851770000001, 1217.032994, 430.07069160000003, 2042.0952399999999, 706.016537, 1704.0637239999999, 986.1478792000001, 277.55185869999997, 3632.557798, 1544.750112, 2082.4815670000003, 5581.180998, 12154.08975, 641.3695236000001, 690.8055759, 13206.48452, 752.7497265, 1327.60891, 942.6542111, 579.2317429999999, 1463.249282, 1569.331442, 414.5073415, 12057.49928, 1044.770126, 759.3499101, 1042.581557, 1803.1514960000002, 10956.99112, 3820.17523, 823.6856205, 4811.060429, 619.6768923999999, 2013.9773050000001, 7670.122558, 863.0884639000001, 1598.435089, 1712.4721359999999, 862.5407561000001, 926.1410683, 9269.657808, 2602.394995, 4513.480643, 1107.482182, 882.9699437999999, 7092.923025, 1056.3801210000001, 1271.211593, 469.70929810000007],
    y=[72.301, 42.731, 56.728, 50.728, 52.295, 49.58, 50.43, 44.74100000000001, 50.651, 65.152, 46.461999999999996, 55.321999999999996, 48.328, 54.791000000000004, 71.33800000000001, 51.57899999999999, 58.04, 52.946999999999996, 56.735, 59.448, 60.022, 56.007, 46.388000000000005, 54.11, 42.592, 45.678000000000004, 73.952, 59.443000000000005, 48.303000000000004, 54.467, 64.164, 72.801, 71.164, 42.082, 52.906000000000006, 56.867, 46.858999999999995, 76.442, 46.242, 65.528, 63.062, 42.568000000000005, 48.159, 49.339, 58.556000000000004, 39.613, 52.516999999999996, 58.42, 73.923, 51.542, 42.38399999999999, 43.486999999999995],
    marker=Marker(
        color='#2ca02c',
        line=Line(
            width=0.0
        ),
        opacity=0.6,
        size=[33333216.0, 12420476.0, 8078314.0, 1639131.0, 14326203.0, 8390505.0, 17696293.0, 4369038.0, 10238807.0, 710960.0, 64606759.0, 3800610.0, 18013409.0, 496374.0, 80264543.0, 551201.0, 4906585.0, 76511887.0, 1454867.0, 1688359.0, 22873338.0, 9947814.0, 1472041.0, 35610177.0, 2012649.0, 3193942.0, 6036914.0, 19167654.0, 13327079.0, 12031795.0, 3270065.0, 1250882.0, 33757175.0, 19951656.0, 2055080.0, 12894865.0, 135031164.0, 798094.0, 8860588.0, 199579.0, 12267493.0, 6144562.0, 9118773.0, 43997828.0, 42292929.0, 1133066.0, 38139640.0, 5701579.0, 10276158.0, 29170398.0, 11746035.0, 12311143.0],
        sizemode='area',
        sizeref=131868.3096
    ),
    mode='markers',
    name='Africa',
    text=['Country: Algeria    <br>Life Expectancy: 72.301 years    <br>GDP per capita: 6223.367465 $    <br>Population: 33.333216 million', 'Country: Angola    <br>Life Expectancy: 42.731 years    <br>GDP per capita: 4797.231267 $    <br>Population: 12.420476 million', 'Country: Benin    <br>Life Expectancy: 56.728 years    <br>GDP per capita: 1441.284873 $    <br>Population: 8.078314 million', 'Country: Botswana    <br>Life Expectancy: 50.728 years    <br>GDP per capita: 12569.85177 $    <br>Population: 1.639131 million', 'Country: Burkina Faso    <br>Life Expectancy: 52.295 years    <br>GDP per capita: 1217.032994 $    <br>Population: 14.326203 million', 'Country: Burundi    <br>Life Expectancy: 49.58 years    <br>GDP per capita: 430.0706916 $    <br>Population: 8.390505 million', 'Country: Cameroon    <br>Life Expectancy: 50.43 years    <br>GDP per capita: 2042.09524 $    <br>Population: 17.696293 million', 'Country: Central African Republic    <br>Life Expectancy: 44.741 years    <br>GDP per capita: 706.016537 $    <br>Population: 4.369038 million', 'Country: Chad    <br>Life Expectancy: 50.651 years    <br>GDP per capita: 1704.063724 $    <br>Population: 10.238807 million', 'Country: Comoros    <br>Life Expectancy: 65.152 years    <br>GDP per capita: 986.1478792 $    <br>Population: 0.71096 million', 'Country: Congo, Dem. Rep.    <br>Life Expectancy: 46.462 years    <br>GDP per capita: 277.5518587 $    <br>Population: 64.606759 million', 'Country: Congo, Rep.    <br>Life Expectancy: 55.322 years    <br>GDP per capita: 3632.557798 $    <br>Population: 3.80061 million', "Country: Cote d'Ivoire    <br>Life Expectancy: 48.328 years    <br>GDP per capita: 1544.750112 $    <br>Population: 18.013409 million", 'Country: Djibouti    <br>Life Expectancy: 54.791 years    <br>GDP per capita: 2082.481567 $    <br>Population: 0.496374 million', 'Country: Egypt    <br>Life Expectancy: 71.338 years    <br>GDP per capita: 5581.180998 $    <br>Population: 80.264543 million', 'Country: Equatorial Guinea    <br>Life Expectancy: 51.579 years    <br>GDP per capita: 12154.08975 $    <br>Population: 0.551201 million', 'Country: Eritrea    <br>Life Expectancy: 58.04 years    <br>GDP per capita: 641.3695236 $    <br>Population: 4.906585 million', 'Country: Ethiopia    <br>Life Expectancy: 52.947 years    <br>GDP per capita: 690.8055759 $    <br>Population: 76.511887 million', 'Country: Gabon    <br>Life Expectancy: 56.735 years    <br>GDP per capita: 13206.48452 $    <br>Population: 1.454867 million', 'Country: Gambia    <br>Life Expectancy: 59.448 years    <br>GDP per capita: 752.7497265 $    <br>Population: 1.688359 million', 'Country: Ghana    <br>Life Expectancy: 60.022 years    <br>GDP per capita: 1327.60891 $    <br>Population: 22.873338 million', 'Country: Guinea    <br>Life Expectancy: 56.007 years    <br>GDP per capita: 942.6542111 $    <br>Population: 9.947814 million', 'Country: Guinea-Bissau    <br>Life Expectancy: 46.388 years    <br>GDP per capita: 579.231743 $    <br>Population: 1.472041 million', 'Country: Kenya    <br>Life Expectancy: 54.11 years    <br>GDP per capita: 1463.249282 $    <br>Population: 35.610177 million', 'Country: Lesotho    <br>Life Expectancy: 42.592 years    <br>GDP per capita: 1569.331442 $    <br>Population: 2.012649 million', 'Country: Liberia    <br>Life Expectancy: 45.678 years    <br>GDP per capita: 414.5073415 $    <br>Population: 3.193942 million', 'Country: Libya    <br>Life Expectancy: 73.952 years    <br>GDP per capita: 12057.49928 $    <br>Population: 6.036914 million', 'Country: Madagascar    <br>Life Expectancy: 59.443 years    <br>GDP per capita: 1044.770126 $    <br>Population: 19.167654 million', 'Country: Malawi    <br>Life Expectancy: 48.303 years    <br>GDP per capita: 759.3499101 $    <br>Population: 13.327079 million', 'Country: Mali    <br>Life Expectancy: 54.467 years    <br>GDP per capita: 1042.581557 $    <br>Population: 12.031795 million', 'Country: Mauritania    <br>Life Expectancy: 64.164 years    <br>GDP per capita: 1803.151496 $    <br>Population: 3.270065 million', 'Country: Mauritius    <br>Life Expectancy: 72.801 years    <br>GDP per capita: 10956.99112 $    <br>Population: 1.250882 million', 'Country: Morocco    <br>Life Expectancy: 71.164 years    <br>GDP per capita: 3820.17523 $    <br>Population: 33.757175 million', 'Country: Mozambique    <br>Life Expectancy: 42.082 years    <br>GDP per capita: 823.6856205 $    <br>Population: 19.951656 million', 'Country: Namibia    <br>Life Expectancy: 52.906 years    <br>GDP per capita: 4811.060429 $    <br>Population: 2.05508 million', 'Country: Niger    <br>Life Expectancy: 56.867 years    <br>GDP per capita: 619.6768924 $    <br>Population: 12.894865 million', 'Country: Nigeria    <br>Life Expectancy: 46.859 years    <br>GDP per capita: 2013.977305 $    <br>Population: 135.031164 million', 'Country: Reunion    <br>Life Expectancy: 76.442 years    <br>GDP per capita: 7670.122558 $    <br>Population: 0.798094 million', 'Country: Rwanda    <br>Life Expectancy: 46.242 years    <br>GDP per capita: 863.0884639 $    <br>Population: 8.860588 million', 'Country: Sao Tome and Principe    <br>Life Expectancy: 65.528 years    <br>GDP per capita: 1598.435089 $    <br>Population: 0.199579 million', 'Country: Senegal    <br>Life Expectancy: 63.062 years    <br>GDP per capita: 1712.472136 $    <br>Population: 12.267493 million', 'Country: Sierra Leone    <br>Life Expectancy: 42.568 years    <br>GDP per capita: 862.5407561 $    <br>Population: 6.144562 million', 'Country: Somalia    <br>Life Expectancy: 48.159 years    <br>GDP per capita: 926.1410683 $    <br>Population: 9.118773 million', 'Country: South Africa    <br>Life Expectancy: 49.339 years    <br>GDP per capita: 9269.657808 $    <br>Population: 43.997828 million', 'Country: Sudan    <br>Life Expectancy: 58.556 years    <br>GDP per capita: 2602.394995 $    <br>Population: 42.292929 million', 'Country: Swaziland    <br>Life Expectancy: 39.613 years    <br>GDP per capita: 4513.480643 $    <br>Population: 1.133066 million', 'Country: Tanzania    <br>Life Expectancy: 52.517 years    <br>GDP per capita: 1107.482182 $    <br>Population: 38.13964 million', 'Country: Togo    <br>Life Expectancy: 58.42 years    <br>GDP per capita: 882.9699438 $    <br>Population: 5.701579 million', 'Country: Tunisia    <br>Life Expectancy: 73.923 years    <br>GDP per capita: 7092.923025 $    <br>Population: 10.276158 million', 'Country: Uganda    <br>Life Expectancy: 51.542 years    <br>GDP per capita: 1056.380121 $    <br>Population: 29.170398 million', 'Country: Zambia    <br>Life Expectancy: 42.384 years    <br>GDP per capita: 1271.211593 $    <br>Population: 11.746035 million', 'Country: Zimbabwe    <br>Life Expectancy: 43.487 years    <br>GDP per capita: 469.7092981 $    <br>Population: 12.311143 million']
)
trace2 = Scatter(
    x=[12779.379640000001, 3822.1370840000004, 9065.800825, 36319.235010000004, 13171.63885, 7006.580419, 9645.06142, 8948.102923, 6025.374752000001, 6873.262326000001, 5728.353514, 5186.050003, 1201.637154, 3548.3308460000003, 7320.880262000001, 11977.57496, 2749.320965, 9809.185636, 4172.838464, 7408.905561, 19328.70901, 18008.50924, 42951.65309, 10611.46299, 11415.805690000001],
    y=[75.32, 65.554, 72.39, 80.653, 78.553, 72.889, 78.782, 78.273, 72.235, 74.994, 71.878, 70.259, 60.916000000000004, 70.19800000000001, 72.567, 76.195, 72.899, 75.53699999999999, 71.752, 71.421, 78.74600000000001, 69.819, 78.242, 76.384, 73.747],
    marker=Marker(
        color='#d62728',
        line=Line(
            width=0.0
        ),
        opacity=0.6,
        size=[40301927.0, 9119152.0, 190010647.0, 33390141.0, 16284741.0, 44227550.0, 4133884.0, 11416987.0, 9319622.0, 13755680.0, 6939688.0, 12572928.0, 8502814.0, 7483763.0, 2780132.0, 108700891.0, 5675356.0, 3242173.0, 6667147.0, 28674757.0, 3942491.0, 1056608.0, 301139947.0, 3447496.0, 26084662.0],
        sizemode='area',
        sizeref=131868.3096
    ),
    mode='markers',
    name='Americas',
    text=['Country: Argentina    <br>Life Expectancy: 75.32 years    <br>GDP per capita: 12779.37964 $    <br>Population: 40.301927 million', 'Country: Bolivia    <br>Life Expectancy: 65.554 years    <br>GDP per capita: 3822.137084 $    <br>Population: 9.119152 million', 'Country: Brazil    <br>Life Expectancy: 72.39 years    <br>GDP per capita: 9065.800825 $    <br>Population: 190.010647 million', 'Country: Canada    <br>Life Expectancy: 80.653 years    <br>GDP per capita: 36319.23501 $    <br>Population: 33.390141 million', 'Country: Chile    <br>Life Expectancy: 78.553 years    <br>GDP per capita: 13171.63885 $    <br>Population: 16.284741 million', 'Country: Colombia    <br>Life Expectancy: 72.889 years    <br>GDP per capita: 7006.580419 $    <br>Population: 44.22755 million', 'Country: Costa Rica    <br>Life Expectancy: 78.782 years    <br>GDP per capita: 9645.06142 $    <br>Population: 4.133884 million', 'Country: Cuba    <br>Life Expectancy: 78.273 years    <br>GDP per capita: 8948.102923 $    <br>Population: 11.416987 million', 'Country: Dominican Republic    <br>Life Expectancy: 72.235 years    <br>GDP per capita: 6025.374752 $    <br>Population: 9.319622 million', 'Country: Ecuador    <br>Life Expectancy: 74.994 years    <br>GDP per capita: 6873.262326 $    <br>Population: 13.75568 million', 'Country: El Salvador    <br>Life Expectancy: 71.878 years    <br>GDP per capita: 5728.353514 $    <br>Population: 6.939688 million', 'Country: Guatemala    <br>Life Expectancy: 70.259 years    <br>GDP per capita: 5186.050003 $    <br>Population: 12.572928 million', 'Country: Haiti    <br>Life Expectancy: 60.916 years    <br>GDP per capita: 1201.637154 $    <br>Population: 8.502814 million', 'Country: Honduras    <br>Life Expectancy: 70.198 years    <br>GDP per capita: 3548.330846 $    <br>Population: 7.483763 million', 'Country: Jamaica    <br>Life Expectancy: 72.567 years    <br>GDP per capita: 7320.880262 $    <br>Population: 2.780132 million', 'Country: Mexico    <br>Life Expectancy: 76.195 years    <br>GDP per capita: 11977.57496 $    <br>Population: 108.700891 million', 'Country: Nicaragua    <br>Life Expectancy: 72.899 years    <br>GDP per capita: 2749.320965 $    <br>Population: 5.675356 million', 'Country: Panama    <br>Life Expectancy: 75.537 years    <br>GDP per capita: 9809.185636 $    <br>Population: 3.242173 million', 'Country: Paraguay    <br>Life Expectancy: 71.752 years    <br>GDP per capita: 4172.838464 $    <br>Population: 6.667147 million', 'Country: Peru    <br>Life Expectancy: 71.421 years    <br>GDP per capita: 7408.905561 $    <br>Population: 28.674757 million', 'Country: Puerto Rico    <br>Life Expectancy: 78.746 years    <br>GDP per capita: 19328.70901 $    <br>Population: 3.942491 million', 'Country: Trinidad and Tobago    <br>Life Expectancy: 69.819 years    <br>GDP per capita: 18008.50924 $    <br>Population: 1.056608 million', 'Country: United States    <br>Life Expectancy: 78.242 years    <br>GDP per capita: 42951.65309 $    <br>Population: 301.139947 million', 'Country: Uruguay    <br>Life Expectancy: 76.384 years    <br>GDP per capita: 10611.46299 $    <br>Population: 3.447496 million', 'Country: Venezuela    <br>Life Expectancy: 73.747 years    <br>GDP per capita: 11415.80569 $    <br>Population: 26.084662 million']
)
trace3 = Scatter(
    x=[974.5803384, 29796.048339999998, 1391.253792, 1713.7786859999999, 4959.1148539999995, 39724.97867, 2452.210407, 3540.6515640000002, 11605.71449, 4471.061906, 25523.2771, 31656.06806, 4519.461171, 1593.06548, 23348.139730000003, 47306.98978, 10461.05868, 12451.6558, 3095.7722710000003, 944.0, 1091.359778, 22316.19287, 2605.94758, 3190.481016, 21654.83194, 47143.179639999995, 3970.0954070000003, 4184.548089, 28718.27684, 7458.3963269999995, 2441.576404, 3025.349798, 2280.769906],
    y=[43.828, 75.635, 64.062, 59.723, 72.961, 82.208, 64.69800000000001, 70.65, 70.964, 59.545, 80.745, 82.603, 72.535, 67.297, 78.623, 77.58800000000001, 71.993, 74.241, 66.803, 62.068999999999996, 63.785, 75.64, 65.483, 71.688, 72.777, 79.972, 72.396, 74.143, 78.4, 70.616, 74.249, 73.422, 62.698],
    marker=Marker(
        color='#1f77b4',
        line=Line(
            width=0.0
        ),
        opacity=0.6,
        size=[31889923.0, 708573.0, 150448339.0, 14131858.0, 1318683096.0, 6980412.0, 1110396331.0, 223547000.0, 69453570.0, 27499638.0, 6426679.0, 127467972.0, 6053193.0, 23301725.0, 49044790.0, 2505559.0, 3921278.0, 24821286.0, 2874127.0, 47761980.0, 28901790.0, 3204897.0, 169270617.0, 91077287.0, 27601038.0, 4553009.0, 20378239.0, 19314747.0, 23174294.0, 65068149.0, 85262356.0, 4018332.0, 22211743.0],
        sizemode='area',
        sizeref=131868.3096
    ),
    mode='markers',
    name='Asia',
    text=['Country: Afghanistan    <br>Life Expectancy: 43.828 years    <br>GDP per capita: 974.5803384 $    <br>Population: 31.889923 million', 'Country: Bahrain    <br>Life Expectancy: 75.635 years    <br>GDP per capita: 29796.04834 $    <br>Population: 0.708573 million', 'Country: Bangladesh    <br>Life Expectancy: 64.062 years    <br>GDP per capita: 1391.253792 $    <br>Population: 150.448339 million', 'Country: Cambodia    <br>Life Expectancy: 59.723 years    <br>GDP per capita: 1713.778686 $    <br>Population: 14.131858 million', 'Country: China    <br>Life Expectancy: 72.961 years    <br>GDP per capita: 4959.114854 $    <br>Population: 1318.683096 million', 'Country: Hong Kong, China    <br>Life Expectancy: 82.208 years    <br>GDP per capita: 39724.97867 $    <br>Population: 6.980412 million', 'Country: India    <br>Life Expectancy: 64.698 years    <br>GDP per capita: 2452.210407 $    <br>Population: 1110.396331 million', 'Country: Indonesia    <br>Life Expectancy: 70.65 years    <br>GDP per capita: 3540.651564 $    <br>Population: 223.547 million', 'Country: Iran    <br>Life Expectancy: 70.964 years    <br>GDP per capita: 11605.71449 $    <br>Population: 69.45357 million', 'Country: Iraq    <br>Life Expectancy: 59.545 years    <br>GDP per capita: 4471.061906 $    <br>Population: 27.499638 million', 'Country: Israel    <br>Life Expectancy: 80.745 years    <br>GDP per capita: 25523.2771 $    <br>Population: 6.426679 million', 'Country: Japan    <br>Life Expectancy: 82.603 years    <br>GDP per capita: 31656.06806 $    <br>Population: 127.467972 million', 'Country: Jordan    <br>Life Expectancy: 72.535 years    <br>GDP per capita: 4519.461171 $    <br>Population: 6.053193 million', 'Country: Korea, Dem. Rep.    <br>Life Expectancy: 67.297 years    <br>GDP per capita: 1593.06548 $    <br>Population: 23.301725 million', 'Country: Korea, Rep.    <br>Life Expectancy: 78.623 years    <br>GDP per capita: 23348.13973 $    <br>Population: 49.04479 million', 'Country: Kuwait    <br>Life Expectancy: 77.588 years    <br>GDP per capita: 47306.98978 $    <br>Population: 2.505559 million', 'Country: Lebanon    <br>Life Expectancy: 71.993 years    <br>GDP per capita: 10461.05868 $    <br>Population: 3.921278 million', 'Country: Malaysia    <br>Life Expectancy: 74.241 years    <br>GDP per capita: 12451.6558 $    <br>Population: 24.821286 million', 'Country: Mongolia    <br>Life Expectancy: 66.803 years    <br>GDP per capita: 3095.772271 $    <br>Population: 2.874127 million', 'Country: Myanmar    <br>Life Expectancy: 62.069 years    <br>GDP per capita: 944.0 $    <br>Population: 47.76198 million', 'Country: Nepal    <br>Life Expectancy: 63.785 years    <br>GDP per capita: 1091.359778 $    <br>Population: 28.90179 million', 'Country: Oman    <br>Life Expectancy: 75.64 years    <br>GDP per capita: 22316.19287 $    <br>Population: 3.204897 million', 'Country: Pakistan    <br>Life Expectancy: 65.483 years    <br>GDP per capita: 2605.94758 $    <br>Population: 169.270617 million', 'Country: Philippines    <br>Life Expectancy: 71.688 years    <br>GDP per capita: 3190.481016 $    <br>Population: 91.077287 million', 'Country: Saudi Arabia    <br>Life Expectancy: 72.777 years    <br>GDP per capita: 21654.83194 $    <br>Population: 27.601038 million', 'Country: Singapore    <br>Life Expectancy: 79.972 years    <br>GDP per capita: 47143.17964 $    <br>Population: 4.553009 million', 'Country: Sri Lanka    <br>Life Expectancy: 72.396 years    <br>GDP per capita: 3970.095407 $    <br>Population: 20.378239 million', 'Country: Syria    <br>Life Expectancy: 74.143 years    <br>GDP per capita: 4184.548089 $    <br>Population: 19.314747 million', 'Country: Taiwan    <br>Life Expectancy: 78.4 years    <br>GDP per capita: 28718.27684 $    <br>Population: 23.174294 million', 'Country: Thailand    <br>Life Expectancy: 70.616 years    <br>GDP per capita: 7458.396327 $    <br>Population: 65.068149 million', 'Country: Vietnam    <br>Life Expectancy: 74.249 years    <br>GDP per capita: 2441.576404 $    <br>Population: 85.262356 million', 'Country: West Bank and Gaza    <br>Life Expectancy: 73.422 years    <br>GDP per capita: 3025.349798 $    <br>Population: 4.018332 million', 'Country: Yemen, Rep.    <br>Life Expectancy: 62.698 years    <br>GDP per capita: 2280.769906 $    <br>Population: 22.211743 million']
)
trace4 = Scatter(
    x=[5937.029525999999, 36126.4927, 33692.60508, 7446.298803, 10680.79282, 14619.222719999998, 22833.30851, 35278.41874, 33207.0844, 30470.0167, 32170.37442, 27538.41188, 18008.94444, 36180.789189999996, 40675.99635, 28569.7197, 9253.896111, 36797.93332, 49357.19017, 15389.924680000002, 20509.64777, 10808.47561, 9786.534714, 18678.31435, 25768.25759, 28821.0637, 33859.74835, 37506.419069999996, 8458.276384, 33203.26128],
    y=[76.423, 79.829, 79.441, 74.852, 73.005, 75.748, 76.486, 78.332, 79.313, 80.657, 79.406, 79.483, 73.33800000000001, 81.757, 78.885, 80.546, 74.543, 79.762, 80.196, 75.563, 78.098, 72.476, 74.002, 74.663, 77.926, 80.941, 80.884, 81.70100000000001, 71.777, 79.425],
    marker=Marker(
        color='#ff7f0e',
        line=Line(
            width=0.0
        ),
        opacity=0.6,
        size=[3600523.0, 8199783.0, 10392226.0, 4552198.0, 7322858.0, 4493312.0, 10228744.0, 5468120.0, 5238460.0, 61083916.0, 82400996.0, 10706290.0, 9956108.0, 301931.0, 4109086.0, 58147733.0, 684736.0, 16570613.0, 4627926.0, 38518241.0, 10642836.0, 22276056.0, 10150265.0, 5447502.0, 2009245.0, 40448191.0, 9031088.0, 7554661.0, 71158647.0, 60776238.0],
        sizemode='area',
        sizeref=131868.3096
    ),
    mode='markers',
    name='Europe',
    text=['Country: Albania    <br>Life Expectancy: 76.423 years    <br>GDP per capita: 5937.029526 $    <br>Population: 3.600523 million', 'Country: Austria    <br>Life Expectancy: 79.829 years    <br>GDP per capita: 36126.4927 $    <br>Population: 8.199783 million', 'Country: Belgium    <br>Life Expectancy: 79.441 years    <br>GDP per capita: 33692.60508 $    <br>Population: 10.392226 million', 'Country: Bosnia and Herzegovina    <br>Life Expectancy: 74.852 years    <br>GDP per capita: 7446.298803 $    <br>Population: 4.552198 million', 'Country: Bulgaria    <br>Life Expectancy: 73.005 years    <br>GDP per capita: 10680.79282 $    <br>Population: 7.322858 million', 'Country: Croatia    <br>Life Expectancy: 75.748 years    <br>GDP per capita: 14619.22272 $    <br>Population: 4.493312 million', 'Country: Czech Republic    <br>Life Expectancy: 76.486 years    <br>GDP per capita: 22833.30851 $    <br>Population: 10.228744 million', 'Country: Denmark    <br>Life Expectancy: 78.332 years    <br>GDP per capita: 35278.41874 $    <br>Population: 5.46812 million', 'Country: Finland    <br>Life Expectancy: 79.313 years    <br>GDP per capita: 33207.0844 $    <br>Population: 5.23846 million', 'Country: France    <br>Life Expectancy: 80.657 years    <br>GDP per capita: 30470.0167 $    <br>Population: 61.083916 million', 'Country: Germany    <br>Life Expectancy: 79.406 years    <br>GDP per capita: 32170.37442 $    <br>Population: 82.400996 million', 'Country: Greece    <br>Life Expectancy: 79.483 years    <br>GDP per capita: 27538.41188 $    <br>Population: 10.70629 million', 'Country: Hungary    <br>Life Expectancy: 73.338 years    <br>GDP per capita: 18008.94444 $    <br>Population: 9.956108 million', 'Country: Iceland    <br>Life Expectancy: 81.757 years    <br>GDP per capita: 36180.78919 $    <br>Population: 0.301931 million', 'Country: Ireland    <br>Life Expectancy: 78.885 years    <br>GDP per capita: 40675.99635 $    <br>Population: 4.109086 million', 'Country: Italy    <br>Life Expectancy: 80.546 years    <br>GDP per capita: 28569.7197 $    <br>Population: 58.147733 million', 'Country: Montenegro    <br>Life Expectancy: 74.543 years    <br>GDP per capita: 9253.896111 $    <br>Population: 0.684736 million', 'Country: Netherlands    <br>Life Expectancy: 79.762 years    <br>GDP per capita: 36797.93332 $    <br>Population: 16.570613 million', 'Country: Norway    <br>Life Expectancy: 80.196 years    <br>GDP per capita: 49357.19017 $    <br>Population: 4.627926 million', 'Country: Poland    <br>Life Expectancy: 75.563 years    <br>GDP per capita: 15389.92468 $    <br>Population: 38.518241 million', 'Country: Portugal    <br>Life Expectancy: 78.098 years    <br>GDP per capita: 20509.64777 $    <br>Population: 10.642836 million', 'Country: Romania    <br>Life Expectancy: 72.476 years    <br>GDP per capita: 10808.47561 $    <br>Population: 22.276056 million', 'Country: Serbia    <br>Life Expectancy: 74.002 years    <br>GDP per capita: 9786.534714 $    <br>Population: 10.150265 million', 'Country: Slovak Republic    <br>Life Expectancy: 74.663 years    <br>GDP per capita: 18678.31435 $    <br>Population: 5.447502 million', 'Country: Slovenia    <br>Life Expectancy: 77.926 years    <br>GDP per capita: 25768.25759 $    <br>Population: 2.009245 million', 'Country: Spain    <br>Life Expectancy: 80.941 years    <br>GDP per capita: 28821.0637 $    <br>Population: 40.448191 million', 'Country: Sweden    <br>Life Expectancy: 80.884 years    <br>GDP per capita: 33859.74835 $    <br>Population: 9.031088 million', 'Country: Switzerland    <br>Life Expectancy: 81.701 years    <br>GDP per capita: 37506.41907 $    <br>Population: 7.554661 million', 'Country: Turkey    <br>Life Expectancy: 71.777 years    <br>GDP per capita: 8458.276384 $    <br>Population: 71.158647 million', 'Country: United Kingdom    <br>Life Expectancy: 79.425 years    <br>GDP per capita: 33203.26128 $    <br>Population: 60.776238 million']
)
trace5 = Scatter(
    x=[34435.367439999995, 25185.00911],
    y=[81.235, 80.204],
    marker=Marker(
        color='#9467bd',
        line=Line(
            width=0.0
        ),
        opacity=0.6,
        size=[20434176.0, 4115771.0],
        sizemode='area',
        sizeref=131868.3096
    ),
    mode='markers',
    name='Oceania',
    text=['Country: Australia    <br>Life Expectancy: 81.235 years    <br>GDP per capita: 34435.36744 $    <br>Population: 20.434176 million', 'Country: New Zealand    <br>Life Expectancy: 80.204 years    <br>GDP per capita: 25185.00911 $    <br>Population: 4.115771 million']
)
data = Data([trace1, trace2, trace3, trace4, trace5])
layout = Layout(
    annotations=Annotations([
        Annotation(
            x=0.02,
            y=0.98,
            bgcolor='#FFFFFF',
            borderpad=4,
            font=Font(
                size=14
            ),
            showarrow=False,
            text='Data source: GapMinder 2007',
            xref='paper',
            yref='paper'
        )
    ]),
    autosize=False,
    height=500,
    hovermode='closest',
    plot_bgcolor='#EFECEA',
    showlegend=False,
    title="Fig 3.1b: Hans Rosling's Bubble Chart for the year 2007",
    width=650,
    xaxis=XAxis(
        exponentformat='power',
        gridcolor='#FFFFFF',
        showexponent='all',
        ticklen=8,
        ticks='outside',
        tickwidth=1.5,
        title='Gross Domestic Product per Capita [in USD of the year 2000]',
        type='log',
        zeroline=False
    ),
    yaxis=YAxis(
        gridcolor='#FFFFFF',
        ticklen=8,
        ticks='outside',
        tickwidth=1.5,
        title='Life Expentancy [in years]',
        zeroline=False
    )
)
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)