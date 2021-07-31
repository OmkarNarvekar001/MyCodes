#1
import pandas as pd
df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
(df.head(5))
(df.tail(5))

#2
df = pd.read_csv("D:\\Downloads\\Automobile_data.csv", na_values={
'price':["?","n.a","NaN"],
'engine-type':["?","n.a","NaN"],
'horsepower':["?","n.a","NaN"],
'average-mileage':["?","n.a","NaN"]}) (df)
df.to_csv("D:\\Downloads\\Automobile_data.csv")

#3
df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
df = df [['company','price']][df.price==df['price'].max()]
(df)


#4
df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
carmanufacturers = df.groupby('company')
toyota = carmanufacturers.get_group('toyota')
(toyota)

#5
df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
df['company'].value_counts()

#6
df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
carmanufacturers = df.groupby('company')
price = carmanufacturers ['company','price'].max()
print(price)

#7
df = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
carmanufacturers = df.groupby('company')
mileage = carmanufacturers ['company','average-mileage'].mean()
print(mileage)

#8
cars = pd.read_csv("D:\\Downloads\\Automobile_data.csv")
cars= cars.sort_values(by=['price'], ascending=False)
cars.head(5)