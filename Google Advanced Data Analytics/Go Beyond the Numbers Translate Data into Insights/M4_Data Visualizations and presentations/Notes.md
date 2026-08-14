## Reference Guide: Tableau Public Overview and Workspace Mechanics

This section covers the core workflow, privacy guidelines, and interface structure of Tableau Public for creating, building, and publishing data visualizations.

### 1. Platform Accessibility and Data Privacy Rules

- **Web Authoring:** Allows creation of visualizations directly through a web browser without installing local software (`Create` > `Web Authoring`).
- **Tableau Desktop Public Edition:** Free standalone software available for Mac and Windows.
- **Public Data Policy:** Tableau Public is intended strictly for public, non-sensitive data analysis. All published workbooks and connected datasets are freely accessible to the public.

---

### 2. Data Source Page Interface

The Data Source page connects and configures incoming data sources before visual building.

1. **Connections Pane (Left):** Lists uploaded files, database connections, and integrated data assets.
2. **Fields Overview List:** Displays auto-detected columns sorted by Tableau into Dimensions vs. Measures and Discrete vs. Continuous variables.
3. **Data Grid & Calculation Workspace (Center-Right):** Displays row-level previews; allows creation of custom calculated fields, groups, sets, and parameters. (Enable **Update Automatically** for live preview updates).
4. **Publish Action (Top-Right):** Acts as the primary Save mechanism in Tableau Public by deploying changes to your public profile.
5. **Navigation Controls (Bottom-Left):** Buttons to toggle between the Data Source page and new Worksheets, Dashboards, or Stories.

---

### 3. Data Design Page Workspace

The workspace where visualizations and interactive dashboards are built.

1. **Data Pane (Far-Left):** Houses categorical and quantitative variables split into discrete/continuous dimensions and measures.
2. **Control Cards (Left-Center):**
   - **Pages Shelf:** Creates animated or step-by-step visual sequences across categories.
   - **Filters Shelf:** Filters data subsets out of the view.
   - **Marks Card:** Controls visual attributes including Color, Size, Label, Detail, and Tooltip.
3. **Columns and Rows Shelves (Top):** Primary drag-and-drop landing zones for establishing chart axes, structure, and headers.
4. **Main View Panel (Center):** Canvas displaying real-time visual output updates as variables are applied.
5. **Show Me & Publish Controls (Top-Right):**
   - **Show Me Menu:** Expandable palette outlining chart templates and structural requirements for each visualization type.
   - **Publish Menu:** Options to update or save changes to your profile.

---

_Note: Additional notes and reference material will be appended here in subsequent updates._

# Module 4 — Data Visualization & Tableau README

## 1. Tableau Terms

### Tableau

A data visualization software primarily used to present data to inform and improve businesses.

### Action

A Tableau tool that allows an audience to interact with a visualization or dashboard by controlling selections.

### Bin

A segment of data that groups values into categories.

### Box Plot

A visualization showing the locality, spread, and skew of groups of values within quartiles.

### Continuous

A mathematical concept where a measure or dimension has an infinite and uncountable number of possible outcomes.

### Discrete

A mathematical concept where a measure or dimension has a finite and countable number of possible outcomes.

### Dimensions

Qualitative data values used to categorize and group data to reveal details.

### Measures

Numeric values that can be aggregated or used in calculations.

### Heatmap

A visualization showing the magnitude of values using two colors.

### Histogram

A visualization showing an approximate representation of the distribution of values in a dataset.

### Set

A Tableau custom field created from a larger dataset using custom conditions.

### Story

A group of Tableau dashboards or worksheets assembled into a presentation.

---

# 2. Previous Module Terms

## A–C

### Bias

Organizing data into groupings, categories, or variables that misrepresent the whole dataset.

### Categorical Data

Data divided into a limited number of qualitative groups.

### Cleaning

Removing errors that may distort data or make it less useful.

### Collective Outliers

A group of abnormal points that follow similar patterns and are isolated from the rest of the population.

### Contextual Outliers

Data points that are normal under certain conditions but become anomalies under other conditions.

### CSV File

A simple text file commonly used to store or import data.

---

## D

### Database (DB) File

A file type used to store data, often in tables, indexes, or fields.

### Data Ethics

Standards of right and wrong that guide how data is collected, shared, and used.

### Data Governance

The formal management of an organization's data assets.

### Data Source

The location where data originates.

### Data Visualization

A graph, chart, diagram, or dashboard representing information.

### Deduplication

The elimination or removal of duplicate/matching data values.

### Discovering

Familiarizing yourself with data to understand how it can be used.

### Documentation String / Docstring

Text that explains what a method or function does.

### Dummy Variables

Variables containing `0` or `1` to indicate the presence or absence of something.

---

## E–G

### Exploratory Data Analysis (EDA)

The process of investigating, organizing, and analyzing datasets to understand their main characteristics.

The six main EDA practices are:

1. Discovering
2. Structuring
3. Cleaning
4. Joining
5. Validating
6. Presenting

### Extracting

Retrieving data from a data source for further processing.

### Filtering

Selecting a smaller part of a dataset based on specified values.

### First-Party Data

Data gathered from inside your own organization.

### Global Outliers

Values completely different from the overall data group and not associated with other outliers.

### Grouping

Aggregating individual observations into groups.

---

## H–I

### Hypothesis

A theory or explanation based on evidence that has not yet been proven true.

### Input Validation

Analyzing and double-checking data to ensure it is complete, error-free, and high quality.

### `info()`

A Pandas method that provides the number of entries and their data types.

### `Int64`

A standard integer data type representing very large positive and negative integers.

---

## J–M

### Joining

Augmenting data by adding values from other datasets.

### JSON File

A data storage format based on JavaScript Object Notation.

### Label Encoding

A transformation technique that assigns each category a unique number.

### Merging

Combining two or more DataFrames using specified column(s).

### Missing Data

A data value that is not stored for a variable in an observation.

---

## N–O

### Non-Null Count

The total number of entries in a column that are not blank.

### One-Hot Encoding

A transformation technique that converts one categorical variable into multiple binary variables.

### Outliers

Observations that are abnormally distant from other values or the overall pattern of a population.

---

## P–V

### PACE

A workflow for staying focused on the end goal:

- **P** = Plan
- **A** = Analyze
- **C** = Construct
- **E** = Execute

### Presenting

Making a cleaned dataset available to others for analysis or further modeling.

### Second-Party Data

Data gathered outside your organization but directly from the original source.

### Slicing

Breaking information into smaller parts for efficient examination and analysis.

### Sorting

Arranging data into a meaningful order.

### String

A sequence of characters and punctuation containing textual information.

### Structuring

Organizing or transforming raw data so it can be more easily visualized, explained, or modeled.

### Third-Party Data

Data gathered outside your organization and aggregated.

### Validating

Verifying that data is consistent and high quality.

---

# 3. Module 4 Quick Reference

| Term             | Remember                            |
| ---------------- | ----------------------------------- |
| Tableau          | Data visualization software         |
| Action           | Interactive dashboard control       |
| Bin              | Groups values into categories       |
| Box Plot         | Shows locality, spread, skew        |
| Continuous       | Infinite, uncountable outcomes      |
| Discrete         | Finite, countable outcomes          |
| Dimension        | Qualitative/categorical data        |
| Measure          | Numeric data used in calculations   |
| Heatmap          | Magnitude represented by colors     |
| Histogram        | Distribution of values              |
| Set              | Custom Tableau field                |
| Story            | Collection of dashboards/worksheets |
| Deduplication    | Remove duplicates                   |
| Dummy Variables  | `0/1` indicators                    |
| Label Encoding   | Categories → numbers                |
| One-Hot Encoding | Category → binary columns           |
| Outliers         | Abnormally distant observations     |
| Data Ethics      | Responsible data collection/use     |
| Data Governance  | Formal data asset management        |

---

# Module 4 — Activity Exemplar: Course 2 TikTok Project

## 1. Purpose of the Exemplar

The exemplars demonstrate possible completed versions of the Course 2:

- Python notebook
- Tableau visualization
- Executive summary

The exemplar is **one possible approach**. Your work may differ in language, answers, layout, colors, or visual design.

The main goal is to understand the **purpose and functionality** of each deliverable.

---

# 2. Python Notebook Requirements

Compare your completed Python notebook with the exemplar and identify:

- What you did well
- Where you can improve

Use this reflection to guide your progress through future projects.

### Your Python Notebook Should:

- Include correct code for performing **EDA**
- Include correct code for creating **data visualizations**
- Clearly communicate answers to questions about:
  - Code input
  - Results

### Important

Your notebook does **not** need to exactly match the exemplar.

Differences may include:

- Specific language
- Answers to questions
- Notebook layout

What matters is understanding the purpose and functionality of a Python notebook for data analysis.

---

# 3. Tableau Visualization Requirements

Compare your Tableau visualization with the exemplar and identify:

- What you did well
- Where you can improve

### Your Tableau Visualization Should:

- Use the **same variables identified during your Python EDA**
- Enhance the **scatterplot initially created with Python**
- Display data clearly and accurately in Tableau Public

### Important

Your visualization may differ from the exemplar in areas such as:

- Colors
- Visual design
- Presentation choices

What matters is understanding the purpose and functionality of **Tableau Public for data visualization**.

---

# 4. Executive Summary Requirements

Compare your executive summary with the exemplar and identify:

- What you did well
- Where you can improve

### Your Executive Summary Should:

- Include key information to share with teammates and/or stakeholders
- Use **clear and concise language**
- Effectively communicate your results

### Important

Your executive summary may differ from the exemplar in:

- Language
- Visual design
- Presentation style

What matters is understanding the purpose and organization of an executive summary for a data project.

---

# 5. Course 2 Project Quality Checklist

### Python Notebook

- [ ] Correct EDA code
- [ ] Correct visualization code
- [ ] Clear explanation of inputs and results

### Tableau

- [ ] Uses variables identified during Python EDA
- [ ] Enhances the Python scatterplot
- [ ] Data is clear and accurate

### Executive Summary

- [ ] Contains key findings/information
- [ ] Appropriate for teammates/stakeholders
- [ ] Clear and concise communication

---

# 6. Core Principle

**Do not copy the exemplar exactly.**

The exemplar represents **one valid way** to complete the project.

Focus on:

**Correct Analysis → Clear Visualization → Concise Communication → Stakeholder Understanding**
