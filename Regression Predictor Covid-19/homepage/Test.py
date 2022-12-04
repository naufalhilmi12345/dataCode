#from Model import Model
from PolynomialFeatures import PolynomialFeatures
from Regression import Regression
import numpy as np

def main():
	reg = Regression()
	reg.fit(np.array([[0],[1],[2]]),np.array([[0],[2],[7]]))
	print(reg.predict([2]))
	print(reg.constant)

	

if __name__ == '__main__':
	main()