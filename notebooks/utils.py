import numpy as np


def merge_small_groups(data, col, other_group_name='OTH', threshold=200):
    """The function merges small group in a data frame's column
    (a small group consists of less than `threshold` observations)
    into a single group called 'OTH' (other).
    
    Parameters
    ----------
    data : pd.DataFrame instance
        Data frame with the column to merge.
    col : str
        The name of the column where infrequent groups will be merged.
    other_group_name: str, default='OTH'
        The name of the group that will be built from the small groups
        in the column `col`.
    threshold : int, default=200
        A group will be deemed infrequent (small) and, consequently, 
        merged if its count in the column is less than `threshold`.
    
    Returns
    -------
    a data frame of the same structure as `data`, but with column
    `col` replaced with its counterpart where small groups are merged
    """
    df = data.copy()
    vc = df[col].value_counts()
    small_groups = vc.loc[vc <= threshold].index
    df[col] = df[col].replace(small_groups, other_group_name)
    return df


def replace_rare_values(data, cols, replace_value=np.nan, threshold=200):
    """The function is used to replace all rare values (values whose count
    is lower than `threshold`) in columns specified in `cols`. The values
    are replaced with `replace_value`.
    
    Parameters
    ----------
    data : pd.DataFrame instance
        Data frame with the columns where values will be replaced.
    cols : iterable
        Columns of `data` where rare values will be replaced. If a column
        in `cols` is not present in the data frame, a warning is raised.
    replace_value: {str, numeric, np.nan}, default=np.nan
        A scalar value that will replace rare values in the columns `cols`.
    threshold : int, default=200
        A value is deemed rare if its count in the column is less than
        `threshold`.
    
    Returns
    -------
    a data frame of the same structure as `data`, but in every column
    in `cols` rare values are replaced with `replace_value`
    """
    df = data.copy()
    for col in cols:
        if col not in df.columns:
            warnings.warn(f'Column {col} is not among the columns of the data frame `data`.')
            continue
        vc = df[col].value_counts()
        small_groups = vc.loc[vc <= threshold].index
        df[col] = df[col].replace(small_groups, replace_value)
    return df
