from numpy import array
import random
from math import sin, sqrt
import time
from kmeans import KMeans
from particle import Particle

max_iterations = 128
population_size = 128
velocity_parameter_1 = 0.03125
velocity_parameter_2 = 0.03125
error_criterion = 0.00000001
dimensions = 3

for tests in range(0, 4):

    print("=====================")

    precisions = []
    times = []

    for executions in range(0, 100):

        print(str(executions) + "%")

        start_time = time.time()

        particles = []

        k_means = KMeans()

        # Particles Initialization
        for i in range(population_size):
            p = Particle()

            num_clusters = random.randint(2, 7)

            plist = [num_clusters, ]
            plist.extend([random.uniform(0, 10) for i in range(0, k_means.dimens * 7)])

            # print(plist)

            p.current_position = array(plist)
            p.best_position = p.current_position
            p.fitness = 0.0
            p.velocity = 0.0
            particles.append(p)

        i = 0

        global_best = Particle()
        error = 999999999


        def printParticles():
            xarray = []
            yarray = []
            zarray = []

            for p in particles:
                xarray.append(p.current_position[0])
                yarray.append(p.current_position[1])
                zarray.append(p.current_position[2])

            import matplotlib.pyplot as plt
            from mpl_toolkits.mplot3d import Axes3D
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(xarray, yarray, zarray, zdir=u'z', s=20, c='b', marker='o')
            plt.show()


        # printParticles()

        while i < max_iterations:
            for j, p in enumerate(particles):

                # print (p.current_position)
                fitness = k_means.execute(p.current_position.tolist())
                error = 1-fitness

                if fitness > p.fitness:
                    p.fitness = fitness
                    p.best_position = p.current_position

                if fitness > global_best.fitness:
                    global_best = p

                v = p.velocity + velocity_parameter_1 * random.uniform(1, 10) * (p.best_position - p.current_position) \
                        + velocity_parameter_2 * random.uniform(1, 10) * (global_best.current_position - p.current_position)

                p.current_position = p.current_position + v
                # print(str(j) + "::" + "::" + str(p.fitness))

            i += 1

            # printParticles()

            # print(i)
            # print(global_best.current_position)
            # print(global_best.fitness)

            if error < error_criterion:
                break

        # print ('\nOtimização Por Enxame De Partículas\n')
        # print ('-'*9, 'PARAMETROS\n','-'*9)
        # print ('Tamanho da População : ', population_size)
        # print ('Número de Dimensões  : ', len(particles[0].current_position))
        # print ('Criterio de Erro     : ', error_criterion)
        # print ('Param de Velocidade 1: ', velocity_parameter_1)
        # print ('Param de Velocidade 2: ', velocity_parameter_2)
        #
        # print ('-'*9, 'RESULTADOS\n', '-'*9)
        # print ('Melhor Fitness       : ', global_best.fitness)
        # print ('Melhor Posição       : ', global_best.current_position)
        # print ('Numero de Iterações  : ', i+1)

        end_time = time.time()
        elapsed_time = end_time - start_time

        times.append(elapsed_time)
        precisions.append(global_best.fitness)

    print("times")
    print(times)
    print("precisions")
    print(precisions)

    print("velocity")
    print(velocity_parameter_1)
    print("average time")
    avg1 = sum(times) / len(times)
    print(avg1)
    print("average precision")
    avg2 = sum(precisions) / len(precisions)
    print(avg2)

    velocity_parameter_1 *= 4
    velocity_parameter_2 *= 4

    if velocity_parameter_1 > 1: velocity_parameter_1 = 1
    if velocity_parameter_2 > 1: velocity_parameter_2 = 1