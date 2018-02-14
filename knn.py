# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:49:22 2018

@author: Naresh Mehta
@description: Predict the house prices for the test data based on the sample
data and 3 independent variables number of rooms, size of house and age of
house.
"""
from sklearn.neighbors import KNeighborsRegressor

"""
Training Data Set:

|Sample No. | y: Price of the house | x1 : Number of rooms | x2 : Size of house (m 2 ) | Age of House (year) |
|-|-|-|-|-|
| 1 | 500.000 | 2 | 45 | 25 |
| 2 | 800.000 | 3 | 65 | 30 |
| 3 | 1.000.000 | 6 | 100 | 40 |
| 4 | 350.000 | 2 | 30 | 20 |
| 5 | 100.000 | 2 | 25 | 20 |


Test Data Set:

|Sample No. | y: Price of the house | x1 : Number of rooms | x2 : Size of house (m 2 ) | Age of House (year) |
|-|-|-|-|-|
| 1 | ?? | 4 | 100 | 25 |
| 2 | ?? | 1 | 60 | 20 |
"""

def predict_prices():
    # X is an array of x1 (Number of rooms), x2 (Size of the house) and
    # x3 (Age of the house). Y is the price of the house
    X = [[2,45,25],[3,65,30],[6,100,40],[2,30,20],[2,25,20]]
    y = [500000, 800000, 1000000, 350000, 100000]

    # Predict using KNN regression for K = 1
    run_knn(X, y, 1)
    # Now predict with K = 2
    run_knn(X, y, 2)

def run_knn(X, y, n):
    knn = KNeighborsRegressor(n_neighbors=n)
    knn.fit(X, y)

    print("K = ", n, "Test Sample 1 price: ", knn.predict([[4,100,25]]))
    print("K = ", n, "Test Sample 2 price: ", knn.predict([[1,60,20]]))

if __name__ == "__main__":
    predict_prices()
