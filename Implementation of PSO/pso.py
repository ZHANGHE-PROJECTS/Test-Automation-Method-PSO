# coding: utf-8
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt


# ----------------------parameter---------------------------------
class PSO():
    def __init__(self, array, pN=100, w=0.8, c1=2, c2=2, r1=0.6, r2=0.3):
        self.w = w 
        self.c1 = c1 
        self.c2 = c2 
        self.r1 = r1 
        self.r2 = r2 
        self.pN = pN  
        self.dim = 3
        self.X = np.zeros((self.pN, self.dim))  
        self.V = np.zeros((self.pN, self.dim))  
        self.pbest = np.zeros((self.pN, self.dim))  
        self.gbest = np.zeros((1, self.dim))  
        self.p_fit = np.ones(self.pN) * 1e10 
        self.fit = 1e10  
        self.fitness = np.array([])
        self.upper_bound = np.array([44,27,51])
        self.lower_bound = np.array([1,-40,5])
        self.array = array

    # ---------------------initialization----------------------------------
    def init_population(self,array,pN):
        index = np.random.choice(array.shape[0],size=pN,replace=False)
        sample = array[index,:]
        for i in range(self.pN):
            for j in range(self.dim):
                self.X[i][j] = sample[i][j]
                self.V[i][j] = 1
            self.pbest[i] = self.X[i]
        return self.X
        # ----------------------update----------------------------------

    def train(self, array, result):
        for i in range(self.pN):
            temp = result[i]
            if temp <= self.p_fit[i]:  
                self.p_fit[i] = temp
                self.pbest[i] = self.X[i]
                if self.p_fit[i] <= self.fit:  
                    self.gbest = self.X[i].copy()
                    self.fit = self.p_fit[i]
        for j in range(self.pN):
            self.V[j] = self.w * self.V[j] + self.c1 * random.random() * (self.pbest[j] - self.X[j]) + self.c2 * random.random() * (self.gbest - self.X[j])
            self.X[j] = np.round(self.X[j] + self.V[j],0)
            distance=abs(array-self.X[j]).sum(axis=1)
            if min(distance)==0:
                self.X[j] = self.X[j]
            else:
               replace=array[np.argmin((abs(array-self.X[j]).sum(axis=1)))]
               self.X[j]=replace

        self.fitness = np.append(self.fitness, self.fit)
        self.X = np.clip(self.X, self.lower_bound, self.upper_bound) 

        return self.X, self.fit
        # -------------------------------------------------

    def get_fitness(self):
        return self.fitness



if __name__ == "__main__":
    from SUT_IDM import IDM

    upper_bound = np.array([44., 27., 50.])
    lower_bound = np.array([1., -40, 5.])
    name = np.array(['vs', 'dif_speed', 'dis'])
    sut = IDMDanger(name)
    pso = PSO(upper_bound, lower_bound, pN=30)
    sample = pso.init_population()
    result = sut.test(sample)
    for i in range(10):
        sample, fit = pso.train(result)
        result = sut.test(sample)
    output3d(sample, result)
