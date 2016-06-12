__author__ = 'http://blog.dominodatalab.com/topology-and-density-based-clustering/'
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

data = pd.read_csv("Wholesale customers data.csv")
# Drop non-continuous variables
data.drop(["Channel", "Region"], axis = 1, inplace=True)

# So we can visualize the data, I'm going to use only two of these attributes:

# Groceries: The customer's annual spending (in some monetary unit) on grocery products.
# Milk: The customer's annual spending (in some monetary unit) on milk products.
data = data[["Grocery", "Milk"]]
data = data.as_matrix().astype("float32", copy=False)

# Because the values of the data are in the thousands, we are going to normalize each attribute by scaling it to 0 mean
# and unit variance.

stscaler = StandardScaler().fit(data)
data = stscaler.transform(data)
#  We will construct a DBSCAN object that requires a minimum of 15 data points in a neighborhood of radius 0.5
#  to be considered a core point.
dbsc = DBSCAN(eps=.5, min_samples=15).fit(data)

# Next, we can extract our cluster labels and outliers to plot our results.

labels = dbsc.labels_
core_samples = np.zeros_like(labels, dtype=bool)
core_samples[dbsc.core_sample_indices_] = True

if __name__=="__main__":
    from sklearn.datasets import make_moons
    # moons_X: Data, moon_y: Labels
    moons_X, moon_y = make_moons(n_samples=2000)
    # This dataset is aesthetically pleasing, but it has no outliers. To rectify this problem,
    #  I am going to add random noise to 1% of the data using the following code:

    def add_noise(X,y, noise_level=0.01):
        # The number of points we wish to make noisy
        amt_noise = int(noise_level*len(y))
        # Pick amt_noise points at random
        idx = np.random.choice(len(X), size = amt_noise)
        # Add random noise to these selected points
        noise = np.random.random((amt_noise, 2)) - 0.5
        X[idx,:] += noise
        return X