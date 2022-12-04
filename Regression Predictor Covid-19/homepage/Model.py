from DataPreprocessing import DataPrep
from Regression import Regression
from PolynomialFeatures import PolynomialFeatures
import pandas as pd
import numpy as np

class Model():

	dataset_all = None
	dataset_psbb = None
	dataset_non_psbb = None
	model_jumlah_diperiksa = None
	model_total_kasus_psbb = None
	model_total_kasus_non_psbb = None
	polynomial_features = None

	def __init__(self):
		data = DataPrep()
		self.dataset_all = data.get_df()
		self.dataset_psbb = data.get_df_psbb()
		self.dataset_non_psbb = data.get_df_non_psbb()
		self.model_total_kasus_non_psbb = Regression()
		self.model_jumlah_diperiksa = Regression()
		self.model_total_kasus_psbb = Regression()
		self.polynomial_features = PolynomialFeatures()
		self.train()

	def get_polynomial_features(self, data, features):
		res = []
		for row in data:
			temp = self.polynomial_features.transform(row.tolist(), features)
			res.append(np.array(temp))
		res = np.array(res)
		return res

	def train(self):
		#independent_jumlah_diperiksa = self.get_polynomial_features(self.dataset_all['Hari ke'].values.reshape(self.dataset_all.shape[0],1), 2)
		independent_jumlah_diperiksa = self.dataset_all['Hari ke'].values.reshape(self.dataset_all.shape[0],1)
		#print(independent_jumlah_diperiksa.reshape(self.dataset_all.shape[0],1).shape)
		dependent_jumlah_diperiksa = self.dataset_all['Orang yang dites'].values.reshape(self.dataset_all.shape[0],1)
		#print(dependent_jumlah_diperiksa.shape)
		self.model_jumlah_diperiksa.fit(independent_jumlah_diperiksa,dependent_jumlah_diperiksa)
		self.train_pssb()
		self.train_non_psbb()

	def train_pssb(self):
		#Train untuk model prediksi total kasus dengan kondisi PSBB
		#independent_total_kasus = self.get_polynomial_features(self.dataset_psbb.iloc[:,-2:].values, 2)
		independent_total_kasus = self.dataset_psbb.iloc[:,-3:-1].values
		dependent_total_kasus = self.dataset_psbb['Total kasus'].values.reshape(self.dataset_psbb.shape[0],1)
		self.model_total_kasus_psbb.fit(independent_total_kasus,dependent_total_kasus)

	def train_non_psbb(self):
		#Train untuk model prediksi total kasus dengan kondisi non PSBB
		#independent_total_kasus = self.get_polynomial_features(self.dataset_non_psbb.iloc[:,-2:].values, 2)
		independent_total_kasus = self.dataset_non_psbb.iloc[:,-3:-1].values
		dependent_total_kasus = self.dataset_non_psbb['Total kasus'].values.reshape(self.dataset_non_psbb.shape[0],1)
		self.model_total_kasus_non_psbb.fit(independent_total_kasus,dependent_total_kasus)

	def predict(self,hari,status):
		if status == 'PSBB':
			return self.predict_total_kasus_psbb(hari)
		else:
			return self.predict_total_kasus_non_psbb(hari)

	def predict_total_kasus_psbb(self,hari):
		jumlah_diperiksa = self.predict_jumlah_diperiksa(hari)
		total_kasus_sebelumnya = 0 #Ini masih bingung nge backtracknya gimana
		#return self.model_total_kasus_psbb.predict(np.array([jumlah_diperiksa,total_kasus_sebelumnya])) ini belom bisa gunain krn belom bisa backtrack
		return jumlah_diperiksa

	def predict_total_kasus_non_psbb(self,hari):
		jumlah_diperiksa = self.predict_jumlah_diperiksa(hari)
		total_kasus_sebelumnya = 0 #Ini masih bingung nge backtracknya gimana
		#return self.model_total_kasus_non_psbb.predict(np.array([jumlah_diperiksa,total_kasus_sebelumnya])) ini belom bisa gunain krn belom bisa backtrack
		return jumlah_diperiksa

	def predict_jumlah_diperiksa(self,hari):
		return self.model_jumlah_diperiksa.predict(np.array([hari]))
