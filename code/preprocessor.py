import os
import pandas as pd
import numpy as np


class Preprocessor:

    def __init__(self, data=None, data_dir="./code/data_deliverable/data"):
        if data is None:
            data = []
        self.data = data
        self.data_dir = data_dir
        self.save_dir = None

    def load_data(self):
        assert len(self.data) == 0 and os.path.exists(self.data_dir)
        for file in os.listdir(self.data_dir):
            self.data.append((pd.read_csv(f"{self.data_dir}/{file}"), file))

        return self.data

    def save_preprocessed_data(self, data=None, save_dir="./code/data_deliverable/preprocessed_data", overwrite=True):
        self.save_dir = save_dir
        if data is None:
            data = self.data
        assert len(data) > 0
        if not overwrite and len(os.listdir(save_dir)) > 0:
            print(f"Directory {save_dir} is not empty. Set overwrite=True to overwrite.")
            return

        os.makedirs(save_dir, exist_ok=True)
        for i, df in enumerate(data):
            d, file = df
            d.to_csv(f"{save_dir}/{file}", index=False)

    def preprocess(self, drop_years=None):
        """
        Preprocess the data
        :param drop_years: years to drop in all data frames (list of years as integers)
        :return: preprocessed data
        """
        if len(self.data) == 0:
            self.load_data()
        data = [df for df, _ in self.data]

        # handle 'country' column by converting anything with 'country' in the name to 'Country'
        for i, df in enumerate(data):
            for col in df.columns:
                lower_col = col.lower()
                if 'country' in lower_col or 'region' in lower_col:
                    df.rename(columns={col: 'Country'}, inplace=True)
                    break

        # handle duplicates
        for i, df in enumerate(data):
            data[i] = df.drop_duplicates()

        # handle data types, remove commas from numbers
        for i, df in enumerate(data):
            for col in df.columns:
                if df[col].dtype == object:
                    try:
                        data[i][col] = pd.to_numeric(df[col].str.replace(',', ''))
                    except ValueError:
                        pass

        # handle years
        if drop_years is not None:
            for i, df in enumerate(data):
                if 'Year' in df.columns:
                    data[i] = df[~df["Year"].isin(drop_years)]
                else:
                    # assume year column is denoted by year number
                    # drop columns with year number in the name if it is in drop_years
                    data[i] = df[[col for col in df.columns if not any([str(year) in col for year in drop_years])]]

        # add back file names
        data = [(df, self.data[i][1]) for i, df in enumerate(data)]

        self.data = data

        return self.data

    def join_by_country(self, data=None, save=True):
        """
        Join data frames by country, putting all data in one data frame
        For every country, there should be one row with all data from all data frames
        If some country is missing from some data frame, the corresponding columns should be NaN
        If a column name is repeated in different data frames, the column name should be suffixed with the file name

        THERE IS ONE MAJOR ASSUMPTION HERE: When joining by country, if certain values are not available in a given
        year, we assume that the values are replicated from the previous year. Some parts become meaningless, especially
        if we have other years in the data denoting other information

        Example where data is repeated byt passport year is different (last column):
        China,"3,715,827",2022,Broadcasting equipment,"2,715,999",2022,62.0,85.0,2022.0
        China,"3,715,827",2022,Broadcasting equipment,"2,715,999",2022,67.0,80.0,2023.0
        China,"3,715,827",2022,Broadcasting equipment,"2,715,999",2022,68.0,80.0,2024.0

        :param data: data to join
        :param save: whether to save the joined data
        :return: joined data
        """
        if data is None:
            data = self.data
        assert len(data) > 0

        # join data frames by country
        passport_index = 0
        for i in range(len(data)):
            if 'passport_index' in data[i][1]:
                passport_index = i
                break
        joined_data = data[passport_index][0]
        for i in range(len(data)):
            if i == passport_index:
                continue
            joined_data = joined_data.merge(data[i][0], on='Country', how='outer',
                                            suffixes=('', f"_{data[i][1].split('.')[0]}"))

        # drop empty passport index rows
        joined_data = joined_data.dropna(subset=['Number of Visa-Free Destinations'])

        if save:
            os.makedirs(self.save_dir, exist_ok=True)
            joined_data.to_csv(f"{self.save_dir}/joined_data.csv", index=False)

        return joined_data
