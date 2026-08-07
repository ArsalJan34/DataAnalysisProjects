# Data Analysis Reference Notes

This README serves as a consolidated reference repository for Python data analysis concepts, functions, and workflows.

---

## Reference Guide: Pandas Tools for Structuring Datasets

This section outlines essential Pandas methods and functions used to combine, extract, filter, sort, and slice DataFrames during data preprocessing and analysis.

### 1. Combining Data

Pandas provides multiple approaches to merge and concatenate datasets depending on structure and joining requirements.

- **`df.merge()`**
  - **Description:** A DataFrame method used to combine columns or indices from another DataFrame based on common key columns or index values (similar to SQL joins).
  - **Syntax / Example:**
    ```python
    df1.merge(df2, how='inner', on=['month', 'year'])
    ```

- **`pd.concat()`**
  - **Description:** A top-level Pandas function used to join Series or DataFrames along a specific axis (`axis=0` for rows, `axis=1` for columns).
  - **Syntax / Example:**
    ```python
    df3 = pd.concat([df1.drop(['column_1', 'column_2'], axis=1), df2])
    ```

- **`df.join()`**
  - **Description:** A DataFrame method optimized for combining columns with another DataFrame on an index or key column. Efficiently joins multiple DataFrames by index at once.
  - **Syntax / Example:**
    ```python
    df1.set_index('key').join(df2.set_index('key'))
    ```

---

### 2. Extracting and Selecting Data

- **`df[[columns]]`**
  - **Description:** Selects a specific subset of columns from a DataFrame by passing a list of column names.
  - **Syntax / Example:**
    ```python
    df[['animal', 'legs']]
    ```

- **`df.select_dtypes()`**
  - **Description:** Returns a subset of columns based on their data types (e.g., `int64`, `float64`, `object`, `bool`).
  - **Syntax / Example:**
    ```python
    df.select_dtypes(include=['int64'])
    ```

---

### 3. Filtering Data

- **`df[condition]`**
  - **Description:** Applies a Boolean mask to filter DataFrame rows according to specific conditional evaluations.
  - **Syntax / Example:**
    ```python
    df[df['class'] == 'Aves']
    ```

---

### 4. Sorting Data

- **`df.sort_values()`**
  - **Description:** Sorts DataFrame rows based on the values in one or more specified columns.
  - **Syntax / Example:**
    ```python
    df.sort_values(by=['legs'], ascending=False)
    ```

---

### 5. Slicing Data

- **`df.iloc[]`**
  - **Description:** Purely integer-location based indexing for selection by position.
  - **Syntax / Examples:**
    ```python
    df.iloc[5:10, 2:]        # Rows 5 through 9, columns index 2 and above
    df.iloc           # Rows 5 through 9, all columns
    df.iloc[1, 2]           # Single value at row 1, column 2
    df.iloc[[0, 2], [2, 4]] # Rows 0 and 2 at column indices 2 and 4
    ```

- **`df.loc[]`**
  - **Description:** Accesses a group of rows and columns by label(s) or a Boolean array.
  - **Syntax / Example:**
    ```python
    df.loc[:, ['color', 'class']]
    ```

---

_Note: Additional notes and reference material will be appended here in subsequent updates._
