import numpy as np 
from PolynomialFeatures import PolynomialFeatures

class Regression():

	dependent = None
	independent = None
	constant = None
	is_trained = False

	def __init__(self):
		pass

	def get_is_trained(self):
		return self.get_is_trained

	def fit(self,independent,dependent):
		tmp = np.ones((independent.shape[0],independent.shape[1]+1))
		tmp[:,:-1] = independent
		self.dependent = dependent
		self.independent = tmp
		left = np.matmul(self.independent.T,self.independent)
		right = np.matmul(self.independent.T,self.dependent)
		self.constant = np.matmul(np.linalg.inv(left),right)
	
	def predict(self,var):
		res = 0	
		for i in range(len(var)):
			res += var[i] * self.constant[i]
		return res + self.constant[-1]

