# Credit Card Transaction Analysis

## Overview
This project analyzes credit card transaction data to identify spending trends, unusual transactions, and customer behavior patterns using Python and data analytics techniques.

The analysis focuses on:
- Transaction trends over time
- Category-level spending analysis
- Unusual transaction detection using threshold logic
- Data visualization and reporting

---

## Project Objectives
- Clean and preprocess transaction data
- Explore customer spending behavior
- Detect potentially unusual transactions
- Create visualizations for business insights
- Practice real-world data analytics workflows

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- VS Code
- Git & GitHub

---

## Dataset Information
The dataset contains simulated credit card transaction records including:
- Transaction amount
- Transaction category
- Transaction date
- Merchant information
- Customer details

---

## Key Features

### Data Cleaning
- Removed missing/null values
- Converted date columns into datetime format
- Standardized transaction categories

### Exploratory Data Analysis
- Monthly spending trends
- Category-based transaction analysis
- Average transaction amount calculations

### Unusual Transaction Detection
Transactions were flagged as unusual when:
- Transaction amount exceeded 2x the category average

Example logic:
```python
threshold = category_avg * 2

if transaction_amount > threshold:
    flag = "Unusual"
