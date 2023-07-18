# preprolib

This is a Python library for preprocessing functions.

## How to Install

Install the library using pip:

1. Open a command prompt or terminal.
2. Use the following command to install the library directly from GitHub using pip:

```
pip install git+https://github.com/donald-okara/preprolib.git
```

3. Import and Use the Library in Your Code:

In your Python script or notebook, import the library or specific modules/functions as needed.

Use the imported functions or modules from your library in your code as you would with any other library.

```python
import preprolib.myfunction
```

## Available Functions

### 1. cat_or_num()

Function Signature:
```python
def cat_or_num(dataframe, ignore, numeric_columns, categorical_columns):
```

**Expected Parameters:**
- `dataframe`: This parameter represents the input pandas DataFrame that contains the data to be processed. It is expected that the input DataFrame has columns with different data types, including numerical and categorical data.
- `ignore`: This parameter is a list of column names that should be ignored during processing. These columns will not be considered for appending to the `numeric_columns` and `categorical_columns` lists.
- `numeric_columns`: This parameter is an empty list that will be populated with the names of columns containing numerical data found in the `dataframe`.
- `categorical_columns`: This parameter is another empty list that will be populated with the names of columns containing categorical data found in the `dataframe`.

**Function Description:**
The purpose of the `cat_or_num()` function is to examine each column in the input DataFrame (`dataframe`) and identify whether it contains numerical or categorical data. It then appends the column names to the appropriate list, `numeric_columns` for numerical data, and `categorical_columns` for categorical data.

The function performs the following steps:

1. Iterates over each column in the DataFrame (`dataframe`).
2. Checks if the column name is in the list of columns to ignore (`ignore`). If it is, the column is skipped, and the function moves on to the next column.
3. For each column, it checks the data type:
   - If the data type is `float`, the column is considered numerical, and its name is appended to the `numeric_columns` list.
   - If the data type is a sub-datatype of `integer`, the column is also considered numerical, and its name is appended to the `numeric_columns` list.
   - If the data type is `object`, the column is considered categorical, and its name is appended to the `categorical_columns` list.
4. If any of the lists `numeric_columns` or `categorical_columns` do not exist (due to a potential `NameError`), the function handles the error by printing an appropriate message indicating that the corresponding list is not present.

**Usage Example:**
```python
import pandas as pd
from preprolib import myfunctions

# Sample DataFrame
data = {
    'Age': [30, 25, 35],
    'Gender': ['Male', 'Female', 'Male'],
    'Income': [50000, 60000, 45000],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

num_cols = []
cat_cols = []

ignore_list = ['City']

myfunctions.cat_or_num(df, ignore_list, num_cols, cat_cols)

print("Numerical Columns:", num_cols)
print("Categorical Columns:", cat_cols)
```

**Output:**
```
Numerical Columns: ['Age', 'Income']
Categorical Columns: ['Gender']
```

In this example, the `cat_or_num()` function is used to identify numerical and categorical columns in the DataFrame `df`. The output shows that the `Age` and `Income` columns are identified as numerical, while the `Gender` column is identified as categorical. The `City` column is ignored as specified in the `ignore_list`.

## Contributing

Contributions to preprolib are welcome! For bug reports, feature requests, or questions, open an issue or submit a pull request. See [Contribution Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or inquiries, reach out to us at contact@example.com or visit our website at https://example.com.

