""" Helper Functions Assignment """

import pandas as pd
import numpy as np

def null_count(df):
    # return the amount of null values in a dataframe
    return df.isnull().sum()

def randomized(df, seed):
    np.random.seed(seed)
    df = df.iloc[np.random.shuffle(len(df))].reset_index(drop=True)
    return df