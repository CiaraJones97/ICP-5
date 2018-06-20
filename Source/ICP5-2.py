import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Set the values
arr = np.array ([[2,70],[2.1,98],[1.5,45],[1.75,78],[1.78,90],[1.8,90],[1.6,60],[2.1,110],[1.8,80], [1.6,65],[1.92,105],[1.6,62],[1.75,76], [1.5, 44]])
kmeans = KMeans (n_clusters= 3)
kmeans.fit(arr)

# Set the centroids
centroids = kmeans.cluster_centers_
print (centroids)
print ("Cluster center 1: height = {} & weight = {}; Cluster center 2: height = {} & weight = {}; Cluster center 3: height = {} & weight = {}"
       .format(centroids[1][0],centroids[1][1],centroids[0][0],centroids[0][1],centroids[2][0],centroids[2][1]))
print ("Remark Height is given in meters and weight is in Kg")

# Plot the points and the centroids
plt.figure(figsize=(15,15), dpi=80)
plt.scatter(arr[:,0], arr[:,1])

for i in range(3):
    plt.scatter(centroids[i][0], centroids[i][1], marker = 'x', linewidths = 5)
plt.show()
