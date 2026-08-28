# Descriptive Statistics with Python

## 1. Exploratory Data Analysis (EDA)

- EDA process: **Discover → Clean → Analyze → Present** data.
- First understand the dataset context through documentation and stakeholders.
- Clean data by handling **missing values, incorrect values, and irrelevant data**.
- Descriptive statistics are commonly calculated after data cleaning to summarize the dataset.

## 2. Import Libraries and Load Dataset

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

education_districtwise = pd.read_csv('education_districtwise.csv')
```

## 3. Explore Dataset with `head()`

- `head()` displays the first rows of a DataFrame.

```python
education_districtwise.head(10)
```

- `head(n)` returns the first `n` rows.
- Each row in this dataset represents a **district**.

## 4. `describe()` for Numerical Data

- `describe()` calculates multiple descriptive statistics at once.

```python
education_districtwise['OVERALL_LI'].describe()
```

### Output Statistics

| Statistic | Meaning                            |
| --------- | ---------------------------------- |
| `count`   | Number of non-missing observations |
| `mean`    | Arithmetic average                 |
| `std`     | Standard deviation                 |
| `min`     | Smallest value                     |
| `25%`     | First quartile (25th percentile)   |
| `50%`     | Median (50th percentile)           |
| `75%`     | Third quartile (75th percentile)   |
| `max`     | Largest value                      |

### Example

- Mean literacy rate ≈ **73.4%**
- Median ≈ **73.49%**
- Minimum ≈ **37.22%**
- Maximum ≈ **98.76%**
- `describe()` excludes missing (`NaN`) values.
- If the dataset has 680 rows but `count = 634`, then **46 literacy-rate values are missing**.

## 5. `describe()` for Categorical Data

```python
education_districtwise['STATNAME'].describe()
```

### Output Statistics

| Statistic | Meaning                                |
| --------- | -------------------------------------- |
| `count`   | Number of non-missing observations     |
| `unique`  | Number of unique categories            |
| `top`     | Most frequently occurring value (mode) |
| `freq`    | Frequency of the most common value     |

### Example

- `unique = 36` → 36 different states.
- `top = STATE21` → most common state.
- `freq = 75` → `STATE21` appears in 75 rows/districts.

## 6. Individual Statistical Functions

Python provides separate functions for common descriptive statistics:

```python
column.mean()
column.median()
column.std()
column.min()
column.max()
```

- `mean()` → average
- `median()` → middle value
- `std()` → standard deviation
- `min()` → smallest value
- `max()` → largest value

These functions are useful when individual statistics are needed for further calculations.

## 7. Calculate Range

- **Range = Maximum − Minimum**
- Use `max()` and `min()`:

```python
range_overall_li = (
    education_districtwise['OVERALL_LI'].max()
    - education_districtwise['OVERALL_LI'].min()
)

range_overall_li
```

- Literacy-rate range ≈ **61.54 percentage points**.
- A large range indicates substantial variation between districts.

## 8. Key Takeaways

- `describe()` provides a quick statistical summary.
- Numerical data returns **count, mean, std, min, quartiles, and max**.
- Categorical data returns **count, unique, top, and frequency**.
- Missing values (`NaN`) are excluded from `describe()` calculations.
- Individual functions such as `mean()`, `median()`, `min()`, and `max()` allow specific calculations.
- Range measures the difference between the highest and lowest values.

---
