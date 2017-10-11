import pandas as pd
import numpy as np
import re

file = 'data_set.csv'

data = pd.read_csv(file)

print data.columns

data['Month'] = data['Month'].map({"1":"Jan","2":"Feb","3":"March","4":"April","5":"May","6":"June","7":"July","8":"August","9":"Sept","10":"October","11":"November","12":"December"})

"""print "Conversion"
print " "
print data.head(5)

print " "

print data.tail(5)

data.to_csv("pre_preprocessed_data.csv",index = False)
"""
print data.head(5)
