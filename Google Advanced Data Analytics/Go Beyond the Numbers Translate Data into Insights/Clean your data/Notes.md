## Reference Guide: Data Deduplication in Python

This section details how to identify, evaluate, and remove duplicate data within pandas DataFrames, including key criteria for deciding when deduplication is appropriate.

---

### 1. Overview and Key Concepts

- **Data Deduplication:** The process of identifying and removing duplicate data values or identical rows from a dataset.
- **Role in Data Cleaning:** Essential step in Exploratory Data Analysis (EDA) to ensure accuracy in metrics, aggregations, and statistical modeling.

---

### 2. Decision Framework: Drop vs. Keep Duplicates

Before dropping duplicate rows, evaluate the domain context and analytical objective:

- **When to Drop Duplicates:**
  - When duplicates represent clear recording errors, duplicate submission entries, or redundant records.
  - _Example:_ Duplicate house addresses in real estate valuation data (counting a house twice skews average price and inventory metrics).
- **When to Keep Duplicates:**
  - When duplicate values reflect valid, naturally occurring repeated events.
  - _Example:_ Recorded throw distances in shot-put athletic training (multiple throws often yield identical rounded distance values).

---

### 3. Identifying Duplicates with Pandas

#### `df.duplicated()`

Returns a Boolean Series indicating whether each row is a duplicate (`True`) or unique (`False`).

- **Key Parameters:**
  - `subset`: Column label or sequence of labels to check for duplicates (defaults to all columns).
  - `keep`: Determines which duplicate occurrence to mark as original/unique:
    - `'first'` (default): Marks the first occurrence as `False` (unique) and subsequent occurrences as `True`.
    - `'last'`: Marks the last occurrence as `False` and previous occurrences as `True`.
    - `False`: Marks all occurrences of duplicates as `True`.

- **Syntax / Examples:**

  ```python
  # Check for duplicate entire rows
  df.duplicated()

  # Check duplicates based on specific columns
  df.duplicated(subset=['style'])

  # Mark last occurrence as original (unique)
  df.duplicated(subset=['style'], keep='last')
  ```
