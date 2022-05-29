
global INDEX

if not "INDEX" in globals():
    INDEX = ['year', 'county']



def cols(df) -> None:
    print(*[c for c in df.columns if c not in INDEX], sep='\n')

def merge(df1, df2) -> pd.DataFrame:
    return df1.merge(df2, how='inner', on=INDEX)

def match_rename(df, text, replacement) -> pd.DataFrame:
    for c in df.columns:
        if c != text:
            df = df.rename(columns={c: c.replace(text, replacement)})
    return df


def insert(df, name, target, col:pd.Series) -> pd.DataFrame:
    """ Like df.insert(), but takes a column name as location, instead of int """
    idx = list(df.columns).index(target)
    df.insert(idx, name, col)
    return df


def move_col(df, name, target) -> pd.DataFrame:
    """ Move named col to right before target col """
    col = df.pop(name)
    idx = list(df.columns).index(target)
    df.insert(idx, name, col)
    return df


def separate_by(df, to_match, keys=INDEX, keep=[], start=False, end=False, mode="") -> (pd.DataFrame, pd.DataFrame):
    """
    Given a df and a substring, return two dfs:
    1. df containing: county + all columns whose name does NOT contain substring
    2. df containing: county + all columns whose name DOES contain substring
    """
    if type(to_match) != list:
        to_match = [to_match]

    names = [item for sublist in [[c for c in df.columns if (
            c.startswith(txt) if start else c.endswith(txt) if end else txt in c
        )] for txt in to_match] for item in sublist]

    include = df.copy()[keys + keep + names]
    exclude = df.copy().drop(columns = keep + names)
    return include if mode == 'include' else exclude if mode == 'exclude' else (include, exclude)


def head(df, n=3, name=None):
    if name:
        print(name.upper())
    print("COLUMNS: ", df.shape[1], '\n', 'ROWS:    ', df.shape[0], sep="")
    display(df.head(n))


def extract_group(df, prefix, keys=INDEX, keep=[], keep_first_word=False) -> pd.DataFrame:
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
            remove = f'{"_".join(p.split("_")[1:])}'
        for c in result.columns:
            if c.startswith(p):
                result = result.rename(columns={c: c.replace(remove, '')})
    return result