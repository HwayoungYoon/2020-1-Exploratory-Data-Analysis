>>> #히스토그램
>>> #1.library import
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> #2.데이터 생성
>>> plt.style.use('ggplot')
>>> mu1,mu2,sigma=100,130,15
>>> x1 = mu1 + sigma*np.random.randn(10000)
>>> x2 = mu2 + sigma*np.random.randn(10000)
>>> #3.그림판 만들기
>>> fig=plt.figure()
>>> ax1 = fig.add_subplot(1,1,1)
>>> #4.히스토그램
>>> ax1.hist(x1, bins=50, color='g')
(array([  2.,   2.,   3.,   4.,   3.,   8.,  11.,  18.,  25.,  47.,  59.,
        77., 121., 150., 191., 226., 301., 364., 422., 459., 476., 550.,
       578., 606., 563., 607., 586., 550., 505., 441., 358., 365., 303.,
       273., 190., 150., 124.,  80.,  67.,  48.,  26.,  28.,  14.,   8.,
         6.,   4.,   0.,   0.,   0.,   1.]), array([ 43.77625442,  46.06247858,  48.34870274,  50.6349269 ,
        52.92115105,  55.20737521,  57.49359937,  59.77982353,
        62.06604769,  64.35227185,  66.63849601,  68.92472017,
        71.21094433,  73.49716849,  75.78339265,  78.06961681,
        80.35584096,  82.64206512,  84.92828928,  87.21451344,
        89.5007376 ,  91.78696176,  94.07318592,  96.35941008,
        98.64563424, 100.9318584 , 103.21808256, 105.50430671,
       107.79053087, 110.07675503, 112.36297919, 114.64920335,
       116.93542751, 119.22165167, 121.50787583, 123.79409999,
       126.08032415, 128.36654831, 130.65277247, 132.93899662,
       135.22522078, 137.51144494, 139.7976691 , 142.08389326,
       144.37011742, 146.65634158, 148.94256574, 151.2287899 ,
       153.51501406, 155.80123822, 158.08746238]), <a list of 50 Patch objects>)
>>> ax1.hist(x2, bins=50, color='r', alpha=0.5)
(array([  2.,   1.,   2.,   6.,   2.,   8.,  18.,  19.,  21.,  43.,  53.,
        74.,  98., 138., 191., 211., 249., 295., 408., 419., 447., 566.,
       538., 594., 562., 602., 573., 581., 567., 509., 453., 340., 264.,
       258., 210., 167., 151., 118.,  65.,  50.,  39.,  28.,  25.,  14.,
        12.,   3.,   2.,   0.,   2.,   2.]), array([ 73.56584832,  75.82131424,  78.07678016,  80.33224608,
        82.58771199,  84.84317791,  87.09864383,  89.35410974,
        91.60957566,  93.86504158,  96.1205075 ,  98.37597341,
       100.63143933, 102.88690525, 105.14237117, 107.39783708,
       109.653303  , 111.90876892, 114.16423484, 116.41970075,
       118.67516667, 120.93063259, 123.1860985 , 125.44156442,
       127.69703034, 129.95249626, 132.20796217, 134.46342809,
       136.71889401, 138.97435993, 141.22982584, 143.48529176,
       145.74075768, 147.99622359, 150.25168951, 152.50715543,
       154.76262135, 157.01808726, 159.27355318, 161.5290191 ,
       163.78448502, 166.03995093, 168.29541685, 170.55088277,
       172.80634869, 175.0618146 , 177.31728052, 179.57274644,
       181.82821235, 184.08367827, 186.33914419]), <a list of 50 Patch objects>)
>>> #5.히스토그램 꾸미기
>>> ax1.xaxis.set_ticks_position('bottom')
>>> ax1.yaxis.set_ticks_position('left')
>>> plt.xlabel('Bins')
Text(0.5, 0, 'Bins')
>>> plt.ylabel('Number of Values in Bin')
Text(0, 0.5, 'Number of Values in Bin')
>>> fig.suptitle('Histograms', fontsize=14, fontweight='bold')
Text(0.5, 0.98, 'Histograms')
>>> ax1.set_title('Two Frequency Distributions')
Text(0.5, 1.0, 'Two Frequency Distributions')
>>> plt.savefig('histogram.png', dpi=400, bbox_inches='tight')
>>> plt.show()
>>>
>>> #상자그림
>>> #1.library import
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> plt.style.use('ggplot')
>>> #2.데이터 생성
>>> N=500
>>> normal = np.random.normal(loc=0.0, scale=1.0, size=N)
>>> lognormal = np.random.lognormal(mean=0.0, sigma=1.0, size=N)
>>> box_plot_data = [normal, lognormal]
>>> #3.그림판 만들기
>>> fig = plt.figure()
>>> ax1 = fig.add_subplot(1,1,1)
>>> box_labels = ['normal','lognormal']
>>> #4.상자그림
>>> ax1.boxplot(box_plot_data, showmeans=True, labels=box_labels)
{'whiskers': [<matplotlib.lines.Line2D object at 0x098B73F0>, <matplotlib.lines.Line2D object at 0x098B7670>, <matplotlib.lines.Line2D object at 0x098C1850>, <matplotlib.lines.Line2D object at 0x098C1AD0>], 'caps': [<matplotlib.lines.Line2D object at 0x098B78F0>, <matplotlib.lines.Line2D object at 0x098B7B70>, <matplotlib.lines.Line2D object at 0x098C1D50>, <matplotlib.lines.Line2D object at 0x098C1FD0>], 'boxes': [<matplotlib.lines.Line2D object at 0x098B7190>, <matplotlib.lines.Line2D object at 0x098C15F0>], 'medians': [<matplotlib.lines.Line2D object at 0x098B7E10>, <matplotlib.lines.Line2D object at 0x098CC270>], 'fliers': [<matplotlib.lines.Line2D object at 0x098C1330>, <matplotlib.lines.Line2D object at 0x098CC770>], 'means': [<matplotlib.lines.Line2D object at 0x098C10B0>, <matplotlib.lines.Line2D object at 0x098CC4F0>]}
>>> #5.상자 꾸미기
>>> ax1.xaxis.set_ticks_position('bottom')
>>> ax1.yaxis.set_ticks_position('left')
>>> ax1.set_title('Box Plots: Two distributions')
Text(0.5, 1.0, 'Box Plots: Two distributions')a
>>> ax1.set_xlabel('Distribution')
Text(0.5, 0, 'Distribution')
>>> ax1.set_ylabel('Value')
Text(0, 0.5, 'Value')
>>> plt.savefig('box_plot.png', dpi=400, bbox_inches='tight')
>>> plt.show()
>>> 
>>> #seaborn install
>>> #cmd에서 python -m pip install seaborn 실행
>>> 
>>> #상관계수
>>> import pandas as pd
>>> wine_red = pd.read_csv('winequality-red.csv', sep=';', header=0)
>>> wine_white = pd.read_csv('winequality-white.csv', sep=';', header=0)
>>> wine_red.columns = wine_red.columns.str.replace(' ', '_')
>>> wine_white.columns = wine_white.columns.str.replace(' ', '_')
>>> print(wine_red.corr())
                      fixed_acidity  volatile_acidity  ...   alcohol   quality
fixed_acidity              1.000000         -0.256131  ... -0.061668  0.124052
volatile_acidity          -0.256131          1.000000  ... -0.202288 -0.390558
citric_acid                0.671703         -0.552496  ...  0.109903  0.226373
residual_sugar             0.114777          0.001918  ...  0.042075  0.013732
chlorides                  0.093705          0.061298  ... -0.221141 -0.128907
free_sulfur_dioxide       -0.153794         -0.010504  ... -0.069408 -0.050656
total_sulfur_dioxide      -0.113181          0.076470  ... -0.205654 -0.185100
density                    0.668047          0.022026  ... -0.496180 -0.174919
pH                        -0.682978          0.234937  ...  0.205633 -0.057731
sulphates                  0.183006         -0.260987  ...  0.093595  0.251397
alcohol                   -0.061668         -0.202288  ...  1.000000  0.476166
quality                    0.124052         -0.390558  ...  0.476166  1.000000

[12 rows x 12 columns]
>>> print(wine_white.corr())
                      fixed_acidity  volatile_acidity  ...   alcohol   quality
fixed_acidity              1.000000         -0.022697  ... -0.120881 -0.113663
volatile_acidity          -0.022697          1.000000  ...  0.067718 -0.194723
citric_acid                0.289181         -0.149472  ... -0.075729 -0.009209
residual_sugar             0.089021          0.064286  ... -0.450631 -0.097577
chlorides                  0.023086          0.070512  ... -0.360189 -0.209934
free_sulfur_dioxide       -0.049396         -0.097012  ... -0.250104  0.008158
total_sulfur_dioxide       0.091070          0.089261  ... -0.448892 -0.174737
density                    0.265331          0.027114  ... -0.780138 -0.307123
pH                        -0.425858         -0.031915  ...  0.121432  0.099427
sulphates                 -0.017143         -0.035728  ... -0.017433  0.053678
alcohol                   -0.120881          0.067718  ...  1.000000  0.435575
quality                   -0.113663         -0.194723  ...  0.435575  1.000000

[12 rows x 12 columns]
>>>
>>> #상관계수 시각화(wine_red)
>>> #1.library import
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> #2.데이터 생성
>>> wine_red = pd.read_csv('winequality-red.csv', sep=';', header=0)
>>> wine_red.columns = wine_red.columns.str.replace(' ', '_')
>>> #3.그림판 만들기
>>> plt.style.use('ggplot')
>>> fig = plt.figure()
>>> ax1 = fig.add_subplot(1,1,1)
>>> #4.상관계수 시각화 플롯
>>> sns.heatmap(wine_red.corr(), annot=True, cmap='RdYlGn')
<matplotlib.axes._subplots.AxesSubplot object at 0x09195710>
>>> #5.상관계수 시각화 플롯 꾸미기
>>> ax1.set_title('Correlations: Red Wine data')
Text(0.5, 1.0, 'Correlations: Red Wine data')
>>> plt.savefig('corr_wine_red.png', dpi=400, bbox_inches='tight')
>>> plt.show()
>>> #상관계수 시각화(wine_white)
>>> #1.library import
>>> import pandas as pd
>>> import matplotlib.pyplot as plt
>>> import seaborn as sns
>>> #2.데이터 생성
>>> wine_white = pd.read_csv('winequality-white.csv', sep=';', header=0)
>>> wine_white.columns = wine_white.columns.str.replace(' ', '_')
>>> #3.그림판 만들기
>>> plt.style.use('ggplot')
>>> fig = plt.figure()
>>> ax1 = fig.add_subplot(1,1,1)
>>> #4.상관계수 시각화 플롯
>>> sns.heatmap(wine_white.corr(), annot=True, cmap='RdYlGn')
<matplotlib.axes._subplots.AxesSubplot object at 0x039640F0>
>>> #5.상관계수 시각화 플롯 꾸미기
>>> ax1.set_title('Correlations: White Wine data')
Text(0.5, 1.0, 'Correlations: White Wine data')
>>> plt.savefig('corr_wine_white.png', dpi=400, bbox_inches='tight')
>>> plt.show()
