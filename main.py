import pandas as pd
import numpy as np




data_2016 = pd.read_csv("mental-heath-in-tech-2016_20161114.csv")
data_2017 = pd.read_csv("OSMI Mental Health in Tech Survey 2017.csv")
data_2018 = pd.read_csv("OSMI Mental Health in Tech Survey 2018.csv")
data_2019 = pd.read_csv("OSMI 2019 Mental Health in Tech Survey Results - OSMI Mental Health in Tech Survey 2019.csv")
data_2020 = pd.read_csv("OSMI 2020 Mental Health in Tech Survey Results .csv")
data_2021 = pd.read_csv("OSMI 2021 Mental Health in Tech Survey Results .csv")


data_2016_columns = pd.Series(data_2016.columns)
data_2017_columns = pd.Series(data_2017.columns)
data_2018_columns = pd.Series(data_2018.columns)
data_2019_columns = pd.Series(data_2019.columns)
data_2020_columns = pd.Series(data_2020.columns)
data_2021_columns = pd.Series(data_2021.columns)

data_2016_columns_fixed = data_2016_columns.replace(to_replace=r"<.+?>", value="", regex=True)
data_2017_columns_fixed = data_2017_columns.replace(to_replace=r"<.+?>", value="", regex=True)
data_2018_columns_fixed = data_2018_columns.replace(to_replace=r"<.+?>", value="", regex=True)
data_2019_columns_fixed = data_2019_columns.replace(to_replace=r"<.+?>", value="", regex=True)
data_2020_columns_fixed = data_2020_columns.replace(to_replace=r"<.+?>", value="", regex=True)
data_2021_columns_fixed = data_2021_columns.replace(to_replace=r"<.+?>", value="", regex=True)

test = pd.DataFrame(data_2017, columns=data_2017_columns_fixed)
print(test.columns)

