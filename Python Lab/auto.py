import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(filename, names = headers)

df.replace("?", np.nan, inplace = True)

missing_data = df.isnull()

# for column in missing_data.columns.values.tolist():
#     print(missing_data[column].value_counts())
#     print("")

# calculate and replace
# avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
# print("average of normalized-losses", avg_norm_loss)
# df["normalized-losses"].replace(np.nan, avg_norm_loss)

# avg_bore = df["bore"].astype("float").mean(axis=0)
# print("average of bore", avg_bore)
# df["bore"].replace(np.nan, avg_bore)

# avg_strk = df["stroke"].astype("float").mean(axis=0)
# print("average of stroke", avg_strk)
# df["stroke"].replace(np.nan, avg_strk)

df['horsepower'] = df['horsepower'].fillna(0).astype(int)     #cannot convert NaN into integer use .fillna() to replace then convert
avg_horsepower = df["horsepower"].mean(axis=0)
# print("Average horsepower:", avg_horsepower)

# avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
# print("Average peak rpm:", avg_peakrpm)
# df['peak-rpm'].replace(np.nan, avg_peakrpm)

#most common value/frequency
# print(df["num-of-doors"].value_counts())  #counts the number of values in the column

# print(df['num-of-doors'].value_counts().idxmax())   #gives the most common value

# df["num-of-doors"].replace(np.nan, "four")

#dropping rows
# df.dropna(subset=["price"], axis=0, inplace=True)
# df.reset_index(drop=True, inplace=True)   # reset index, because we droped two rows
# print(df.head())

#coverting data types
#print(df.dtypes)
# df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
# df[["normalized-losses"]] = df[["normalized-losses"]].astype("float")
# df[["price"]] = df[["price"]].astype("float")
# df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")


#Data standardization
#convert mpg to l/km
#df["city-L/100"] = 235/df["city-mpg"]
# df["highway-mpg"] = 235/df["highway-mpg"]
# df.rename(columns = {"highway-mpg":"highway-L/km"}, inplace = True)
# print(df.head())

#Data Normalization
# df["length"] = df["length"]/df["length"].max()
# df["width"] = df["width"]/df["width"].max()
# df["height"] = df["height"]/df["height"].max()

# print(df[["width","height","length"]])

# #Binning
# df["horsepower"] = df["horsepower"].astype("int")
import matplotlib
# plt.hist(df["horsepower"])

# plt.xlabel("horsepower")
# plt.ylabel("count")
# plt.title("horsepower bins")
# # plt.show()

# bins = np.linspace(min(df["horsepower"]), max(df["horsepower"]), 4)
# group_names = ['Low', 'Medium', 'High']
# df['horsepower-binned'] = pd.cut(df['horsepower'], bins, labels=group_names, include_lowest=True )
# # print(df[["horsepower","horsepower-binned"]].head(20))
# # print(df["horsepower-binned"].value_counts())
# plt.bar(group_names, df["horsepower-binned"].value_counts())

# # set x/y labels and plot title
# plt.xlabel("horsepower")
# plt.ylabel("count")
# plt.title("horsepower bins")
# plt.show()

dummy_variable_1 = pd.get_dummies(df["fuel-type"])
dummy_variable_1.rename(columns = {'gas':'fuel-type-gas', 'diesel':'fuel-type-diesel'}, inplace = True)
# print(dummy_variable_1.head())

df = pd.concat([df, dummy_variable_1], axis=1)
df.drop('fuel-type', axis=1, inplace=True)
# print(df.head())

dummy_variable_2 = pd.get_dummies(df['aspiration'])
dummy_variable_2.rename(columns={'aspiration': 'aspiration-std', 'turbo': 'aspiration-turbo'}, inplace = True)
# print(dummy_variable_2.head())

df = pd.concat([df, dummy_variable_2], axis = 1)
df.drop('aspiration', axis = 1, inplace=True)
# print(df.head())

