import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 
from scipy import stats
path='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/automobileEDA.csv'
df = pd.read_csv(path)

# Find the correlation between 'bore', 'stroke', 'compression-ratio', and 'horsepower'
# print(df[['bore', 'stroke', 'compression-ratio', 'horsepower']].corr())


#Continuos variables
#Positive
# #linear regression plot 
# sns.regplot(x='engine-size', y='price', data=df)
# plt.ylim(0,)
#plt.show()
#print(df[['engine-size','price']].corr())

#Negative
# sns.regplot(x='highway-mpg',y='price', data = df)
# #plt.show()
# print(df[['highway-mpg','price']].corr())

#Weak
# sns.regplot(x='peak-rpm',y='price', data=df)
# plt.show()
# print(df[['peak-rpm','price']].corr())

# sns.regplot(x='stroke',y='price', data=df)
# plt.show()
# print(df[['stroke','price']].corr())

#Categorical variables
# sns.boxplot(x='body-style',y='price', data=df)
# plt.show()
# print(df[['body-style','price']].corr())

# sns.boxplot(x='engine-location',y='price', data=df)
# plt.show()
# print(df[['engine-location','price']].corr())

# sns.boxplot(x='drive-wheels',y='price', data=df)
# plt.show()
# print(df[['drive-wheels','price']].corr())

#Descriptive statistics
# print(df.describe())
# print(df.describe(include=['object']))

#Value counts
# print(df['drive-wheels'].value_counts())
drive_wheels_counts = df['drive-wheels'].value_counts().to_frame(name='value_counts')   #.to_frame(name='value_counts') to convert series to dataframe and name the column as value_counts all in one line
#drive_wheels_counts.rename(columns={'count':'value_counts'}, inplace=True) #to rename the column name from count to value_counts, inplace=True to make the change in the original dataframe if not using last line
#print(drive_wheels_counts)

#drive_wheels_counts.index.name = 'drive-wheels'    #to name the index as drive-wheels, this is optional but it is good practice to name the index when converting series to dataframe
#print(drive_wheels_counts)

engine_loc_counts = df['engine-location'].value_counts().to_frame(name='value_counts')
#engine_loc_counts.index.name = 'engine-location'
#print(engine_loc_counts.head(10))

#Grouping
#print(df['drive-wheels'].unique())
#print(df.corr())

df_group_one = df[['drive-wheels','body-style','price']]
df_group_one = df_group_one.groupby(['drive-wheels', 'body-style'],as_index=False).mean()
#print(df_group_one)

grouped_pivot = df_group_one.pivot(index='drive-wheels', columns='body-style')
grouped_pivot.fillna(0, inplace=True) #fill NaN values with 0
# print(grouped_pivot)


#P-value
#P-value tells how statistically significant our calculated score value is.
#Pearson correlation coefficient and p-value

#pearson_coef, p_value = stats.pearsonr(df['wheel-base'], df['price'])
#print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value) #The Pearson Correlation Coefficient is 0.584641822265508 which is strong with a P-value of P = 8.076488270733218e-20 less than 0.001 which means the correlation is statistically significant.

# pearson_coef, p_value = stats.pearsonr(df['horsepower'], df['price'])
# print("The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P =", p_value)

#Anova
#F-test score: ANOVA assumes the means of all groups are the same, calculates how much the actual means deviate from the assumption, and reports it as the F-test score. A larger score means there is a larger difference between the means.

grouped_test2=df_group_one[['drive-wheels', 'price']].groupby(['drive-wheels'])
# print(grouped_test2.head(2))

# print(grouped_test2.get_group(('rwd',))['price'])

# f_val, p_val = stats.f_oneway(grouped_test2.get_group(('fwd',))['price'], grouped_test2.get_group(('rwd',))['price'], grouped_test2.get_group(('4wd',))['price'])
# print('Anova results: f=', f_val, 'p=', p_val)

# f_val, p_val = stats.f_oneway(grouped_test2.get_group(('fwd',))['price'], grouped_test2.get_group(('rwd',))['price'])
# print('Anova results: f=', f_val, 'p=', p_val)

# f_val, p_val = stats.f_oneway(grouped_test2.get_group(('fwd',))['price'], grouped_test2.get_group(('4wd',))['price'])
# print('Anova results: f=', f_val, 'p=', p_val)
#We notice that ANOVA for the categories 4wd and fwd yields a high p-value > 0.1, so the calculated F-test score is not very statistically significant. This suggests we can't reject the assumption that the means of these two groups are the same, or, in other words, we can't conclude the difference in correlation to be significant.


