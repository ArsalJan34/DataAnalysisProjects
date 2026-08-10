# Module 2 — Python Data Analysis & EDA README

## 1. Importing Datasets with Python

Data can come from:

- CSV files
- Databases
- Other file formats
- Online sources

### Import CSV with Python

Use `open()` with a `with` statement:

```python
with open("file_path/file_name", "r") as data:
    # read file
```

### File Modes

| Mode | Purpose           |
| ---- | ----------------- |
| `r`  | Read              |
| `w`  | Write             |
| `a`  | Append            |
| `+`  | Create a new file |

For reading CSV files, the usual mode is **`r`**.

### Import CSV with Pandas

```python
import pandas as pd

df = pd.read_csv("file_path/file_name")
```

You can also import a CSV directly from a URL:

```python
df = pd.read_csv("https://example.com/data.csv")
```

---

# 2. Importing Data from Databases

Common databases include:

- BigQuery
- MySQL
- SQLite
- Oracle

Large datasets are often stored in databases because they may be too large to download and process locally.

Instead of downloading everything, use **SQL queries** to extract only the required rows and/or columns.

### BigQuery

BigQuery is Google's cloud data warehouse.

**BigQuery Sandbox** provides access to public datasets and, according to the course material:

- 10 GB active storage
- 1 TB processed query data per month

### Basic BigQuery Workflow

1. Access BigQuery.
2. Authenticate and create a project.
3. Find a dataset/table.
4. Open the table.
5. Select **Query**.
6. Write SQL.
7. Run the query.
8. Save the results.
9. Import the results into your notebook.

### BigQuery Notebooks

BigQuery can provide a Jupyter notebook environment on a virtual machine.

A virtual machine has its own:

- CPU
- Memory
- Software

but runs on shared server hardware.

This allows you to query large cloud datasets directly without downloading the entire dataset locally.

---

# 3. Discovering a Dataset with Pandas

After importing a dataset, first understand its structure before performing analysis.

## `df.head()`

Displays the first `n` rows.

```python
df.head()
```

Default:

```python
df.head(5)
```

Custom number:

```python
df.head(10)
```

**Use:** Quickly inspect the beginning of a dataset.

---

## `df.info()`

Provides a concise summary of the DataFrame.

```python
df.info()
```

Shows information such as:

- Number of entries
- Number of columns
- Column names
- Data types (`dtypes`)
- Non-null counts
- Memory usage

You can also use:

```python
df.info(show_counts=True)
```

to show non-null counts.

---

## `df.describe()`

Provides descriptive statistics.

```python
df.describe()
```

Common statistics include:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- 50th percentile (median)
- 75th percentile
- Maximum

You can control which data types are included:

```python
df.describe(include=[...])
df.describe(exclude=[...])
```

---

## `df.shape`

Returns the dimensions of the DataFrame as:

```text
(rows, columns)
```

Example:

```python
df.shape
```

Output:

```text
(3401012, 3)
```

**Important:** `shape` is an **attribute**, so it does not use parentheses.

### Dataset Discovery Quick Reference

```python
df.head()
df.info()
df.describe()
df.shape
```

These are foundational tools for beginning EDA.

---

# 4. Datetime Manipulation

Datetime data represents dates and times.

Python provides a standard `datetime` module, while NumPy and Pandas provide optimized datetime types for working with large datasets.

## Common Datetime Format Codes

| Code | Meaning                   | Example                 |
| ---- | ------------------------- | ----------------------- |
| `%a` | Abbreviated weekday       | Sun                     |
| `%A` | Full weekday              | Sunday                  |
| `%b` | Abbreviated month         | Jan                     |
| `%B` | Full month                | January                 |
| `%c` | Date and time             | Sun Jan 1 00:00:00 2021 |
| `%d` | Day                       | 01–31                   |
| `%H` | Hour, 24-hour format      | 00–23                   |
| `%I` | Hour, 12-hour format      | 01–12                   |
| `%j` | Day of year               | 001–366                 |
| `%m` | Month                     | 01–12                   |
| `%M` | Minute                    | 00–59                   |
| `%p` | AM/PM                     | AM/PM                   |
| `%S` | Seconds                   | 00–61                   |
| `%U` | Week number, Sunday start | 00–53                   |
| `%W` | Week number, Monday start | 00–53                   |
| `%w` | Weekday number            | 0–6                     |
| `%x` | Locale date               | 08/16/1988              |
| `%X` | Locale time               | 21:30:00                |
| `%y` | Year without century      | 00–99                   |
| `%Y` | Full year                 | 2022                    |
| `%z` | UTC offset                | +0900                   |
| `%Z` | Time zone                 | JST                     |

---

# 5. Python `datetime` Functions

Import:

```python
from datetime import datetime
```

## `datetime.strptime()`

Converts a string into a datetime object.

```python
dt = datetime.strptime("25/11/2022", "%d/%m/%Y")
```

**String → DateTime**

---

## `datetime.strftime()`

Converts a datetime object into a formatted string.

```python
dt.strftime("%d/%m/%Y")
```

**DateTime → String**

---

## `datetime.timestamp()`

Converts a datetime object into a timestamp in seconds.

```python
datetime.timestamp(dt)
```

**DateTime → Float timestamp**

---

## `datetime.fromtimestamp()`

Converts a timestamp into a datetime object.

```python
datetime.fromtimestamp(timestamp)
```

**Timestamp → DateTime**

---

## Convert Between Date Formats

```python
datetime.strptime(
    "25/11/2022",
    "%d/%m/%Y"
).strftime("%Y-%m-%d")
```

---

## Convert 24-Hour to 12-Hour Time

```python
datetime.strptime("20:00", "%H:%M").strftime("%I:%M %p")
```

Output:

```text
08:00 PM
```

## Convert 12-Hour to 24-Hour Time

```python
datetime.strptime("08:00 PM", "%I:%M %p").strftime("%H:%M")
```

Output:

```text
20:00
```

---

# 6. Time Zones

The course demonstrates timezone conversion using `pytz`.

```python
from pytz import timezone
```

Example:

```python
ny_time = datetime.strptime(
    "25-11-2022 09:34:00-0700",
    "%d-%m-%Y %H:%M:%S%z"
)

tokyo_time = ny_time.astimezone(timezone("Asia/Tokyo"))
```

This converts a datetime from one timezone to another.

---

# 7. Datetime in NumPy and Pandas

### NumPy Datetime Types

- `datetime64`
- `timedelta64`

### Pandas Datetime Types

- `Timestamp`
- `Timedelta`
- `Period`
- `DateOffset`

Pandas and NumPy datetime objects are efficient for large datasets because of their vectorization capabilities.

### Convert a Column to Datetime

```python
df["date"] = pd.to_datetime(df["date"])
```

`pd.to_datetime()` converts datetime-like strings into Pandas datetime data.

### Pandas `.dt` Accessor

When a Series contains datetime data, `.dt` allows access to datetime properties.

```python
df["date"].dt.year
df["date"].dt.month
df["date"].dt.day
```

**Important:** The Pandas `.dt` accessor is different from importing the Python `datetime` module using `dt` as an alias.

---

# 8. Structuring a Dataset with Pandas

Structuring involves organizing data so it can be efficiently analyzed.

Common operations include:

- Combining
- Selecting
- Filtering
- Sorting
- Slicing

---

## Combining Data

### `df.merge()`

Combines columns or indices from another DataFrame with the current DataFrame.

```python
df1.merge(df2)
```

Useful when combining related datasets using common columns/keys.

### `pd.concat()`

Combines Series and/or DataFrames along an axis.

```python
pd.concat([df1, df2])
```

Can combine:

- Rows
- Columns
- Multiple DataFrames

### `df.join()`

Combines columns from another DataFrame using an index or key column.

```python
df1.join(df2)
```

It can efficiently join multiple DataFrames by index.

---

# 9. Selecting Data

### Select Specific Columns

```python
df[["column1", "column2"]]
```

Returns only the selected columns.

### `df.select_dtypes()`

Selects columns based on their data types.

```python
df.select_dtypes(include=["int64"])
```

Can filter by types such as:

- `int64`
- `float64`
- `bool`
- `object`

---

# 10. Filtering Data

Boolean masks are used to filter rows.

```python
df[df["age"] > 18]
```

General form:

```python
df[condition]
```

The condition determines which rows are returned.

---

# 11. Sorting Data

### `df.sort_values()`

Sorts data according to selected columns.

```python
df.sort_values("column")
```

Descending order:

```python
df.sort_values("column", ascending=False)
```

---

# 12. Slicing Data

## `df.iloc[]`

Selects data using **integer/index positions**.

```python
df.iloc[5:10, 2:]
```

Selects:

- Rows 5 through 9
- Columns from position 2 onward

```python
df.iloc[5:10]
```

Selects rows 5 through 9 and all columns.

```python
df.iloc[1, 2]
```

Selects the value at row 1, column 2.

```python
df.iloc[[0, 2], [2, 4]]
```

Selects rows 0 and 2 and columns 2 and 4.

## `df.loc[]`

Selects data using **labels or Boolean conditions**.

```python
df.loc[condition]
```

### `iloc` vs `loc`

| Method   | Selection                   |
| -------- | --------------------------- |
| `iloc[]` | Integer positions           |
| `loc[]`  | Labels / Boolean conditions |

---

# 13. Histograms

## What is a Histogram?

A histogram is a graphical representation of a **frequency distribution**.

- X-axis → ranges/bins of values
- Y-axis → frequency/count
- Bar height → number of observations in that range

### Histograms Help Identify

- Distribution shape
- Center
- Spread
- Patterns
- Trends
- Potential outliers

They can also help with:

- Choosing statistical tests
- Understanding model assumptions
- Selecting appropriate models

---

# 14. Common Histogram Distributions

## Symmetric / Normal

- Bell-shaped distribution
- Data is distributed around the center
- Also called a **normal/Gaussian distribution**

## Right-Skewed

- Longer tail on the right
- More observations are concentrated toward the left

## Left-Skewed

- Longer tail on the left
- More observations are concentrated toward the right

## Bimodal

- Two distinct peaks
- Indicates two modes

## Uniform

- Relatively flat distribution
- Values are evenly distributed

### Center and Spread

**Center** can be represented by:

- Mean
- Median

**Spread** can be represented by:

- Standard deviation
- Range

---

# 15. Creating Histograms with Matplotlib

```python
import matplotlib.pyplot as plt

plt.hist(df["seconds"], bins=10)

plt.xlabel("seconds")
plt.ylabel("count")
plt.title("Histogram")
plt.show()
```

### Important `plt.hist()` Parameters

- `x` → data to plot
- `bins` → number or boundaries of bins

Example:

```python
plt.hist(df["seconds"], bins=range(40, 101, 5))
```

---

# 16. Creating Histograms with Seaborn

```python
import seaborn as sns

sns.histplot(
    x=df["seconds"],
    binrange=(40, 100),
    binwidth=5
)

plt.show()
```

### Important `sns.histplot()` Parameters

- `x` → data sequence
- `bins` → number/bin boundaries
- `binrange` → lowest and highest bin edges
- `binwidth` → width of each bin

---

# 17. Module 2 Glossary

### Box Plot

A visualization showing the locality, spread, and skew of groups of values within quartiles.

### CSV File

A simple text file commonly used to store and import tabular data.

### Database (DB) File

A file/system used to store data in structures such as tables, indexes, or fields.

### Data Source

The location where data originates.

### Extracting

Retrieving data from a data source for further processing or storage.

### Filtering

Selecting a smaller part of a dataset based on specified conditions.

### First-Party Data

Data gathered from within your own organization.

### Grouping

Aggregating individual observations into groups.

### Hypothesis

A theory or explanation based on evidence that has not yet been refuted.

### `info()`

A Pandas method that provides information about entries and data types.

### `Int64`

A standard integer data type.

### JSON File

A data storage format based on JavaScript Object Notation.

### Merging

Combining DataFrames using specified column(s) or keys.

### Second-Party Data

Data gathered outside your organization directly from the original source.

### Slicing

Breaking data into smaller sections for examination and analysis.

### Sorting

Arranging data into a meaningful order.

### String

A sequence of characters and punctuation representing textual information.

### Third-Party Data

Data gathered outside your organization and aggregated.

---

# 18. EDA & Data Concepts

### Bias

In data structuring, organizing results into groups, categories, or variables that misrepresent the dataset as a whole.

### Cleaning

Removing errors that may distort data or make it less useful.

### Data Visualization

A graph, chart, diagram, or dashboard representing information.

### Discovering

Familiarizing yourself with a dataset to understand how it can be used.

### Exploratory Data Analysis (EDA)

The process of investigating, organizing, and analyzing datasets while summarizing their main characteristics.

The six main EDA practices are:

1. **Discovering**
2. **Structuring**
3. **Cleaning**
4. **Joining**
5. **Validating**
6. **Presenting**

### Joining

Augmenting data by adding values from other datasets.

### PACE

A workflow used to stay focused on the end goal of a dataset:

- **P** = Plan
- **A** = Analyze
- **C** = Construct
- **E** = Execute

### Presenting

Making a cleaned dataset available to others for analysis or further modeling.

### Structuring

Organizing or transforming raw data so it can be more easily visualized, explained, or modeled.

### Validating

Verifying that data is consistent and high quality.

---

# 19. Module 2 Quick Reference

```python
# Import
import pandas as pd
df = pd.read_csv("data.csv")

# Discover
df.head()
df.info()
df.describe()
df.shape

# Datetime
df["date"] = pd.to_datetime(df["date"])
df["date"].dt.year
df["date"].dt.month
df["date"].dt.day

# Combine
df1.merge(df2)
pd.concat([df1, df2])
df1.join(df2)

# Select
df[["col1", "col2"]]
df.select_dtypes(include=["int64"])

# Filter
df[df["column"] > value]

# Sort
df.sort_values("column")
df.sort_values("column", ascending=False)

# Slice
df.iloc[5:10]
df.iloc[1, 2]
df.loc[condition]

# Histogram
plt.hist(df["column"], bins=10)
sns.histplot(x=df["column"])
```

## Core Module 2 Workflow

**Import → Discover → Structure → Visualize → Analyze**

- Import the dataset.
- Inspect its structure using `head()`, `info()`, `describe()`, and `shape`.
- Structure the data using selection, filtering, sorting, slicing, and combining.
- Convert and manipulate datetime data when necessary.
- Use histograms to understand distributions.
- Continue with the remaining EDA practices: cleaning, joining, validating, and presenting.
