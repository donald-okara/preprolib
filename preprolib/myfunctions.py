
def cat_or_num(dataframe, ignore, numeric_columns, categorical_columns):
    """ This function appends a column to the appropriate datatype list. Ensure there is a list of columns numeric_columns and categorical_columns"""
    import numpy as np

    for col in dataframe.columns:
        if col in ignore:
            continue
        elif dataframe[col].dtype == float:
            try:
                numeric_columns.append(col)
            except NameError:
                print("The variable numeric_columns list is not present.")
                print("Please make sure it is present before using it.")
        elif np.issubdtype(dataframe[col].dtype, np.integer):
            try:
                numeric_columns.append(col)
            except NameError:
                print("The variable numeric_columns list is not present.")
                print("Please make sure it is present before using it.")
        elif dataframe[col].dtype == object:
            try:
                categorical_columns.append(col)
            except NameError:
                print("The variable categorical_columns list is not present.")
                print("Please make sure it is present before using it.")
