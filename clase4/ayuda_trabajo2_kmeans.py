import seaborn as sns
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("small_test.csv")

df_rand = np.random.randint(0,10,size=dataframe.shape)
dataframe = dataframe + df_rand
dataframe.to_csv("small_test.csv",index=False)
print(dataframe)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(dataframe)


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(principal_components)
cluster_labels = kmeans.labels_
pca_results = pd.DataFrame(data = principal_components, columns = ['PC1', 'PC2'])
pca_results['Cluster'] = cluster_labels
print(pca_results)
sns.scatterplot(x='PC1', y='PC2', hue='Cluster', data=pca_results)
plt.show()
