import pandas as pd
import numpy as np

class DataPrep():

	df = None
	df_psbb = None
	df_non_psbb = None

	def __init__(self):
		self.df = pd.read_csv('Dataset/All.csv')
		self.df = self.df.fillna("0")
		self.preprocess()

	def get_df(self):
		return self.df

	def get_df_psbb(self):
		return self.df_psbb

	def get_df_non_psbb(self):
		return self.df_non_psbb

	def preprocess(self):

		#Remove some column
		lst_drop = ['Tingkat kesembuhan (closed cases)']
		for i in lst_drop:
 			del self.df[i]

    	#Clean row value
		lst_change = ['Kasus baru', 'Total kasus', 'Kasus aktif', 'Orang yang dites']
		for col in lst_change:
			data = self.df[col]
			for row in range(self.df.shape[0]):
				if "," in data[row]:
					data[row] = data[row].replace(",","")

    	#Change datatype 
		for col in lst_change:
			self.df[col] = self.df[col].astype(int)

    	#Add 'Total Kasus H-1' column
		self.df['Total Kasus h-1'] = 0
		for i in range(1,self.df.shape[0]+1):
			self.df['Total Kasus h-1'][i] = self.df['Total kasus'][i-1]

		#Add 'Hari ke' column
		self.df['Hari ke'] = 0
		for i in range(1,self.df.shape[0]+1):
			self.df['Hari ke'][i-1] = i

    	#Create non psbb dataframe
		self.df_non_psbb = self.df.iloc[0:38,:]
		self.df_non_psbb = self.df_non_psbb.append(self.df.iloc[52:195,:])

		#Create psbb dataframe
		self.df_psbb = self.df.iloc[38:52,:]
		self.df_psbb = self.df_psbb.append(self.df.iloc[195:223,:])



