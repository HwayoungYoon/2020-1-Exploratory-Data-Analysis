Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 18 2019, 23:46:00) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
>>> import matplotlib.pyplot as plt
>>> 
>>> plt.style.use('ggplot')
>>> x = [59,61,50,61,69,38,47,64,82,78,
     47,47,11,49,76,36,48,29,56,60,
     61,61,55,58,78,52,70,23,62,20,
     40,59,33,28,28,50,26,56,31,23,
     32,47,37,48,10,14,54,52,48,31]
>>> 
>>> fig = plt.figure()
>>> ax1 = fig.add_subplot(1,1,1)
>>> 
>>> ax1.hist(x, bins=50, color='g')
(array([2., 0., 1., 0., 0., 0., 1., 0., 0., 2., 0., 1., 2., 1., 2., 2., 0.,
       0., 2., 1., 1., 0., 0., 0., 0., 4., 3., 3., 0., 2., 1., 3., 0., 1.,
       3., 4., 1., 1., 0., 0., 1., 1., 0., 0., 0., 1., 0., 2., 0., 1.]), array([10.  , 11.44, 12.88, 14.32, 15.76, 17.2 , 18.64, 20.08, 21.52,
       22.96, 24.4 , 25.84, 27.28, 28.72, 30.16, 31.6 , 33.04, 34.48,
       35.92, 37.36, 38.8 , 40.24, 41.68, 43.12, 44.56, 46.  , 47.44,
       48.88, 50.32, 51.76, 53.2 , 54.64, 56.08, 57.52, 58.96, 60.4 ,
       61.84, 63.28, 64.72, 66.16, 67.6 , 69.04, 70.48, 71.92, 73.36,
       74.8 , 76.24, 77.68, 79.12, 80.56, 82.  ]), <a list of 50 Patch objects>)
>>> 
>>> ax1.xaxis.set_ticks_position('bottom')
>>> ax1.yaxis.set_ticks_position('left')
>>> plt.xlabel('Students')
Text(0.5, 0, 'Students')
>>> plt.ylabel('Grades in a particular subject')
Text(0, 0.5, 'Grades in a particular subject')
>>> fig.suptitle('Histograms', fontsize=15, fontweight='bold')
Text(0.5, 0.98, 'Histograms')
>>> plt.savefig('histogram_grades.png', dpi=400, bbox_inches='tight')
>>> plt.show()
>>> 
>>> from uuid import getnode as get_mac
>>> mac = get_mac()
>>> print("Mac address: {0}".format(mac))
Mac address: 150075731951663
>>> 
