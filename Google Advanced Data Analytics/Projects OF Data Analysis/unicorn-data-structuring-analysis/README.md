# Unicorn Companies - Datetime Structuring & EDA

## 📌 Project Overview

This project demonstrates data structuring and temporal exploratory data analysis (EDA) techniques using Python. Using a dataset of over 1,000 unicorn companies ($1B+ valuations), the analysis explores how founding dates, join dates, and temporal groupings (weekly/quarterly) correlate with time-to-unicorn milestones and valuation metrics.

## 🛠️ Key Techniques & Features

- **Datetime Formatting:** Converting raw date strings into standard pandas `datetime64` types.
- **Temporal Component Extraction:** Extracting month names (`dt.month_name()`), ISO calendar weeks (`dt.strftime('%Y-W%V')`), and financial quarters (`dt.to_period('Q')`).
- **Feature Engineering:** Calculating duration metrics (`Years To Join = Year Joined - Year Founded`).
- **Data Restructuring:** Filtering, subset concatenation (`pd.concat`), and multi-level aggregations (`groupby()`).
- **Data Visualizations:** Generating custom boxplots, single-variable bar plots, and year-over-year grouped bar charts using Seaborn and Matplotlib.

## 🚀 How to Run Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/unicorn-data-structuring-eda.git](https://github.com/your-username/unicorn-data-structuring-eda.git)
   ```
