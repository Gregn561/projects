#Modeling data
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as wid
import seaborn as sns

path = path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/module_5_auto.csv'
df = pd.read_csv(path)
# print(df.head())
df.to_csv('module_5_auto.csv')

df=df._get_numeric_data()
# print(df.head())

from ipywidgets import interact, interactive, fixed, interact_manual

def distributionplot(redfunction, bluefunction, redname, bluename, title):
    width  =12
    height = 10
    plt.figure(figsize=(width,height))
    ax1 = sns.kdeplot(redfunction, color = 'r', label = redname)
    ax2 = sns.kdeplot(bluefunction, color = 'b', label = bluename)
    plt.title('Title')
    plt.xlabel('price in dollars')
    plt.ylabel('proportion of cars')
    plt.show()
    plt.close()

def pollyplot(xtrain, xtest, ytrain, ytest, lr, poly_transform):
    width = 12
    height = 10
    plt.figure(figsize = (width, height))
    #training data
    #testing data
    #lr: linear regression object
    #poly_transform: polynomial transformation function

    xmax = max(xtrain.values.max(), xtest.values.max())
    #the maximum value among xtrain and xtest is assigned to xmax. This value is used to create a range of values from the minimum to the maximum for plotting the polynomial regression curve.
    xmin = min(xtrain.values.min(), xtest.values.min())
    #the minimum value among xtrain and xtest is assigned to xmin. This value is used to create a range of values from the minimum to the maximum for plotting the polynomial regression curve.

    x= np.arange(xmin, xmax, 0.1)
    #transforming x data using polynomial transformation function

    plt.plot(xtrain, ytrain, 'ro', label = 'training data')
    plt.plot(xtest, ytest, 'go', label = 'test data')
    plt.plot(x, lr.predict(poly_transform.fit_transform(x.reshape(-1,1))), label = 'predicted function')
    plt.ylim([-10000, 60000])
    plt.ylabel('price')
    plt.legend()
    plt.show()
    plt.close()

ydata = df['price']
xdata = df.drop('price', axis = 1)

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(xdata, ydata,test_size = .10, random_state = 1)
#the train_test_split function is used to split the dataset into training and testing sets. The test_size parameter specifies the proportion of the dataset to be included in the test set, which is set to 0.10 (10% of the data). The random_state parameter is set to 1 to ensure that the split is reproducible.

# print('number of test samples:', xtest.shape[0])
# print('number of training samples:', xtrain.shape[0])

xtrain1, xtest1, ytrain1, ytest1 =  train_test_split(xdata, ydata, test_size=.40, random_state=0)

# print('number of test samples:', xtest1.shape[0])
# print('number of training samples:', xtrain1.shape[0])
from sklearn.linear_model import LinearRegression

lre = LinearRegression()
lre.fit(xtrain[['horsepower']], ytrain)
#The fit method is used to train the linear regression model using the training data. The model learns the relationship between the 'horsepower' feature and the target variable 'price' based on the training data provided.

b = lre.score(xtest[['horsepower']], ytest)
#The score method is used to evaluate the performance of the trained linear regression model on the test data. It calculates the coefficient of determination (R^2 score) for the predictions made by the model on the test set, which indicates how well the model explains the variance in the target variable 'price' based on the 'horsepower' feature.
# print(b) # the r^2 is 3635875575078824

c = lre.score(xtrain[['horsepower']], ytrain)
#The score method is used again to evaluate the performance of the trained linear regression model on the training data. It calculates the coefficient of determination (R^2 score) for the predictions made by the model on the training set, which indicates how well the model explains the variance in the target variable 'price' based on the 'horsepower' feature for the training data.
# print(c) # the r^2 is 0.6619724197515103

lre.fit(xtrain1[['horsepower']], ytrain1)

d = lre.score(xtest1[['horsepower']], ytest1)
# print(d) # the r^2 is 0.7139364665406973

#Cross-Validation Score
from sklearn.model_selection import cross_val_score
rcross = cross_val_score(lre, xdata[['horsepower']], ydata, cv=4)
#The cross_val_score function is used to perform cross-validation on the linear regression model. It evaluates the model's performance by splitting the dataset into 4 folds (as specified by cv=4) and calculating the R^2 score for each fold. The resulting scores are stored in the variable rcross, which contains the R^2 scores for each fold of the cross-validation process.

#print(rcross)
# print('the mean of the folds are', rcross.mean(), 'the standard deviation is ', rcross.std() )

mse_scores = -1 * cross_val_score(lre, xdata[['horsepower']], ydata, cv=4, scoring = 'neg_mean_squared_error')
#The cross_val_score function is used again to perform cross-validation on the linear regression model, but this time it calculates the negative mean squared error (MSE) for each fold instead of the R^2 score. The scoring parameter is set to 'neg_mean_squared_error' to specify that we want to evaluate the model based on the negative MSE. The resulting scores are multiplied by -1 to convert them back to positive MSE values, which are easier to interpret. The output will be an array of MSE values for each fold of the cross-validation process._

rcross1 = cross_val_score(lre, xdata[['horsepower']], ydata, cv=2)

mse_scores1 = -1 * cross_val_score(lre, xdata[['horsepower']], ydata, cv=2, scoring = 'neg_mean_squared_error')
# print('the mean of the folds are', rcross1.mean())

#You can also use the function 'cross_val_predict' to predict the output. The function splits up the data into the specified number of folds, with one fold for testing and the other folds are used for training.

from sklearn.model_selection import cross_val_predict
yhat = cross_val_predict(lre, xdata[['horsepower']], ydata, cv=4)
# print(yhat[:5])

#overfitting and underfitting model selection
#test data, sometimes referred to as the "out of sample data", is a much better measure of how well your model performs in the real world.

lr = LinearRegression()
lr.fit(xtrain[['horsepower', 'curb-weight','engine-size','highway-mpg']], ytrain)
# The fit method is used to train the linear regression model using the training data. The model learns the relationship between the specified features ('horsepower', 'curb-weight', 'engine-size', 'highway-mpg') and the target variable 'price' based on the training data provided.

yhat_train = lr.predict(xtrain[['horsepower','curb-weight','engine-size','highway-mpg']])
# print(yhat_train[:5])

yhat_test = lr.predict(xtest[['horsepower','curb-weight','engine-size','highway-mpg']])
# print(yhat_test[:5])

# title = 'Distribution  Plot of Predicted Value Using Training Data vs Predicted Value Using Test Data'
# distributionplot(ytrain, yhat_train, 'actual values (train)', 'predicted values (train)', title)
# the training data fits better than the test data, which is an indication of underfitting. The model is too closely fit to the training data and may not perform well on new, unseen data.

# title = 'Distribution plot of predicted value using test data vs data distribution of test data'
# distributionplot(ytest, yhat_test, 'actual values (test)', 'predicted values (test)', title)
# the predicted values using the test data do not fit well with the actual values of the test data, which is an indication of underfitting. The model is too simple and does not capture the underlying patterns in the data, resulting in poor performance on both the training and test data.

from sklearn.preprocessing import PolynomialFeatures

#overfitting the data
xtrain, xtest, ytrain, ytest = train_test_split(xdata, ydata, test_size = .45, random_state = 0)

pr = PolynomialFeatures(degree = 5)
xtrain_pr = pr.fit_transform(xtrain[['horsepower']])
xtest_pr = pr.fit_transform(xtest[['horsepower']])

poly = LinearRegression()
poly.fit(xtrain_pr, ytrain)
#The fit method is used to train the polynomial regression model using the transformed training data (xtrain_pr) and the target variable (ytrain). The model learns the relationship between the polynomial features of 'horsepower' and the target variable 'price' based on the training data provided.

yhat = poly.predict(xtest_pr)
# print(yhat[:5])

# print("Predicted values:", yhat[0:4])
# print("True values:", ytest[0:4].values)
# comparing the predicted values with the true values of the test set. The predicted values are generated by the polynomial regression model based on the transformed test data (xtest_pr), while the true values are the actual target variable values from the test set (ytest). This comparison helps to evaluate the performance of the polynomial regression model in predicting the target variable 'price' based on the 'horsepower' feature.

# pollyplot(xtrain['horsepower'], xtest['horsepower'], ytrain, ytest, poly, pr)

# print("Training score:", poly.score(xtrain_pr, ytrain))
# print("Test score:", poly.score(xtest_pr, ytest))
# the R^2 for the test data is in the negatives, which indicates that the model is performing worse than a horizontal line (which would have an R^2 of 0). This suggests that the polynomial regression model is overfitting the training data and does not generalize well to the test data, resulting in poor performance on unseen data.

rsqu_test = []
order = [1,2,3,4]
for n in order:
    pr = PolynomialFeatures(degree = n)
    xtrain_pr = pr.fit_transform(xtrain[['horsepower']])
    xtest_pr = pr.fit_transform(xtest[['horsepower']])
    lr.fit(xtrain_pr, ytrain)
    rsqu_test.append(lr.score(xtest_pr,ytest))

plt.plot(order, rsqu_test)
plt.xlabel('order')
plt.ylabel('R^2')
plt.title('R^2 Using Test Data')
plt.text(3, 0.75, 'maximum R^2')
# plt.show()
# plt.close()
# figure shows that the R^2 value is highest for a polynomial of degree 3, which suggests that a cubic polynomial may be the best fit for the data. However, it's important to consider other factors such as the complexity of the model and the potential for overfitting when selecting the appropriate degree for the polynomial regression model.

def f(order, test_data):
    xtrain, xtest, ytrain, ytest = train_test_split(xdata, ydata, test_size = .45, random_state = 0)
    pr= PolynomialFeatures(degree = order)
    xtrain_pr = pr.fit_transform(xtrain[['horsepower']])
    xtest_pr = pr.fit_transform(xtest[['horsepower']])
    poly = LinearRegression()
    poly.fit(xtrain_pr, ytrain)
    pollyplot(xtrain['horsepower'], xtest['horsepower'], ytrain, ytest, poly, pr)

# interact(f, order = (0,6,1), test_data = (0.05, 0.95, 0.05))

#Ridge Regression

pr = PolynomialFeatures(degree = 2)
xtrain_pr = pr.fit_transform(xtrain[['horsepower', 'curb-weight','engine-size','highway-mpg','normalized-losses','symboling']])
xtest_pr = pr.fit_transform(xtest[['horsepower','curb-weight','engine-size','highway-mpg','normalized-losses','symboling']])

from sklearn.linear_model import Ridge 

ridgemodel = Ridge(alpha = 0.1)
ridgemodel.fit(xtrain_pr, ytrain)

yhat = ridgemodel.predict(xtest_pr)

# print('predicted:', yhat[0:4])
# print('test set:', ytest[0:4].values)

from tqdm import tqdm

rsqu_test = []
rsqu_train = []
dummy1 = []
alpha = 10 * np.array(range(0,1000))
pbar = tqdm(alpha)

for a in pbar:
    ridgemodel = Ridge(alpha = a)
    ridgemodel.fit(xtrain_pr, ytrain)
    test_score, train_score = ridgemodel.score(xtest_pr, ytest), ridgemodel.score(xtrain_pr, ytrain)
    rsqu_test.append(test_score)
    rsqu_train.append(train_score)
    
width = 12
height = 10
plt.figure(figsize=(width, height))
plt.plot(alpha,rsqu_test, label='validation data  ')
plt.plot(alpha,rsqu_train, 'r', label='training Data ')
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.legend()
# plt.show()
# plt.close()

#Grid Search
#makes finding the hyperparameters easier. It is a way to systematically work through multiple combinations of parameter tunes, cross-validating as it goes to determine which tune gives the best performance. The GridSearchCV object implements the "fit" and "predict" methods like any classifier, and can be used as a regular classifier in the rest of your code.
from sklearn.model_selection import GridSearchCV

parameters1 = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000, 10000, 100000, 100000]}]
#creating a dictionary of parameters to be tuned. In this case, we are tuning the 'alpha' parameter of the Ridge regression model, which controls the strength of regularization. The values provided in the list are the different values of 'alpha' that will be tested during the grid search process.

rr = Ridge()
# creating an instance of the Ridge regression model. This model will be used in the grid search process to evaluate the performance of different 'alpha' values.

grid1 = GridSearchCV(rr, parameters1, cv=4)
# creating an instance of the GridSearchCV class, which will perform the grid search for hyper

grid1.fit(xdata[['horsepower','curb-weight','engine-size','highway-mpg','normalized-losses','symboling']], ydata)
# fitting the GridSearchCV object to the data. This will perform the grid search by evaluating

bestrr = grid1.best_estimator_
# retrieving the best estimator (model) found during the grid search process. This model will have the optimal 'alpha' value that resulted in the best performance based on the cross-validation scores.

bestrr.score(xtest[['horsepower','curb-weight','engine-size','highway-mpg','normalized-losses','symboling']], ytest)
# evaluating the performance of the best Ridge regression model (bestrr) on the test data








