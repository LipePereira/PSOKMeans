from math import sqrt
from datareader import DataReader
from random import uniform
from random import random
from point import Point
from cluster import Cluster
from rand import get_tp_fp_tn_fn

class KMeans:

    def __init__(self):
        self.reader = DataReader("yeast.data", 1, 1, " ")

        self.pts, self.mini, self.maxi, self.dimens, self.classes = self.reader.getPoints()

        self.points = []

        for pt, c in zip(self.pts, self.classes):
            point = Point()
            point.position = pt
            point.classe = c
            self.points.append(point)

        self.i = 0
        self.max_iterations = 1

        self.clusters = []

        self.possible_classes = self.get_possible_classes()


    def randomPoint(self):
        point = Point()
        for mi, ma in zip(self.mini, self.maxi):
            point.position.append(uniform(mi, ma))
        return point

    def randomClusters(self, max_clusters):
        for i in range(0, max_clusters):
            cluster = Cluster()
            cluster.centroid = self.randomPoint()
            self.clusters.append(cluster)

    def distanceBetween(self, p1, p2):

        distance = 0
        for d1, d2 in zip(p1, p2):
            distance += (d2-d1) ** 2
        return distance

    def realDistanceBetween(self, p1, p2):
        distance = 0
        for d1, d2 in zip(p1, p2):
            distance += (d2-d1) ** 2
        return sqrt(distance)

    def putPointInClosestCluster(self, point):
        min_distance = self.distanceBetween(point.position, self.clusters[0].centroid.position)
        cur_cluster = self.clusters[0]
        for cluster in self.clusters:
            distance = self.distanceBetween(point.position, cluster.centroid.position)
            if distance < min_distance:
                cur_cluster = cluster
                min_distance = distance
        cur_cluster.points.append(point)

    def assignPointsToClusters(self):
        for point in self.points:
            self.putPointInClosestCluster(point)

    def recalculateCentroids(self):
        for cluster in self.clusters:
            cluster.updateCentroid()

    def clearClusters(self):
        for cluster in self.clusters:
            cluster.points = []

    def clusterToX(self, cluster):
        xarray = []
        for p in cluster.points:
            xarray.append(p.position[0])
        return xarray

    def clusterToY(self, cluster):
        yarray = []
        for p in cluster.points:
            yarray.append(p.position[1])
        return yarray

    def clusterToZ(self, cluster):
        zarray = []
        for p in cluster.points:
            zarray.append(p.position[2])
        return zarray

    def printClusters(self):
        import matplotlib.pyplot as plt
        from mpl_toolkits.mplot3d import Axes3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for i, cluster in enumerate(self.clusters):
            if i == 0:
                ax.scatter(self.clusterToX(cluster), self.clusterToY(cluster), self.clusterToZ(cluster), zdir=u'z', s=20, c='b', marker='o')
                ax.scatter([cluster.centroid.position[0],], [cluster.centroid.position[1],], [cluster.centroid.position[2],], zdir=u'z', s=50, c='b', marker='s')
            if i == 1:
                ax.scatter(self.clusterToX(cluster), self.clusterToY(cluster), self.clusterToZ(cluster), zdir=u'z', s=20, c='r', marker='o')
                ax.scatter([cluster.centroid.position[0],], [cluster.centroid.position[1],], [cluster.centroid.position[2],], zdir=u'z', s=50, c='r', marker='s')
            if i == 2:
                ax.scatter(self.clusterToX(cluster), self.clusterToY(cluster), self.clusterToZ(cluster), zdir=u'z', s=20, c='g', marker='o')
                ax.scatter([cluster.centroid.position[0],], [cluster.centroid.position[1],], [cluster.centroid.position[2],], zdir=u'z', s=50, c='g', marker='s')
            if i == 3:
                ax.scatter(self.clusterToX(cluster), self.clusterToY(cluster), self.clusterToZ(cluster), zdir=u'z', s=20, c='y', marker='o')
                ax.scatter([cluster.centroid.position[0],], [cluster.centroid.position[1],], [cluster.centroid.position[2],], zdir=u'z', s=50, c='y', marker='s')
            if i == 4:
                ax.scatter(self.clusterToX(cluster), self.clusterToY(cluster), self.clusterToZ(cluster), zdir=u'z', s=20, c='c', marker='o')
                ax.scatter([cluster.centroid.position[0],], [cluster.centroid.position[1],], [cluster.centroid.position[2],], zdir=u'z', s=50, c='c', marker='s')

        plt.show()

    def get_possible_classes(self):
        classes = []
        for p in self.points:
            if classes.count(p.classe) == 0:
                # print(p.classe)
                classes.append(p.classe)
        return classes

    def rand_index(self):
        cooccurrence_matrix = []

        for possible_class in self.possible_classes:
            matrix_line = []
            for cluster in self.clusters:
                array_of_classes = cluster.to_array_of_classes()
                matrix_line.append(array_of_classes.count(possible_class))
            cooccurrence_matrix.append(matrix_line)

        import numpy as np
        array_matrix = np.array(cooccurrence_matrix)

        tp, fp, tn, fn = get_tp_fp_tn_fn(array_matrix)

        rand_index = float(tp + tn) / (tp + fp + fn + tn)

        precision = float(tp) / (tp + fp)
        recall = float(tp) / (tp + fn)

        return rand_index


    # execution
    def execute(self, args):

        # First Argument is the Number of Clusters
        # All the others are coordinates
        # Example (3, x1,y1,z1, x2,y2,z2, x3,y3,z3)

        self.clusters = []

        iters = int(args[0])

        if iters < 1: iters = 1
        if iters > 5 : iters = 5

        for i in range (0, iters):
            cluster = Cluster()
            cluster.centroid.position = args[(i * self.dimens) + 1: (i * self.dimens) + self.dimens + 1]
            self.clusters.append(cluster)
        i = 0

        while i < self.max_iterations:
            self.clearClusters()
            self.assignPointsToClusters()
            # self.recalculateCentroids()
            i += 1


        rand_index = self.rand_index()

        return rand_index