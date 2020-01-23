import pandas

data=pandas.read_csv(r"C:\Users\Hanshik\Desktop\Datasets\weather_by_cities.csv")

cities=data.groupby("city")

# for city in cities:
#     print(city)


mumbai=cities.get_group("mumbai")
print(mumbai)
print(mumbai.max())
print(mumbai.min())



