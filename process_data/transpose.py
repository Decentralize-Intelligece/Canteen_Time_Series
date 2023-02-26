# load data from ../data/processed_data/<canteenH>/interval_counts.csv
from pathlib import Path
import pandas as pd

# df head max col
pd.set_option('display.max_columns', None)

# load each csv file in ../data/processed_data/<canteenH>/interval_counts.csv
for file in Path("../data/processed_data/original_to_csv/").glob("*/interval_counts.csv"):
    print(file)
    # read csv file as dataframe
    df = pd.read_csv(file)
    # print(df.head())
    # transpose creating new column for each record as index
    df = df.transpose()
    # print(df.head())
    # reset index

    # rename first column name to datetime
    df = df.rename(columns={df.columns[0]: "datetime"})

    # df = df.reset_index()
    print(df.head())

    # save dataframe to csv in ../data/processed_data/<canteenH>_interval_counts_transposed.csv
    df.to_csv("../data/processed_data/transposed/" + file.parent.name + "_interval_counts_transposed.csv")
