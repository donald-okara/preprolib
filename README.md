# preprolib

This is a python library for preprocessing functions.

#### How to install

Install the library using pip:

Open a command prompt or terminal.

```bash
pip install git+https://github.com/donald-okara/preprolib.git
```

2. Import and use the library in your code:

In your Python script or notebook, import the library or specific modules/functions as needed.

Use the imported functions or modules from your library in your code as you would with any other library.

```python
import preprolib.myfunctions
```

##### Use functions from the library

```python
# Example: Data Preprocessing
cat_cols = []
num_cols = []
ignore_list = ['City']

myfunctions.cat_or_num(df, ignore_list, num_cols, cat_cols)
```

```python
# Example: Model Evaluation
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier()
rf_model.fit(X_train_transformed, y_train)

myfunctions.evaluate_model(rf_model, X_test_transformed, y_test)
```

### Function Documentation

The preprolib library provides the following functions for data preprocessing and model evaluation:

1. `cat_or_num(dataframe, ignore, numeric_columns, categorical_columns)`: This function identifies numerical and categorical columns in the input DataFrame and appends them to the corresponding lists.

   - `dataframe`: Input pandas DataFrame containing the data to be processed.
   - `ignore`: List of column names to ignore during processing.
   - `numeric_columns`: Empty list to store the names of columns containing numerical data.
   - `categorical_columns`: Empty list to store the names of columns containing categorical data.

2. `evaluate_model(model, X_test, y_test)`: This function evaluates a trained machine learning model on the test dataset.

   - `model`: Trained machine learning model to be evaluated.
   - `X_test`: Test features.
   - `y_test`: Test labels.

3. `other_function()`: This function provides an example of another function that could be added to the library.

### Contribution Guidelines

Please check the [Contribution Guidelines](Guidelines.md) for instructions on how to contribute to the development of preprolib.

## License

The preprolib library is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

Thank you for using preprolib! We hope this library simplifies your data preprocessing tasks and enhances your data analysis and machine learning projects. If you have any questions or need further assistance, feel free to reach out to the project maintainers. Happy preprocessing!
