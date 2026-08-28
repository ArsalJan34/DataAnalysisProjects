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

# Explore Descriptive Statistics with Pandas & NumPy

## 1. Descriptive Statistics

- Descriptive statistics summarize the **location, center, and spread** of data.
- Common statistics: **mean, median, minimum, maximum, standard deviation, and percentiles**.
- `pandas` and `numpy` provide functions to calculate these statistics.

## 2. Import Libraries & Load Data

```python
import pandas as pd
import numpy as np

epa_data = pd.read_csv("c4_epa_air_quality.csv", index_col=0)
```

- `index_col=0` uses the first CSV column as the DataFrame index and prevents an unwanted `Unnamed: 0` column.

## 3. Explore the Dataset with `head()`

```python
epa_data.head(10)
```

- Displays the first 10 rows.
- `head(n)` displays the first `n` rows.
- `aqi` = **Air Quality Index**, used to represent air quality.

## 4. `describe()` for Numerical Data

```python
epa_data.describe()
```

- Generates descriptive statistics for numeric columns.

### Main Statistics

| Statistic | Meaning                      |
| --------- | ---------------------------- |
| `count`   | Number of non-missing values |
| `mean`    | Average                      |
| `std`     | Standard deviation           |
| `min`     | Minimum                      |
| `25%`     | 25th percentile              |
| `50%`     | Median                       |
| `75%`     | 75th percentile              |
| `max`     | Maximum                      |

### AQI Results

- `count = 260` → 260 AQI measurements.
- `mean ≈ 6.76` → average AQI is about 6.76.
- `25% = 2` → 25% of AQI values are below 2.
- `50% = 5` → median AQI is 5.
- `75% = 9` → 75% of AQI values are below 9.
- `min = 0` → lowest observed AQI.
- `max = 50` → highest observed AQI.
- `std ≈ 7.06` → measures how spread out AQI values are.

## 5. `describe()` for Categorical Data

```python
epa_data["state_name"].describe()
```

### Results

| Statistic | Meaning                     |
| --------- | --------------------------- |
| `count`   | 260 state entries           |
| `unique`  | 52 unique states            |
| `top`     | California                  |
| `freq`    | California appears 66 times |

- `top` represents the **mode** (most common category).
- `freq` represents how often the mode occurs.

## 6. NumPy Statistical Functions

### Mean

```python
np.mean(epa_data["aqi"])
```

- Result ≈ **6.76**
- Represents the average AQI.

### Median

```python
np.median(epa_data["aqi"])
```

- Result = **5.0**
- Half of the AQI values are below 5 and half are above it.

### Minimum

```python
np.min(epa_data["aqi"])
```

- Result = **0**
- Lowest observed AQI.

### Maximum

```python
np.max(epa_data["aqi"])
```

- Result = **50**
- Highest observed AQI.

### Standard Deviation

```python
np.std(epa_data["aqi"], ddof=1)
```

- Result ≈ **7.06**
- Measures the spread/variability of AQI values.

## 7. NumPy vs Pandas Standard Deviation

- NumPy's default: `ddof=0`
- Pandas' default: `ddof=1`
- To calculate the sample standard deviation with NumPy and match pandas:

```python
np.std(epa_data["aqi"], ddof=1)
```

## 8. Percentiles

- **25th percentile (Q1):** 25% of values are below this point.
- **50th percentile (Q2):** Median; 50% of values are below this point.
- **75th percentile (Q3):** 75% of values are below this point.
- Percentiles help understand the **distribution and location** of values.

## 9. AQI Findings

- Average AQI ≈ **6.76**.
- 75% of AQI values are **below 9**.
- Maximum AQI in the dataset is **50**.
- The observed AQI values are well below the general AQI level of 100 that is considered satisfactory.
- Further investigation can focus on regions with relatively higher AQI values to identify ways to improve air quality.

## 10. Key Takeaways

- Use `pandas` `describe()` for a quick summary of numerical or categorical data.
- Use NumPy functions when individual statistics are needed:

```python
np.mean()
np.median()
np.min()
np.max()
np.std()
```

- `describe()` is useful for quickly understanding a dataset before deeper analysis.
- Mean describes the **average**, median describes the **central position**, and standard deviation describes **spread**.

---

# Course 3 — Module 1: Statistics Terms & Definitions

## 1. Statistics & Statistical Concepts

- **Statistics:** Study of the collection, analysis, and interpretation of data.
- **Descriptive Statistics:** Summarizes the main features of a dataset.
- **Inferential Statistics:** Uses sample data to draw conclusions about a larger population.
- **Summary Statistics:** Summarizes data using a single number.
- **Statistic:** A characteristic of a sample.
- **Parameter:** A characteristic of a population.

## 2. Population & Sampling

- **Population:** Every possible element a data professional is interested in measuring.
- **Sample:** A subset of a population.
- **Sampling:** Process of selecting a subset of data from a population.
- **Representative Sample:** A sample that accurately reflects the characteristics of a population.

## 3. Measures of Central Tendency

- **Measure of Central Tendency:** A value representing the center of a dataset.
- **Mean:** Average value of a dataset.
- **Median:** Middle value in a dataset.
- **Mode:** Most frequently occurring value in a dataset.

## 4. Measures of Dispersion

- **Measure of Dispersion:** Describes the spread or variation of data points.
- **Range:** Difference between the largest and smallest value.
  - `Range = Maximum − Minimum`

- **Variance:** Average of the squared differences between each data point and the mean.
- **Standard Deviation:** Measures the typical distance of data points from the mean.
- **Interquartile Range (IQR):** Distance between the first and third quartiles.
  - `IQR = Q3 − Q1`

## 5. Measures of Position

- **Measure of Position:** Determines the position of a value relative to other values in a dataset.
- **Percentile:** Value below which a specified percentage of data falls.
- **Quartile:** A value that divides a dataset into four equal parts.

## 6. Statistical Testing

- **A/B Testing:** Compares two versions of something to determine which performs better.
- **Confidence Interval:** A range of values describing the uncertainty surrounding an estimate.
- **Statistical Significance:** Indicates that test or experiment results are unlikely to be explained by chance alone.

## 7. Other Key Terms

- **Econometrics:** Branch of economics that uses statistics to analyze economic problems.
- **Literacy Rate:** Percentage of a population in a given age group that can read and write.
