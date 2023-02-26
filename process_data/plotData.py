# load data from ../data/processed_data/<canteenH>/interval_counts.csv
from pathlib import Path
import pandas as pd

# df head max col
pd.set_option('display.max_columns', None)

# plot data
import matplotlib.pyplot as plt
import seaborn as sns

# set the style of the plots
sns.set_style("whitegrid")

# set the size of the plots
plt.rcParams["figure.figsize"] = (20, 10)

# load each csv file in ../data/processed_data/canteen<H>_interval_counts_transposed.csv
for file in Path("../data/processed_data/10000").glob("*.csv"):
    print(file)
    # read csv file as dataframe only first 100 rows
    df = pd.read_csv(file, nrows=10000)
    # df = pd.read_csv(file)


    # load each csv file in ../data/processed_data/100/canteen<C>interval_counts_100.csv
    # read csv file as dataframe
    # df = pd.read_csv("../data/processed_data/100/canteenCinterval_counts_100.csv")

    # plot the sales, time, weekday, and holiday with respect to datetime in 4 plots and show same time
    fig, axes = plt.subplots(4, 1)
    sns.lineplot(x="datetime", y="sales", data=df, ax=axes[0])
    sns.lineplot(x="datetime", y="time", data=df, ax=axes[1])
    sns.lineplot(x="datetime", y="weekday", data=df, ax=axes[2])
    sns.lineplot(x="datetime", y="holiday", data=df, ax=axes[3])

    # show the plot
    # plt.show()

    # save the plot to png in ../data/processed_data/plots
    fig.savefig("../data/processed_data/" + file.name + ".png")

    # close the plot
    plt.close(fig)








