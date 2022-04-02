from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.clustering import KMeans
from pyspark.sql import SparkSession

if __name__ == "__main__":
    ss = SparkSession.builder.appName("k_means_clustering").getOrCreate()

    # Perform k-means clustering
    input_data = ss.read.format("libsvm").load("kmeans_data.txt")
    k_model = KMeans().setK(50).setSeed(50).fit(input_data)
    cluster_centers = k_model.clusterCenters()
    sil = ClusteringEvaluator().evaluate(k_model.transform(input_data))

    ss.stop()
