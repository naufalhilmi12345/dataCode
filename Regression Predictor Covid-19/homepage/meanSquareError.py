import numpy as np

class meanSquareError:

    def __init__(self):
        pass

    def mse(self, actual, predict):
        actual, pred = np.array(actual), np.array(predict)
        tmp = (actual - pred)**2
        counter = 0
        for i in range(len(tmp)):
            counter += tmp[i]
        counter = counter // len(tmp)
        return counter
