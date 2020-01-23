import pandas

data=pandas.read_csv(r"C:\Users\Hanshik\Desktop\Datasets\weather_by_cities.csv")

print(data.shape)

print(data)

#Sort the dataframe
#data.sort_values("city",inplace=True)
#drop all the duplicates on the data frames after sorting
print("******************************************************")
data.drop_duplicates(subset=["city"],keep="last",inplace=True)

print(data)