from sklearn import datasets
from sklearn.datasets import load_boston 
from sklearn.linear_model import LinearRegression 

dataset= load_boston()
x = datasets('data')
y = datasets('target')

model = LinearRegression
model.fit (x,y)


