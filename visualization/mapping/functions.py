import pathlib
import pandas as pd, numpy as np
import dash_bootstrap_components as dbc
from dash import html, dcc

def head(*args, n=3):
    for df in [*args]:
        print("COLS: ", df.shape[1])
        print("ROWS: ", df.shape[0])
        display(df.head(n))


def extract_group(df, prefix, keys=[], keep=[], keep_first_word=False) -> pd.DataFrame:
    """ Returns a df containing index plus columns that start with given prefix """

    if type(prefix) != list:
        prefix = [prefix]
    names = [item for sublist in [
                [c for c in df.columns if c.startswith(txt)] for txt in prefix
            ] for item in sublist ]

    result = df.copy()[keys + keep + names]

    for p in prefix:
        remove = f'{p}_'
        if keep_first_word:
            remove = f'{"_".join(p.split("_")[1:])}_'
        for c in result.columns:
            if c.startswith(p):
                result = result.rename(columns={c: c.replace(remove, '')})
    return result


def normalize(data, multiplier=None):
    result = (data - np.min(data)) / (np.max(data) - np.min(data))
    if multiplier:
        result = [v*multiplier for v in result]
    return result