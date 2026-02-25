# 👥 People Analytics: Salary and Career Analysis

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-green)

## 📝 About the Project
This project presents an **Exploratory Data Analysis (EDA)** pipeline focused on Human Resources (*People Analytics*).

The objective was to apply Descriptive Statistical techniques using Python to analyze salary patterns, demographic distribution, and correlations between career variables (such as Age and Income) in a simulated dataset.

## ⚠️ Technical Note (Proof of Concept)
This project serves as a **Proof of Concept (PoC)** for structuring data analysis pipelines. 

The database used is synthetic and intentionally small ($n=20$) to focus the project strictly on code construction, data cleaning, and visualizations (EDA). In a real production environment, this exact script would be scaled for databases with thousands of records, where distributions and correlations would reach proper statistical significance.

## 🧠 Analysis Performed
The script generates visualizations to answer business questions such as:

⚫ What is the distribution of employees by region?

⚪ How are salaries distributed? (Detection of asymmetries)

⚫ Are there *outliers* (discrepant values) in salaries?

⚪ Is there a linear correlation between the employee's age and their compensation?

## 🛠️ Technologies Used

⚫ **Python:** Base language.

⚪ **Pandas:** Manipulation and structuring of tabular data.

⚫ **Seaborn & Matplotlib:** Statistical data visualization.

⚪ **OS:** Directory management for automatic export of visual reports.

## 📈 Visualizations Generated

### 1. Geographic Distribution
Absolute frequency analysis of employees by region.
![Região](images/distribuicao_regiao.png)

### 2. Income Analysis (Histogram)
Frequency distribution visualization of salaries.
![Histograma](images/histograma_renda.png)

### 3. Outlier Detection (Boxplot)
Use of position measures (quartiles) to identify salary dispersion.
![Boxplot](images/boxplot_renda.png)

### 4. Correlation: Age x Income
Scatter plot to investigate the relationship between professional maturity and compensation.
![Scatter](images/scatter_idade_renda.png)

## 🚀 How to Run

1. Clone this repository.

2. Install the dependencies:
   ```bash
   pip install pandas seaborn matplotlib
