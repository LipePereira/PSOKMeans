__author__ = 'felipe'

from point import Point

class Cluster:
    def __init__(self):
        self.centroid = Point()
        self.points = []

    def updateCentroid(self):
        points_sum = [0] * len(self.centroid.position)

        if len(self.points) == 0:
            return points_sum

        for point in self.points:
            for i, dimension in enumerate(point.position):
                points_sum[i] += dimension

        points_avg = []

        for point_sum in points_sum:
            points_avg.append(point_sum / len(self.points))

        self.centroid.position = points_avg

    def to_array_of_classes(self):
        classes = []
        for point in self.points:
            classes.append(point.classe)
        return classes