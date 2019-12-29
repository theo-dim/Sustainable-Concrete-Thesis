"""
===============================================================
G(r) Isotonic Regression for High-Alkali, H-activated Metakaolin
===============================================================
"""

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.collections import LineCollection

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state

main = pd.read_csv('/Users/Theo/Google Drive/College/Senior Thesis/Materials Science/data/isotonic/haham_g.csv', sep=',',names = ['Time','G'])
mainx_data = main.Time[1:60]
mainx_target = main.G[1:60]

###############################################################################
# Fit Isotonic Regression model
###############################################################################

ir = IsotonicRegression()
lr = LinearRegression()

y_ = ir.fit_transform(mainx_data, mainx_target)
predictions = ir.predict([10])
print predictions
print ir.score(mainx_data, mainx_target)
#print("RSS: %.2f"
#      % np.mean((ir.predict(mainx_target) - mainy_target) ** 2))

###############################################################################
# Plot result
###############################################################################

fig = plt.figure()
plt.plot(mainx_data, mainx_target, 'r.', markersize=12)
plt.plot(mainx_data, y_, 'g.-', markersize=12)
plt.legend(('Data', 'Isotonic Fit', 'Linear Fit'), loc='lower right')
plt.title('Isotonic regression')
plt.show()
