import time

__author__ = 'felipe'

from pyswarm import pso
from kmeans import KMeans
import random

precisions = []
times = []

for executions in range(0, 100):

    print(str(executions) + "%")

    start_time = time.time()


    km = KMeans()

    min_clusters = 2
    max_clusters = 7

    lb = [min_clusters, ]
    lb.extend([0 for i in range(0, km.dimens * max_clusters)])

    up = [max_clusters, ]
    up.extend([10 for i in range(0, km.dimens * max_clusters)])

    xopt, fopt = pso(km.execute, lb, up, swarmsize=128, maxiter=8, omega=0.125)

    end_time = time.time()
    elapsed_time = end_time - start_time

    times.append(elapsed_time)
    precisions.append(fopt)


print(times)
print(precisions)