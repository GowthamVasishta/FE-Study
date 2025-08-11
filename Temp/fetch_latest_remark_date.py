# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 11:45:30 2025

@author: gowth
"""
import pandas as pd
import numpy as np

loan_names_90 = [f"Loan_{i}" for i in range(1, 91)]  # 90 loans
dates_180 = pd.date_range(start="2025-02-01", periods=180, freq="D")

# Create all combinations of loans and dates with random prices
data_90_loans = [
    (loan, date, round(np.random.uniform(90, 110), 2))
    for loan in loan_names_90
    for date in dates_180
]

df_90_loans = pd.DataFrame(data_90_loans, columns=["loan_name", "date", "price"])

# Ensure 'date' column is datetime
df_90_loans['date'] = pd.to_datetime(df_90_loans['date'])

# Get latest remark date per loan
latest_dates_90 = df_90_loans.groupby('loan_name', as_index=False)['date'].max()

# Get full row for latest date (price included)
latest_rows_90 = df_90_loans.loc[df_90_loans.groupby('loan_name')['date'].idxmax()]

latest_rows_90.head()