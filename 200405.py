>>> #matplotlib install
>>> #cmd에서 python -m pip install matplotlib 실행
>>> 
>>> #파이차트
>>> #1.라이브러리 선언
>>> import matplotlib.pyplot as plt
>>> import pandas as pd
>>> #2.데이터 설정
>>> df=pd.read_csv('pop_ratio.csv')
>>> #3.플롯
>>> plt.style.use('ggplot')
>>> colors = ['gold','yellowgreen','lightcoral','lightskyblue','red']
>>> plt.pie(df.ratio, explode=(0.1,0,0,0,0), labels=df.region, colors=colors)
([<matplotlib.patches.Wedge object at 0x00FA3070>, <matplotlib.patches.Wedge object at 0x00FA3250>, <matplotlib.patches.Wedge object at 0x00FA3530>, <matplotlib.patches.Wedge object at 0x00FA3810>, <matplotlib.patches.Wedge object at 0x00FA3C50>], [Text(0.7148391653909202, 0.9638490377767739, 'Seoul'), Text(-0.6552692349416768, 0.8835282846287095, 'Busan'), Text(-1.0526343693054299, 0.31931314497990865, 'Incheon'), Text(-0.370578838731442, -1.035698471701323, 'gyeong-gi'), Text(1.035698471701323, -0.37057883873144204, 'gyeongnam')])
>>> #4.플롯 꾸미기
>>> plt.title('Population by region')
Text(0.5, 1.0, 'Population by region')
>>> plt.savefig('pie_chart.png',dpi=400, bbox_inches='tight')
>>> plt.show()
>>> 
>>> #막대그래프
>>> #1.라이브러리 선언
>>> import matplotlib.pyplot as plt
>>> #2.데이터 설정
>>> customers=['ABC','DEF','GHI','JKL','MNO']
>>> customers_index = range(len(customers))
>>> sale_amounts=[127,90,201,111,232]
>>> #3.플롯
>>> plt.style.use('ggplot')
>>> fig=plt.figure()
>>> ax1 = fig.add_subplot(1,1,1)
>>> ax1.bar(customers_index,sale_amounts,align='center',color='darkblue')
<BarContainer object of 5 artists>
>>> #4.플롯 꾸미기
>>> ax1.xaxis.set_ticks_position('bottom')
>>> ax1.yaxis.set_ticks_position('left')
>>> plt.xticks(customers_index,customers,rotation=0,fontsize='small')
([<matplotlib.axis.XTick object at 0x0A7EF510>, <matplotlib.axis.XTick object at 0x0A7EF4F0>, <matplotlib.axis.XTick object at 0x0A7EF0D0>, <matplotlib.axis.XTick object at 0x0A6B36B0>, <matplotlib.axis.XTick object at 0x0A6B3C30>], [Text(0, 0, 'ABC'), Text(0, 0, 'DEF'), Text(0, 0, 'GHI'), Text(0, 0, 'JKL'), Text(0, 0, 'MNO')])
>>> plt.xlabel('Customer Name')
Text(0.5, 0, 'Customer Name')
>>> plt.ylabel('Sale Amount')
Text(0, 0.5, 'Sale Amount')
>>> plt.title('Sale Amount per Customer')
Text(0.5, 1.0, 'Sale Amount per Customer')
>>> plt.savefig('bar_plot.png',dpi=400,bbox_inches='tight')
>>> plt.show()
>>>
>>> #선그래프
>>> #1.라이브러리 선언
>>> from numpy.random import randn
>>> import matplotlib.pyplot as plt
>>> #2.데이터 설정
>>> plot_data1 = randn(50).cumsum()
>>> plot_data2 = randn(50).cumsum()
>>> plot_data3 = randn(50).cumsum()
>>> plot_data4 = randn(50).cumsum()
>>> #3.플롯
>>> plt.style.use('ggplot')
>>> fig=plt.figure()
>>> ax1=fig.add_subplot(1,1,1)
>>> ax1.plot(plot_data1, marker=r'o', color=u'blue', linestyle='-', label='Blue Solid')
[<matplotlib.lines.Line2D object at 0x0392FDF0>]
>>> ax1.plot(plot_data2, marker=r'+', color=u'red', linestyle='--', label='Red Dashed')
[<matplotlib.lines.Line2D object at 0x0393F150>]
>>> ax1.plot(plot_data3, marker=r'*', color=u'green', linestyle='-.', label='Green Dash Dot')
[<matplotlib.lines.Line2D object at 0x0393F3D0>]
>>> ax1.plot(plot_data4, marker=r's', color=u'orange', linestyle=':', label='Orange Dotted')
[<matplotlib.lines.Line2D object at 0x0393F5F0>]
>>> #4.플롯 꾸미기
>>> ax1.xaxis.set_ticks_position('bottom')
>>> ax1.yaxis.set_ticks_position('left')
>>> ax1.set_title('Line Plots: Markers, Colors, and Linestyles')
Text(0.5, 1.0, 'Line Plots: Markers, Colors, and Linestyles')
>>> plt.xlabel('Draw')
Text(0.5, 0, 'Draw')
>>> plt.ylabel('Random Number')
Text(0, 0.5, 'Random Number')
>>> plt.legend(loc='best')
<matplotlib.legend.Legend object at 0x0A6BB230>
>>> plt.savefig('line_plot.png',dpi=400,bbox_inches='tight')
>>> plt.show()
>>>
>>> #산점도
>>> #1.라이브러리 선언
>>> import matplotlib.pyplot as plt
>>> from random import shuffle
>>> #2.데이터 설정
>>> x=list(range(1,100))
>>> y=list(range(1,100))
>>> shuffle(x)
>>> shuffle(y)
>>> #3.플롯
>>> plt.style.use('ggplot')
>>> fig=plt.figure()
>>> ax1=fig.add_subplot(1,1,1)
>>> ax1.scatter(x,y,color='b',marker='o')
<matplotlib.collections.PathCollection object at 0x038DD670>
>>> #4.플롯 꾸미기
>>> ax1.xaxis.set_ticks_position('bottom')
>>> ax1.yaxis.set_ticks_position('left')
>>> ax1.set_title('Scatter plots')
Text(0.5, 1.0, 'Scatter plots')
>>> plt.xlabel('x')
Text(0.5, 0, 'x')
>>> plt.ylabel('y')
Text(0, 0.5, 'y')
>>> plt.xlim(min(x)-1.,max(x)+1.)
(0.0, 100.0)
>>> plt.ylim(min(y)-1.,max(y)+1.)
(0.0, 100.0)
>>> plt.savefig('scatter_plot.png',dpi=400,bbox_inches='tight')
>>> plt.show()
>>> 
