# Module 2 — Measures of Central Tendency

## 1. Measures of Central Tendency

Measures of central tendency describe the **center of a dataset**.

The three main measures are:

- **Mean** → Average value
- **Median** → Middle value
- **Mode** → Most frequently occurring value

---

# 2. Mean

The **mean** is the average value of a dataset.

### Formula

**Mean = Sum of all values ÷ Number of values**

Example:

```text
10, 5, 3, 50, 12

Mean = (10 + 5 + 3 + 50 + 12) ÷ 5
     = 80 ÷ 5
     = 16
```

**Mean = 16**

### Important

The mean is **sensitive to outliers**. An unusually large or small value can significantly change the mean.

---

# 3. Median

The **median** is the middle value of a dataset.

### Steps

1. Arrange values from smallest to largest.
2. Find the middle value.

Example:

```text
3, 5, 10, 12, 50
```

**Median = 10**

### Even Number of Values

If there is an even number of values:

1. Arrange the values in order.
2. Find the two middle values.
3. Calculate their average.

Example:

```text
3, 5, 8, 10, 12, 50

Median = (8 + 10) ÷ 2
       = 9
```

**Median = 9**

### Important

When outliers are present, the **median is usually a better measure of the center** because it is less affected by extreme values.

---

# 4. Mode

The **mode** is the value that occurs most frequently.

A dataset can have:

- **No mode** → No value repeats
- **One mode** → One value occurs most frequently
- **Multiple modes** → More than one value occurs most frequently

Examples:

```text
1, 12, 33, 54, 75
→ No mode

2, 7, 7, 11, 20
→ Mode = 7

3, 12, 12, 40, 40
→ Modes = 12 and 40
```

---

# 5. Mean vs Median

Both describe the center of a dataset, but the best choice depends on the data.

| Situation                    | Better Measure              |
| ---------------------------- | --------------------------- |
| No significant outliers      | Mean usually works well     |
| Significant outliers present | Median usually works better |

### Example: Salaries

```text
$40,000
$45,000
$45,000
$45,000
$45,000
$50,000
$500,000
```

Mean:

```text
$770,000 ÷ 7 = $110,000
```

The mean is **$110,000**, but most employees earn between **$40,000–$50,000**.

The **$500,000 salary is an outlier** that pulls the mean upward.

Median:

```text
$45,000
```

Therefore, **$45,000 is a better representation of the typical salary** in this example.

---

# 6. When to Use the Mode

The mode is especially useful for **categorical data** because it identifies the category that occurs most frequently.

Example employee satisfaction responses:

- Strongly agree
- Agree
- Disagree
- Strongly disagree

If **"Strongly agree"** occurs most frequently, then:

**Mode = Strongly agree**

The mode provides a clear indication of the most common category or response.

---

# 7. Quick Reference

| Measure    | Definition          | Best Use                               |
| ---------- | ------------------- | -------------------------------------- |
| **Mean**   | Average value       | Data without significant outliers      |
| **Median** | Middle value        | Data with outliers                     |
| **Mode**   | Most frequent value | Especially useful for categorical data |

### Remember

**Mean = Average**

**Median = Middle**

**Mode = Most frequent**

## Core Rule

**Outliers → Prefer Median**

**No significant outliers → Mean usually works well**

**Categorical data → Mode is useful**

---

# Measures of Dispersion — Range, Variance & Standard Deviation

## 1. Measures of Dispersion

Measures of dispersion describe the **spread or variation** of values in a dataset.

The three main measures covered are:

- **Range**
- **Variance**
- **Standard deviation**

They help data professionals understand how much data values vary and help determine appropriate statistical methods.

---

# 2. Range

### Definition

The **range** is the difference between the largest and smallest value in a dataset.

### Formula

```text
Range = Maximum − Minimum
```

### Example

Exam scores:

```text
Highest = 99
Lowest  = 62
```

```text
Range = 99 − 62
      = 37
```

**Range = 37 percentage points**

### Key Point

- Easy and quick to calculate.
- Gives a quick understanding of the overall spread.
- Uses only the minimum and maximum values.

---

# 3. Variance

### Definition

**Variance** is the average of the squared differences between each data point and the mean.

It measures how much the data varies around the mean.

For the sample calculation:

```text
Variance = Σ(x − x̄)² / (n − 1)
```

### Relationship to Standard Deviation

```text
Variance = (Standard Deviation)²
```

```text
Standard Deviation = √Variance
```

---

# 4. Standard Deviation

### Definition

**Standard deviation measures how spread out values are from the mean.**

It represents the typical distance of a data point from the mean.

### Interpretation

- **Small standard deviation** → values are closer to the mean → less variation.
- **Large standard deviation** → values are farther from the mean → more variation.

### Example

Three distributions have the same mean:

```text
SD = 1 → least spread
SD = 2 → more spread
SD = 3 → most spread
```

The larger the standard deviation, the wider the distribution.

---

# 5. Sample Standard Deviation Formula

For sample data:

```text
s = √[Σ(x − x̄)² / (n − 1)]
```

Where:

- `s` = sample standard deviation
- `x` = individual data value
- `x̄` = sample mean
- `n` = number of data values
- `Σ` = sum

**Important:** Data professionals typically work with samples and use them to make inferences about populations.

---

# 6. Calculating Standard Deviation Step-by-Step

Dataset:

```text
2, 3, 10
```

### Step 1 — Calculate the Mean

```text
(2 + 3 + 10) ÷ 3
= 15 ÷ 3
= 5
```

Mean:

```text
x̄ = 5
```

### Step 2 — Subtract the Mean

```text
2 − 5 = −3
3 − 5 = −2
10 − 5 = 5
```

### Step 3 — Square Each Difference

```text
(−3)² = 9
(−2)² = 4
5² = 25
```

### Step 4 — Calculate Variance

Add the squared differences and divide by `n − 1`:

```text
(9 + 4 + 25) ÷ (3 − 1)
= 38 ÷ 2
= 19
```

Variance:

```text
19
```

### Step 5 — Calculate Standard Deviation

```text
√19 = 4.36
```

**Sample standard deviation = 4.36**

### Calculation Flow

```text
Data
 ↓
Mean
 ↓
Difference from mean
 ↓
Square differences
 ↓
Variance
 ↓
Square root
 ↓
Standard deviation
```

---

# 7. Real-World Example — Rental Prices

Two neighborhoods have the same average monthly rent but different levels of variation.

### Emerald Woods

```text
$900, $950, $1,000, $1,050, $1,100

Mean = $1,000
Standard deviation = $79.05
```

### Rock Park

```text
$500, $650, $1,000, $1,350, $1,500

Mean = $1,000
Standard deviation = $431.56
```

### Comparison

| Neighborhood  |   Mean | Standard Deviation |
| ------------- | -----: | -----------------: |
| Emerald Woods | $1,000 |             $79.05 |
| Rock Park     | $1,000 |            $431.56 |

Both have the same mean:

```text
$1,000
```

But Rock Park has a much larger standard deviation:

```text
$431.56 > $79.05
```

Therefore, **Rock Park has much more variation in rental prices**.

### Main Lesson

The **mean alone does not tell you how spread out the data is**.

Two datasets can have:

```text
Same mean
+
Different standard deviation
=
Different levels of variation
```

---

# 8. Practical Uses of Standard Deviation

Standard deviation can be used to understand variation in:

- Rental prices
- Ad revenue
- Stock prices
- Employee salaries
- Exam scores
- Other numerical datasets

It helps data professionals quickly understand the basic structure and variability of their data.

---

# 9. Quick Reference

| Measure                | Meaning                                             | Key Formula                        |
| ---------------------- | --------------------------------------------------- | ---------------------------------- |
| **Range**              | Overall difference between highest and lowest value | `Max − Min`                        |
| **Variance**           | Average squared difference from the mean            | `Σ(x − x̄)² / (n − 1)` for a sample |
| **Standard Deviation** | Typical distance of values from the mean            | `√Variance`                        |

### Remember

```text
Range → Overall spread
Variance → Squared spread
Standard deviation → Typical spread from the mean
```

**Higher standard deviation = more variation**

**Lower standard deviation = less variation**

---

# Measures of Position: Percentiles, Quartiles, IQR & Five-Number Summary

## 1. Measures of Position

Measures of position show the **relative location/rank of a value** compared with other values in a dataset.

They help determine whether a value is in the **lower, middle, or upper portion** of the dataset.

---

## 2. Percentiles

A **percentile** is the value below which a certain percentage of the data falls.

- Percentiles divide data into **100 parts**.
- Used to compare the relative position of a value.

### Examples

- **99th percentile** → the value is higher than 99% of the data.
- **75th percentile** → the value is higher than 75% of the data.
- **50th percentile** → the value is higher than 50% of the data.

### Important: Percentile ≠ Percentage

A test score of **90%** does not necessarily mean the score is in the **90th percentile**.

- **Percentage** = how much of the test you answered correctly.
- **Percentile** = how your result compares with other people's results.

---

## 3. Quartiles

**Quartiles** divide an ordered dataset into **4 equal parts**.

Each section represents approximately **25% of the data**.

| Quartile | Percentile | Meaning                         |
| -------- | ---------: | ------------------------------- |
| **Q1**   |       25th | 25% of values are below it      |
| **Q2**   |       50th | Median; 50% below and 50% above |
| **Q3**   |       75th | 75% of values are below it      |

### Quartile Example

Cars sold:

`[18, 13, 6, 10, 15, 7, 10, 9]`

### Step 1: Sort the data

`[6, 7, 9, 10, 10, 13, 15, 18]`

### Step 2: Find Q2 (Median)

Middle values = `10, 10`

`Q2 = (10 + 10) / 2 = 10`

### Step 3: Find Q1

Lower half:

`[6, 7, 9, 10]`

Middle values = `7, 9`

`Q1 = (7 + 9) / 2 = 8`

### Step 4: Find Q3

Upper half:

`[10, 13, 15, 18]`

Middle values = `13, 15`

`Q3 = (13 + 15) / 2 = 14`

### Result

- **Q1 = 8**
- **Q2 = 10**
- **Q3 = 14**

Interpretation:

- Lower 25% → **8 or fewer**
- Middle 50% → **8 to 14**
- Upper 25% → **14 or more**

> Different methods can calculate quartiles/percentiles. For small datasets, the method used can noticeably affect the result. NumPy's `percentile()` supports multiple calculation methods.

---

## 4. Interquartile Range (IQR)

The **IQR** represents the spread of the **middle 50%** of the dataset.

### Formula

`IQR = Q3 - Q1`

### Example

`Q1 = 8`
`Q3 = 14`

`IQR = 14 - 8 = 6`

So, the middle 50% of the data spans **6 units**.

### IQR and Outliers

A common rule considers values outside:

`Q1 - (1.5 × IQR)`

and

`Q3 + (1.5 × IQR)`

as potential **outliers**.

### Why IQR is useful

- Measures the spread of the middle 50%.
- Less affected by extreme values than the range.
- Useful for identifying potential outliers.

---

## 5. Five-Number Summary

The **five-number summary** describes the main divisions of a dataset:

1. **Minimum**
2. **Q1**
3. **Q2 (Median)**
4. **Q3**
5. **Maximum**

### Example

For the car-sales dataset:

- Minimum = `6`
- Q1 = `8`
- Median/Q2 = `10`
- Q3 = `14`
- Maximum = `18`

**Five-number summary:**

`6, 8, 10, 14, 18`

It provides a quick view of:

- Extreme values
- Center
- Spread
- Overall distribution

---

## 6. Box Plot

A **box plot** visually represents the five-number summary.

- **Box** → Q1 to Q3
- **Line inside box** → Median (Q2)
- **Lower whisker** → Q1 to minimum
- **Upper whisker** → Q3 to maximum
- **Box length** → IQR

### Key idea

`IQR = length of the box = Q3 - Q1`

---

## Quick Reference

| Concept                 | Key Point                                    |
| ----------------------- | -------------------------------------------- |
| **Percentile**          | Relative position out of 100 parts           |
| **Q1**                  | 25th percentile                              |
| **Q2**                  | 50th percentile / median                     |
| **Q3**                  | 75th percentile                              |
| **IQR**                 | Q3 - Q1; middle 50%                          |
| **Five-number summary** | Min, Q1, Q2, Q3, Max                         |
| **Box plot**            | Visualizes the five-number summary           |
| **Outlier rule**        | Below `Q1 - 1.5×IQR` or above `Q3 + 1.5×IQR` |

## Key Takeaway

**Percentiles and quartiles describe where values are located within a dataset. IQR measures the spread of the middle 50%, while the five-number summary and box plot provide a quick overview of the dataset's distribution.**
