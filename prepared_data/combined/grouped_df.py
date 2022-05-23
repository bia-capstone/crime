import pandas as pd
from copy import deepcopy


def separate_by(df, txt, keys=['year', 'county'], keep=[], start=False, end=False, mode="") -> (pd.DataFrame, pd.DataFrame):
    """
    Given a df and a substring, return two dfs:
    1. df containing: county + all columns whose name does NOT contain substring
    2. df containing: county + all columns whose name DOES contain substring
    """
    names = [c for c in df.columns if (
            c.startswith(txt) if start else c.endswith(txt) if end else txt in c
        )]
    include = df.copy()[keys + keep + names]
    exclude = df.copy().drop(columns = keep + names)
    return include if mode == 'include' else exclude if mode == 'exclude' else (include, exclude)



class GroupedDF(object):
    groups = {}

    def __init__(self, df, custom={}):
        self._df = deepcopy(df)
        self._custom = custom
        self.set_groups()
    
    def set_groups(self):
        self._dict = {g: separate_by(self._df, g, start=True, mode='include') for g in GroupedDF.groups.keys()}
        for name, cols in self._custom.items():
            self._dict[name] = self._df[cols]
        for k, v in self._dict.items():
            setattr(self, k, v)
        
    @property
    def df(self):
        return self._df
    
    @df.setter
    def df(self, new):
        self._df = new
        self.set_groups()

    def __getattr__(self, name):
        return self._dict.get(name)

    def __getitem__(self, name):
        return self._dict[name]
    
    @property
    def dict(self):
        return self._dict
    
    def display(self, rows=3, exclude=[]):
        for k, v in self._dict.items():
            print(k, GroupedDF.groups[k], sep=': ')
            display(v.drop(columns=exclude).head(rows))
            print()