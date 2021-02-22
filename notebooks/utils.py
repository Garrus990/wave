import numpy as np

def merge_small_groups(data, col, threshold=200):
    df = data.copy()
    vc = df[col].value_counts()
    small_groups = vc.loc[vc <= threshold].index
    df[col] = df[col].replace(small_groups, 'OTH')
    return df

def replace_rare_values(data, cols, replace_value=np.nan, threshold=200):
    df = data.copy()
    for col in cols:
        if col not in df.columns:
            warnings.warn(f'Column {col} is not among the columns of the data frame `data`.')
            continue
        vc = df[col].value_counts()
        small_groups = vc.loc[vc <= threshold].index
        df[col] = df[col].replace(small_groups, replace_value)
    return df
