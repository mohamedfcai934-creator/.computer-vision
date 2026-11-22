import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans


X, y = make_blobs(
    n_samples=100,
    centers=3,
    random_state=42
)


kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)


labels = kmeans.labels_
centers = kmeans.cluster_centers_


plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], 
            color='red', marker='X', s=200)

plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
