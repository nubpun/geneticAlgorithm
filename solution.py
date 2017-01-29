#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This script uses nqueens.py module for solving 8-queens problem by using 
a genetic algorithm
"""
import sys
import nqueens as nq
print('Python version:', sys.version)


solver = nq.Solver_8_queens()

best_fit, epoch_num, visualization = solver.solve()
print("Best solution:")
print("Fitness:", best_fit)
print("Iterations:", epoch_num)
print(visualization)
#my test
for i in range(100):
    solver = nq.Solver_8_queens()
    best_fit, epoch_num, visualization = solver.solve()
    if epoch_num > 20:
        print(epoch_num, best_fit)
    else:
        print('ok', epoch_num)
