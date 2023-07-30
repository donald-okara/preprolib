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


def evaluate_model(curr_model, X_test, y_test):
    import pandas as pd
    from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

    predictions = curr_model.predict(X_test)
    # Convert the one-hot encoded y_test to a 1-dimensional array
    y_test_1d = y_test.argmax(axis=1)

    # Calculate the necessary metrics
    accuracy = accuracy_score(y_test_1d, predictions)
    precision = precision_score(y_test_1d, predictions, average='weighted')
    recall = recall_score(y_test_1d, predictions, average='weighted')
    f1 = f1_score(y_test_1d, predictions, average='weighted')

    # Print the evaluation metrics
    print("Model Evaluation:")
    print("Accuracy:", accuracy)
    print("Precision:", precision)
    print("Recall:", recall)
    print("F1-score:", f1)


