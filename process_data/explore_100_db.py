# load data from ../data/processed_data/<canteenH>/interval_counts.csv
from pathlib import Path
import pandas as pd

# df head max col
pd.set_option('display.max_columns', None)

# # load each csv file in ../data/processed_data/<canteenH>/interval_counts.csv
# for file in Path("../data/processed_data").glob("*/interval_counts.csv"):
#     print(file)
#     # read csv file as dataframe
#     df = pd.read_csv(file)



# load each csv file in ../data/processed_data/100/canteen<C>interval_counts_100.csv
# read csv file as dataframe
df = pd.read_csv("../data/processed_data/100/canteenCinterval_counts_100.csv")
print(df.head())
print(df.columns)
print(df.index)
print(df.values)
print(df.dtypes)
print(df.shape)
print(df.info())
print(df.describe())
print(df.describe(include='all'))
print(df.describe(include=['object', 'float', 'int']))

# save above data(df.head, column, ...) to txt
with open("data.txt", "w") as f:
    f.write("Head of dataframe:")
    f.write(str(df.head()))
    f.write("\n\n\n\n\nColumn of dataframe:")
    f.write(str(df.columns))
    f.write("\n\n\n\n\nIndex of dataframe:")
    f.write(str(df.index))
    f.write("\n\n\n\n\nValue of dataframe:")
    f.write(str(df.values))
    f.write("\n\n\n\n\nData Type of dataframe:")
    f.write(str(df.dtypes))
    f.write("\n\n\n\n\nShape of dataframe:")
    f.write(str(df.shape))
    f.write("\n\n\n\n\nInfo of dataframe:")
    f.write(str(df.info()))
    f.write("\n\n\n\n\nDescribe of dataframe:")
    f.write(str(df.describe()))
    f.write("\n\n\n\n\nDescribe of dataframe (include object, float, int):")
    f.write(str(df.describe(include=['object', 'float', 'int'])))
