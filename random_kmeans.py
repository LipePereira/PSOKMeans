__author__ = 'felipe'

from kmeans import KMeans
from random import uniform

km = KMeans()

for num_clusters in range(2, 31):

    average_precision = 0
    best_precision = 0
    worst_precision = 9999999999999

    for execs in range(0, 3532):
        params = [num_clusters, ]

        for j in range(0, num_clusters):
            for i in range(0, km.dimens):
                params.extend([uniform(km.mini[i], km.maxi[i])])

        precision = km.execute(params)

        average_precision += precision

        best_precision = max(precision, best_precision)
        worst_precision = min(precision, worst_precision)
        # print(execs)

    average_precision /= 3532
    print(str(num_clusters) + "," + str(average_precision) + "," + str(best_precision) + "," + str(worst_precision))
