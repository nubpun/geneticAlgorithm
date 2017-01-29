# -*- coding: utf-8 -*-
import random


class Solver_8_queens:
    def __init__(self, pop_size=1000, cross_prob=0.0, mut_prob=1):
        self.pop_size = pop_size
        self.cross_prob = cross_prob
        self.mut_prob = mut_prob
        # Исходная популяция
        self.__scores = [-1] * pop_size
        self.__populations = []
        for i in range(pop_size):
            gen = []
            temp_model = []
            for j in range(8):
                row = [0] * j + [1] + [0] * (7 - j)
                temp_model.append(row)
            random.shuffle(temp_model)
            for part in temp_model:
                gen.extend(part)
            self.__populations.append(gen)
        self.fitness()

    @staticmethod
    def visualization(gen):
        viz = []
        for i in range(8):
            for j in range(8):
                if gen[i * 8 + j] == 0:
                    viz.append('+')
                else:
                    viz.append('Q')
            viz.append('\n')
        return ''.join(viz)

    #Кол-во неатакующих друг друга пар ферзей.
    def fitness(self):
        gen_id = 0
        for gen in self.__populations:
            score = 0
            for i in range(8):
                for j in range(8):
                    if gen[i * 8 + j] == 1:
                        under_attack = 0
                        x = i + 1
                        y = j + 1
                        while (x < 8) and (y < 8):
                            if gen[x * 8 + y] == 1:
                                under_attack += 1
                            x += 1
                            y += 1

                        x = i - 1
                        y = j - 1
                        while (x >= 0) and (y >= 0):
                            if gen[x * 8 + y] == 1:
                                under_attack += 1
                            x -= 1
                            y -= 1

                        x = i - 1
                        y = j + 1
                        while (x >= 0) and (y < 8):
                            if gen[x * 8 + y] == 1:
                                under_attack += 1
                            x -= 1
                            y += 1

                        x = i + 1
                        y = j - 1
                        while (x < 8) and (y >= 0):
                            if gen[x * 8 + y] == 1:
                                under_attack += 1
                            x += 1
                            y -= 1
                        score += under_attack
            self.__scores[gen_id] = 28 - score / 2
            gen_id += 1

    #Селекция методом колеса рулетки.
    def selection(self):
        temp_populations = []
        s = sum(self.__scores)
        for i in range(self.pop_size):
            prob = random.randint(0, s)
            cur = 0
            for idGen in range(self.pop_size):
                cur += self.__scores[idGen]
                if cur >= prob:
                    temp_populations.append(self.__populations[idGen])
                    break
        self.__populations = temp_populations

    def cross(self):
        for cnt in range(1):
            if random.random() > self.cross_prob:
                return
            parent_first = random.randint(0, self.pop_size - 1)
            parent_second = random.randint(0, self.pop_size - 1)
            median = 8 * random.randint(0, 8)
            for i in range(median, 8 * 8):
                t = self.__populations[parent_first][i]
                self.__populations[parent_first][i] = self.__populations[parent_second][i]
                self.__populations[parent_second][i] = t

    def mutation(self):
        for cnt in range(self.pop_size ):
            if random.random() > self.mut_prob:
                return
            gen_id = random.randint(0, self.pop_size - 1)
            row_a = random.randint(0, 7)
            row_b = random.randint(0, 7)
            for i in range(8):
                t = self.__populations[gen_id][row_a * 8 + i]
                self.__populations[gen_id][row_a * 8 + i] = self.__populations[gen_id][row_b * 8 + i]
                self.__populations[gen_id][row_b * 8 + i] = t

    def solve(self, min_fitness=0.99, max_epochs=30):
        cur_max_fitness = 0
        epoch_num = 0

        while(cur_max_fitness < min_fitness) and (epoch_num < max_epochs):
            self.selection()
            self.cross()
            self.mutation()
            self.fitness()

            best_fit_id = 0
            for i in range(self.pop_size):
                if self.__scores[i] > self.__scores[best_fit_id]:
                    best_fit_id = i
            #avg = sum(self.__scores) / self.pop_size
            #mn = min(self.__scores)
            #print(self.__scores[best_fit_id], ' ', avg, ' ', mn)
            #print(self.visualization(self.__populations[best_fit_id]))

            cur_max_fitness = self.__scores[best_fit_id] / 28
            epoch_num += 1

        best_fit = self.__scores[best_fit_id]
        visualization = self.visualization(self.__populations[best_fit_id])
        return best_fit, epoch_num, visualization
