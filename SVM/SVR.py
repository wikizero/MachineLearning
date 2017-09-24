# coding:utf-8
import pandas as pd
from sklearn.svm import SVR, SVC
from sqlalchemy import create_engine


class SVRTest:
	def __init__(self):
		self.engine = create_engine("mysql://root:root@39.108.141.110:3306/world", encoding="utf-8")

	def query_database(self, sql):
		df = pd.read_sql_query(sql, self.engine)
		return df

	def df_to_excel(self, df, file_name):
		write = pd.ExcelWriter(file_name)
		df.to_excel(write)
		write.save()
		write.close()

	def predict(self, data, target, new_data):
		clf = SVR()
		clf.fit(data, target)
		return clf.predict(new_data)

	def predict_price(self):
		df = self.query_database()
		df = df[['level', 'account_type', 'soul_num', 'price']]
		df = df[df['soul_num'] > 0]
		account_type = set(df['account_type'].tolist())
		dct = {v: k for k, v in enumerate(account_type)}
		df['account_type'] = df['account_type'].map(lambda x: dct[x])
		data = df[['level', 'account_type', 'soul_num']]
		target = df['price']
		print self.predict(data, target, [[23, 8, 65000]])


if __name__ == '__main__':
	svr = SVRTest()
	svr.df_to_excel(svr.query_database(sql='select * from swordinfo'), 'sword.xlsx')  # write to excel
	# svr.predict_price()