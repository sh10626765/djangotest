import pandas
import os
import pymongo
import numpy

from testsite.utils import ExcelFileProcess
from sklearn.neighbors import LocalOutlierFactor
from sklearn.ensemble import IsolationForest
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from scipy import stats

BASE_DIR = 'E:/毕设/data'

DATA_FILE_PATH = os.path.join(BASE_DIR, 'traindata-0.5D0 - he.xlsx')

print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# import pandas_profiling
#
# data = pandas.read_excel(DATA_FILE_PATH)
# datapro = pandas_profiling.ProfileReport(data)
# datapro.to_file(output_file='./asd.html')
# cl = pymongo.MongoClient(host='127.0.0.1', port=27017)
# db = cl.get_database('materialsData')
# coll = db.get_collection('traindata-0.5D0 - he.xlsx')
# data = [it for it in coll.find()]
# df = pandas.DataFrame(data)
# dft = df.iloc[:, 5:]
# print(str(dft))

# TEST_FILE = os.path.join(BASE_DIR, 'test_blank_data.xlsx')

# df = pandas.read_excel(DATA_FILE_PATH)

# df = df.iloc[:, 4:]
# df = (df-df.min())/(df.max()-df.min())

# clf = LocalOutlierFactor(n_neighbors=50, contamination=0.1)
# a = clf.fit_predict(df)
# b = clf.negative_outlier_factor_
# c = stats.scoreatpercentile(b, 10)
# for i in range(b.size):
#     if b[i] < c:
#         print(i)
#
# clf = IsolationForest()
# a = clf.fit(df)
# b = clf.decision_function(df)
# c = stats.scoreatpercentile(b, 10)
# for i in range(b.size):
#     if b[i] < c:
#         print(i)

# X = df.values
#
# clf = KMeans()
# clf.fit(X)
# print(clf.predict(X))
# for i in range(len(labels)):
#     if -1 == labels[i]:
#         print(i, end=' ')

# print(X)
# pca = PCA(n_components='mle')
# Xt = pca.fit_transform(X)
# lbd = pca.explained_variance_ratio_
# print(lbd)
#
# print(pca.get_covariance())

# clf = LocalOutlierFactor()
# a = clf.fit_predict(Xt)
# b = clf.negative_outlier_factor_
# c = stats.scoreatpercentile(b, 20)
# for i in range(b.size):
#     if b[i] < c:
#         print(i)

import matplotlib.pyplot as plt
# X = df.values
# print(df.shape[0])

# clf = LocalOutlierFactor(n_neighbors=25, contamination=0.1)
# labels = clf.fit_predict(X)
# for i in range(len(labels)):
#     if labels[i] == -1:
#         print(i, end=' ')
# print()
# clf = IsolationForest(n_estimators=102, contamination=0.1)
# labels = clf.fit_predict(X)
# for i in range(len(labels)):
#     if labels[i] == -1:
#         print(i, end=' ')
#
# Xs = []
# cnt = {}
# for i in range(len(X[0])):
#     # print(list(zip(X[:, i], X[:, -1])))
#     # Xs.append(list(zip(X[:, i], X[:, -1])))
#     labels = clf.fit_predict(list(zip(X[:, i], X[:, -1])))
#     scores = clf.negative_outlier_factor_
#
#     for j in range(len(labels)):
#         if labels[j] == -1:
#             cnt[j] = cnt.get(j, 0) + 1
#             # print(j, end=' ')
# print(cnt)
# print(sorted(cnt.items(), key=lambda x:x[1], reverse=True))


# for i in range(len(X[0])):
#     print(df.columns[i])
#     plt.figure()
#     plt.scatter(X[:, i], X[:, -1])
#     plt.show()
#     input()
