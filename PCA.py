# -*- coding: utf-8 -*-

from google.colab import drive
drive.mount('/content/drive')

# Answer to the question 3. Part(b) without centering

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import pandas

result = pandas.read_csv('Dataset3.csv')

to = result.size/2;

C = [[0,0], 
    [0,0] ]  

for i in range(0, int(to) ):
  x = result[i:i+1]
  X = x.to_numpy()
  XT = X.transpose()
  C += XT@X

C = C/int(to)
#print(C)

results = la.eig(C)
print(results[0])
print(results[1])

# Answer to the question 3. Part(a) with centering 

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import pandas

result = pandas.read_csv('Dataset3.csv')

to = result.size/2;

whdata = result[0:int(to)]
WHdata = whdata.to_numpy()
#print(WHdata[0][1])
meanmat = np.mean(WHdata, axis=0)

#centering the data
for i in range(0, int(to) ):
  WHdata[i][0] -= meanmat[0]
  WHdata[i][1] -= meanmat[1]
#end of data centering

C = [[0,0], 
    [0,0] ] 

for i in range(0, int(to) ):
  X = WHdata[i:i+1]
  XT = X.transpose()
  C += XT@X

C = C/int(to)
#print(C)

results = la.eig(C)
print(results[0])
print(results[1])

y = np.array([[1, 2, 3], [5, 6, 1]])

np.mean(y, axis=0) # first axis

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
import pandas

result = pandas.read_csv('Dataset3.csv')

to = result.size/2;
C=0;
#C = [[0,0], 
#    [0,0] ]  

for i in range(0, int(to) ):
  x = result[i:i+1]
  X = x.to_numpy()
  XT = X.transpose()
  C += X@XT

C = C/int(to)
print(C)

results = la.eig(C)
print(results[0])
#print(results[1])
