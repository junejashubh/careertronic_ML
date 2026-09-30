# Simple Linear Regression
#%%
# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#%%
# Importing the dataset
dataset = pd.read_csv('/Users/shubhamjuneja/Desktop/Amity/Machine Learning A-Z (Codes and Datasets)/Part 2 - Regression/Section 4 - Simple Linear Regression/Python/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
#%%
# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
import sklearn.metrics as sk_metric
regressor = LinearRegression()
regressor.fit(X_train, y_train)
#%%
y_train_pred = regressor.predict(X_train)
#%%
# Predicting the Test set results
y_pred = regressor.predict(X_test)
#%%
r2_value = sk_metric.r2_score(y_test,y_pred)
#%%
# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
#%%
# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
#%%

[a = 'NY','CAL','XYX']

for i in range(len(a)):
    data_x = data.loc[data['State']==a[i],]
    #regresss
