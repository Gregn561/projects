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
plt.figure(figsize=(width, height))
sns.residplot(df['highway-mpg'], df['price'])
plt.show()




