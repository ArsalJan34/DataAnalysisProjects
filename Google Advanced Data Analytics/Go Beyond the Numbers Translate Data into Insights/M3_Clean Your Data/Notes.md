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

## Reference Guide: Histograms and Frequency Distributions

This section covers the fundamentals of histograms, their role in exploratory data analysis (EDA), interpretation of common distribution shapes, and implementation using Matplotlib and Seaborn.

---

### 1. Overview and Importance

- **Histogram:** A graphical representation of a frequency distribution showing how often values in a continuous dataset or variable occur within specified intervals (bins).
- **Role in EDA:** Helps data professionals identify data shapes, central tendencies, variability, and potential outliers.
- **Downstream Impact:** Influences critical analytical decisions, such as selecting statistical tests, checking model assumptions, and designing experiments.

---

### 2. Interpreting Histogram Distributions

Evaluating histograms requires examining shape, center (mean/median), and spread (standard deviation/range).

- **Symmetric (Normal / Gaussian):** Bell-shaped curve centered in the middle; data is evenly distributed around the mean.
- **Right-Skewed (Positive Skew):** Longer tail extends to the right; majority of data points are concentrated on the left.
- **Left-Skewed (Negative Skew):** Longer tail extends to the left; majority of data points are concentrated on the right.
- **Bimodal:** Features two distinct peaks, indicating two different modes within the dataset.
- **Uniform:** Flat distribution across all ranges, indicating equal frequency for all bin intervals.

---

### 3. Creating Histograms in Python

#### Matplotlib: `plt.hist()`

Generates histograms using the `pyplot` interface.

- **Key Parameters:**
  - `x`: Input data sequence (list, Series, array).
  - `bins`: Number of bins (int), sequence of bin edges, or string rule.
- **Syntax / Example:**

  ```python
  import matplotlib.pyplot as plt

  plt.hist(df['seconds'], bins=range(40, 101, 5))
  plt.title('Old Faithful Geyser - Time Between Eruptions')
  plt.xlabel('Seconds')
  plt.ylabel('Count')
  plt.show()
  ```

  ***

## Reference Guide: Data Analysis Glossary (Course 2, Module 2)

This section provides a structured reference glossary covering core data types, file formats, exploratory data analysis (EDA) practices, and dataset operations.

---

### 1. Data File Formats & Sources

- **CSV File:** A simple text file format used to store tabular data, easily imported or stored across databases and platforms.
- **Database (DB) File:** A structured file used to store relational data in tables, indexes, and fields.
- **JSON File:** A lightweight data-interchange storage file format saved in JavaScript Object Notation format.
- **Data Source:** The origin location from which data is extracted.
- **First-Party Data:** Data collected directly from within your own organization.
- **Second-Party Data:** Data collected outside your organization directly from the primary source that gathered it.
- **Third-Party Data:** Data collected and aggregated by outside entities from multiple external sources.

---

### 2. Core Exploratory Data Analysis (EDA) Practices

Exploratory Data Analysis (EDA) involves investigating, organizing, and summarizing datasets to uncover key characteristics. The workflow relies on six primary practices:

1. **Discovering:** Familiarizing yourself with the dataset to conceptualize how to analyze and leverage it.
2. **Structuring:** Organizing and transforming raw data into structured formats to facilitate visualization and modeling.
3. **Cleaning:** Removing errors, missing values, duplicates, and inconsistencies that distort analysis.
4. **Joining:** Augmenting datasets by combining and integrating values from external or related datasets.
5. **Validating:** Verifying that the processed data is consistent, accurate, and high quality.
6. **Presenting:** Sharing the cleaned and structured dataset or visual findings with stakeholders for decision-making.

---

### 3. Key Concepts & Frameworks

- **Box Plot:** A graphical visualization displaying data locality, spread, and skewness across quartiles.
- **Bias:** In data structuring, organizing data into groups or categories that misrepresent the true nature of the entire dataset.
- **Data Visualization:** Any graphical representation (chart, graph, diagram, dashboard) created to communicate data insights.
- **Hypothesis:** A testable theory or explanation based on initial evidence that has not yet been refuted.
- **PACE Framework:** A structured data project workflow standing for **Plan, Analyze, Construct, and Execute**.

---

### 4. Technical Methods & Data Types

- **`df.info()`:** A Pandas method that displays total entries, non-null counts, and data types (`dtypes`) across DataFrame columns.
- **Extracting:** Retrieving data from primary or secondary data sources for processing.
- **Filtering:** Selecting a subset of a dataset based on specified conditional constraints.
- **Grouping:** Aggregating individual observation records based on common categorical values.
- **Int64:** A standard integer data type representing numbers between $-9 \times 10^{18}$ and $+9 \times 10^{18}$.
- **Merging:** Combining two or more DataFrames along specified key column(s) or indices.
- **Slicing:** Subsetting information into smaller portions by positions or labels for detailed examination.
- **Sorting:** Arranging data rows in a specific numerical or alphabetical order.
- **String:** A character sequence used to represent textual information.

---

_Note: Additional notes and reference material will be appended here in subsequent updates._

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

## Reference Guide: Histograms and Frequency Distributions

This section covers the fundamentals of histograms, their role in exploratory data analysis (EDA), interpretation of common distribution shapes, and implementation using Matplotlib and Seaborn.

### 1. Overview and Importance

- **Histogram:** A graphical representation of a frequency distribution showing how often values in a continuous dataset or variable occur within specified intervals (bins).
- **Role in EDA:** Helps data professionals identify data shapes, central tendencies, variability, and potential outliers.
- **Downstream Impact:** Influences critical analytical decisions, such as selecting statistical tests, checking model assumptions, and designing experiments.

---

### 2. Interpreting Histogram Distributions

Evaluating histograms requires examining shape, center (mean/median), and spread (standard deviation/range).

- **Symmetric (Normal / Gaussian):** Bell-shaped curve centered in the middle; data is evenly distributed around the mean.
- **Right-Skewed (Positive Skew):** Longer tail extends to the right; majority of data points are concentrated on the left.
- **Left-Skewed (Negative Skew):** Longer tail extends to the left; majority of data points are concentrated on the right.
- **Bimodal:** Features two distinct peaks, indicating two different modes within the dataset.
- **Uniform:** Flat distribution across all ranges, indicating equal frequency for all bin intervals.

---

### 3. Creating Histograms in Python

#### Matplotlib: `plt.hist()`

Generates histograms using the `pyplot` interface.

- **Key Parameters:**
  - `x`: Input data sequence (list, Series, array).
  - `bins`: Number of bins (int), sequence of bin edges, or string rule.
- **Syntax / Example:**

  ```python
  import matplotlib.pyplot as plt

  plt.hist(df['seconds'], bins=range(40, 101, 5))
  plt.title('Old Faithful Geyser - Time Between Eruptions')
  plt.xlabel('Seconds')
  plt.ylabel('Count')
  plt.show()
  ```
