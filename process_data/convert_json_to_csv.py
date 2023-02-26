import os
import os
import json
import pandas as pd

# load each json file in canteens/<canteenH>/preparedData
for file in os.listdir("../data/canteens"):
    if os.path.isdir("../data/canteens/" + file + "/preparedData"):
        print(file)
        # read json file as dataframe
        df = pd.read_json("../data/canteens/" + file + "/preparedData/interval_counts.json")
        print(df.head())
        # save dataframe to csv in canteens/<canteenH>/preparedDataCSV
        df.to_csv("../data/canteens/" + file + "/preparedDataCSV/interval_counts.csv")


    # with open("../data/canteens/" + file + "/preparedData/" + "interval_counts.json") as f:
    #     data = pd.read_json(f)
    #     print(data.head())
    #     # data.to_csv("datasave.csv")
    #     #

#
# # load data from json file and save it to csv file
# with open("datasave.json") as f:
#     data = json.load(f)
#
# # show all column in df head max col
# pd.set_option('display.max_columns', None)
#
# # print the first 5 rows of the dataset
# print(data.head())
#
# # save data to csv
# data.to_csv("datasave.csv")
#
# # load data from json file and save it to csv file
# # import pandas as pd
# # import matplotlib.pyplot as plt
#
# # read json file
# # data = pd.read_json("data.json")
#
# # print the first 5 rows of the dataset
# print(data.head())
#
