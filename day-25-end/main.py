"""Goal"""
#Create a dataframe that sums the squirrel data fomr central park based on fur color
#Create a csv using that data frame

import pandas as pd

data_dict = dict()
data = pd.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    'Fur_Color' : ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
    }

print(data_dict)

custom_frame = pd.DataFrame(data_dict)
custom_frame.to_csv("squirrel_data.csv")

