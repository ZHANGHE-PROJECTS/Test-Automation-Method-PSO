import numpy as np


def grid():
    upper_bound = np.array([0.91, 2.51, 2.51])  # 'w', 'c1', 'c2'
    lower_bound = np.array([0.1, 0.5, 0.5])
    interval = np.array([0.1, 0.5, 0.5])  #9*5*5=225

    grad = []
    for i in range(upper_bound.shape[0]):
        grad += [np.arange(lower_bound[i], upper_bound[i], interval[i])]
    a = np.meshgrid(*grad)
    x_all = np.vstack([x.ravel() for x in a]).T

    return x_all


if __name__ == '__main__':
    grid()