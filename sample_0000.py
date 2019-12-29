print(__doc__)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

# Load the sample dataset
sample = datasets.load_diabetes()
print(sample)
# Use only one feature
sample_x = sample.data[:, np.newaxis, 2]

# Split the data into training/testing sets
sample_x_train = sample_x[:-20]
sample_x_test = sample_x[-20:]

# Split the targets into training/testing sets
sample_y_train = sample.target[:-20]
sample_y_test = sample.target[-20:]

# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(sample_x_train, sample_y_train)

# The mean square error
print("Residual sum of squares: %.2f"
      % np.mean((regr.predict(sample_x_test) - sample_y_test) ** 2))

# Explained variance score:
print('Variance score: %.2f' % regr.score(sample_x_test, sample_y_test))

# Plot outputs
plt.scatter(sample_x_test, sample_y_test,  color='black')
plt.plot(sample_x_test, regr.predict(sample_x_test), color='blue',
         linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
