# -*- coding: utf-8 -*-
from random import shuffle

class Solver_8_queens:

    def __init__(self, pop_size=5, cross_prob=0.11, mut_prob=0.05):
        self.pop_size = pop_size
        self.cross_prob = cross_prob
        self.mut_prob = mut_prob
        #Исходная популяция
        self.populations = []
        for i in range(pop_size):
            population = [1] * 8
            population.extend([0] * (64 - 8))
            shuffle(population)
            self.populations.append(population)

    def visualization(self, gen):
        viz = []
        for i in range(8):
            for j in range(8):
                if gen[i * 8 + j] == 0:
                    viz.append('+')
                else:
                    viz.append('Q')
            viz.append('\n')
        return ''.join(viz)



    '''
    Dummy method representing proper interface
    '''
    def solve(self, min_fitness=0.9, max_epochs=100):
        best_fit = None
        epoch_num = None
        visualization = self.visualization(self.populations[0])
        return best_fit, epoch_num, visualization
