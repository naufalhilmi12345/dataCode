# Dashboard for Heart Attack Case Analysis

## Description

This dashboard is designed to provide insight into **heart attack cases** based on data sourced from a CSV file. The presented analysis and visualization aim to help understand patient characteristics, trends, and the distribution of heart attacks, which can be useful for further decision-making.

## Data Source

- CSV file used: `Medicaldataset.csv`.
- This CSV file consists of several columns, including:
  - `Age`: Patient's age
  - `Gender`: Biological sex of the patient (1 for male, 0 for female)
  - `Heart Rate`: Number of heartbeats per minute
  - `Systolic Blood Pressure`: Pressure in arteries during heart contraction
  - `Diastolic Blood Pressure`: Pressure in arteries between heartbeats
  - `Blood Sugar`: Glucose level in the patient’s blood
  - `Ck-mb`: Cardiac enzyme released during heart muscle damage
  - `Troponin`: Protein biomarker for heart muscle injury
  - `Result`: Label indicating whether or not the patient experienced a heart attack

## Dashboard Content

The dashboard can be accessed at [Heart Attack Case Dashboard](https://lookerstudio.google.com/reporting/cb59c434-958d-4613-a67c-b0b1cd75a798/page/p_ftne2w8ftd)

### Summary

The **Summary** section provides a general overview of the available data, including:

- **Total number of heart attack cases**.
- **Patient percentage by gender**.
- **Patient count by age group**.

### Visualizations

- **Pie Chart**: Distribution of patients by gender (Male and Female).
- **Bar Chart**: Distribution of heart attack cases by age group.

### Pivot Table

A **pivot table** is available for more granular analysis:

- Groups patients by **gender** and **age group**.
- Counts the number of heart attack cases in each group.

This is helpful for identifying patterns or trends, for instance:

- Are certain age groups more vulnerable?
- Are there significant differences between genders?

### Detail Table

The last section displays a **detailed table** with complete information for each patient, reflecting the data available in the CSV.  
This is helpful if you need more granular details for further investigation.
