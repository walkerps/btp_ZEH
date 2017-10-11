import pandas as  pd
import numpy as np
import re
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

file = 'data_set.csv'

data  = pd.read_csv(file)

data = data.drop(['Month','Day','Hour','ACO'],axis = 1)

Y = data['DCO'].values

data = data.drop(['DCO'],axis = 1)

X = data.values

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,train_size = 0.7)

model = svm.SVR()

model.fit(X_train,Y_train)

pred = model.predict(X_test)

#accuracy = accuracy_score(Y_test,pred)

#print accuracy
filename = 'ML_Model.sav'

pickle.dump(model,open(filename,'wb'))



