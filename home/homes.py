import pandas as pd

df = pd.read_csv("housing.csv")
print(df.head(15))

missing_values = df.isnull().sum()


print("columns with missing values:")
print(missing_values[missing_values > 0])


total_bedrooms_mean = df ['total_bedrooms'].mean()
print("total_bedrooms_mean:",total_bedrooms_mean)
df["total_bedrooms"]=df["total_bedrooms"].fillna("total_bedrooms_mean")
print(df.isna().sum())    

min_price = float(input("Enter the minimum price:"))
max_price = float(input("Enter the maximum price:"))

filtered_houses = df[(df['median_house_value'] >= min_price) & (df['median_house_value'] <= max_price)]


print(filtered_houses)
