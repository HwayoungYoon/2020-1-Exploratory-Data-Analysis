# -*- coding: utf-8 -*-
"""
25강: 가설검정(P-value, Type of Error), ROC Curve
"""


"""
ROC Curve
"""
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as metrics

actual = np.array([1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,0,1,0,1,0])
predicted = np.array([0.9,0.8,0.7,0.6,0.55,0.54,0.53,0.52,0.51,
                      0.505,0.4,0.39,0.38,0.37,0.36,0.35,0.34,
                      0.33,0.30,0.1])

fpr, tpr, threshold = metrics.roc_curve(actual, predicted)

plt.title("Receiver Operating Characteristic")
plt.plot(fpr, tpr, 'b')
plt.xlabel("False Positive Rate(1 - Specificity)")
plt.ylabel("True Positive Rate(Sensitivity)")
plt.plot([0,1], [0,1], 'r--')
plt.xlim([0,1])
plt.ylim([0,1])