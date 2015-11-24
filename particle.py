from numpy import array

__author__ = 'felipe'

class Particle:

    def __init__(self):
        self.current_position = array([])
        self.best_position = array([])
        self.fitness = 0
        self.velocity = 0