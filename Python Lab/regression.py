import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


path = '/Users/gregnelson/Downloads/automobileEDA.csv'
df = pd.read_csv(path)
# print(df.head())

#simple linear regression   

lm = LinearRegression()

x = df[['highway-mpg']]
y  = df['price']

lm.fit(x,y)
yhat = lm.predict(x)

# print('The predicted prices are: ', yhat[0:5])
# print('The intercept is: ', lm.intercept_)
# print('The coefficient is: ', lm.coef_)

price = lm.intercept_ + lm.coef_ * x
# print('The prices are: ', price[0:5])

lm1=LinearRegression()

x1 = df[['engine-size']]
y1 = df['price']

lm1.fit(x1,y1)
yhat1 = lm1.predict(x1)

# print('The predicted prices are: ', yhat1[0:5])
# print('The intercept is: ', lm1.intercept_)
# print('The coefficient is: ', lm1.coef_)

price1 = lm1.intercept_ + lm1.coef_ * x1
# print('The prices are: ', price1[0:5])

lm3 = LinearRegression()

z = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm3.fit(z, df['price'])

# print('The predicted prices are: ', lm3.predict(z)[0:5])
# print('the intercept is : ', lm3.intercept_)
# print('the coefficient is:', lm3.coef_)

price2 = lm3.intercept_ + lm3.coef_[0] * z['horsepower']+ lm3.coef_[1] * z['curb-weight'] + lm3.coef_[2] * z['engine-size'] + lm3.coef_[3] * z['highway-mpg']
# print('the prices are:', price2[0:5])

lm4 = LinearRegression()

z1 = df[['normalized-losses', 'highway-mpg']]

lm4.fit(z1,df['price'])
 
# print('the predicted prices are:',lm4.predict(z1)[0:5])
# print('the intercept is:', lm4.intercept_)
# print('the coef is:', lm4.coef_)

price3 = lm4.intercept_ + lm4.coef_[0] * z1['normalized-losses'] + lm4.coef_[1] * z1['highway-mpg']
# print ('the price is:', price3[0:5])

# width = 12
# height = 10
# plt.figure(figsize=(width,height))
# sns.regplot(x=df['peak-rpm'], y=df['price'], data=df)
# plt.ylim(0,)
# plt.show()

# print(df[['price', 'peak-rpm','highway-mpg']].corr())

#Residual plot

width = 12 
height = 10
# plt.figure(figsize=(width, height))
# sns.residplot(x=df['highway-mpg'], y=df['price'])
# plt.show()
z2 = df[['horsepower', 'curb-weight', 'engine-size', 'highway-mpg']]
lm5 = LinearRegression()
lm5.fit(z2, df['price'])
yhat = lm5.predict(z2)

# plt.figure(figsize=(width, height))
# sns.kdeplot(df['price'], label='Actual Values', color='blue')
# sns.kdeplot(yhat, label='Fitted Values', color='red')
# plt.title('Actual vs Fitted Values for Price')
# plt.xlabel('Price (in dollars)')
# plt.ylabel('Proportion of Cars')
# plt.show()
# plt.close()

# polynominal regression and pipelines

def plotpolly(model, independent_variable, dependent_variable, name):
    x_new = np.linspace(15,55,100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variable, '.', x_new, y_new, '-')
    plt.title('ploynomial fit with matplotlib for price ~ length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(name)
    plt.ylabel('price of cars')
    plt.show()
    plt.close()


x = df['highway-mpg']
y = df['price']
f = np.polyfit(x, y, 3)
p = np.poly1d(f)
# plotpolly(p, x, y, 'highway-mpg')

#multivariate polynominal regression
from sklearn.preprocessing import PolynomialFeatures

# pr = PolynomialFeatures(degree=2)
# z_pr = pr.fit_transform(z) 

# print(z.shape)
# print(z_pr.shape)

#pipelines
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# input = [(('scale', StandardScaler())), ('polynomial', PolynomialFeatures(include_bias=False)), ('model', LinearRegression())]  # create a list of tuples including scaling, polynomial transform and linear regression steps
# pipe=Pipeline(input)    # create a pipeline object with the list as argument

# z=z.astype(float)   # convert to float to avoid error with StandardScaler
# pipe.fit(z,y)   # fit the pipeline with the features and target variable

# ypipe = pipe.predict(z) # predict the target variable using the pipeline
# print('the predicted value is:', ypipe[0:4])

# input1 = [('scale1', StandardScaler()), ('model1', LinearRegression())]

# pipe1=Pipeline(input1)
# z1 = z1.astype(float)

# pipe1.fit(z1,y)   # fit the pipeline with the features and target variable
# ypipe1 = pipe1.predict(z1)
# print('the predicted value is:', ypipe1[0:6])

#measures for in-sample evaluation of the model

#model 1 simple linear
#calculate R-squared, for highway-mpg
# lm.fit(x,y)
# print('the r square is:', lm.score(x,y))

#calculate mean squared error(MSE) for highway-mpg
# yhat = lm.predict(x)
# print('the predicted values are:', yhat[0:4])

from sklearn.metrics import mean_squared_error
# mse = mean_squared_error(df['price'], yhat)
# print('the mse is:', mse)

#model 2 multi linear regression
# lm.fit(z, df['price'])
# print('the rsquare is:', lm.score(z, df['price']))

# y_predict_multifit = lm.predict(z)
# print('the predicted values are:', y_predict_multifit[0:4])

#mse for multi linear regression
# print('the mse is:', mean_squared_error(df['price'], y_predict_multifit))

#model 3 polynomial regression
from sklearn.metrics import r2_score

r_squared = r2_score(y, p(x))
# print('the r squared is:', r_squared)

# mse for polynomial regression
# print('the mse is:', mean_squared_error(df['price'], p(x)))

#prediction and decision making
x = df[['highway-mpg']]
new_input = np.arange(1, 100, 1).reshape(-1, 1)
#fit the model
lm.fit(x, y)
#predict the model
yhat = lm.predict(new_input)
print(yhat[0:5])

plt.plot(new_input, yhat)
plt.show()



