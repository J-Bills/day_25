# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = list()
#     for row in data:
#         if (row[1] != 'temp'):
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data = pd.read_csv('./weather_data.csv')
# # print(data['temp'])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print('**************')
# print(temp_list)

# """ Average temp from temp list using pandas mean"""

# # temp_sum = sum(temp_list)
# # print(temp_sum/len(temp_list))

# print(data['temp'].mean())

# """Get date in columns"""
# print(data['condition'])
# #or
# print(data.condition) 

# #Get data in Row
# print(data[data.day == 'Monday'])

# #Print data in row where temp was at the max
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']

print(monday)

#Create a dataframe from scratch

data_dict = {
    'students': ["Amy", "James", "Tom"],
    'scores': [90,90,90]
}

custom_df = pd.DataFrame(data_dict)
custom_df.to_csv("new_data.csv")
