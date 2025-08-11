# -*- coding: utf-8 -*-
"""
Created on Mon Aug 11 09:51:45 2025

@author: gowth
"""

import pandas as pd
from rapidfuzz import fuzz, process

# Example internal dataset
internal_df = pd.DataFrame({
    "internal_id": ["INT001", "INT002"],
    "borrower_name": ["ABC Corp 2028", "XYZ Limited 2030"],
    "maturity_date": ["2028-05-15", "2030-11-20"],
    "currency": ["USD", "EUR"]
})

# Example external dataset
external_df = pd.DataFrame({
    "external_id": ["EXT_A", "EXT_B"],
    "borrower_name": ["ABC Corporation 2028", "XYZ Ltd. 2030"],
    "maturity_date": ["2028-05-15", "2030-11-20"],
    "currency": ["USD", "EUR"]
})

# Function to find best match
def match_external_id(internal_row, external_df):
    best_match = None
    best_score = 0
    
    for _, ext_row in external_df.iterrows():
        # Calculate name similarity
        name_score = fuzz.token_sort_ratio(internal_row["borrower_name"], ext_row["borrower_name"])
        
        # Add bonus points if maturity date matches
        date_bonus = 20 if internal_row["maturity_date"] == ext_row["maturity_date"] else 0
        
        # Add bonus points if currency matches
        currency_bonus = 10 if internal_row["currency"] == ext_row["currency"] else 0
        
        total_score = name_score + date_bonus + currency_bonus
        
        if total_score > best_score:
            best_score = total_score
            best_match = ext_row["external_id"]
    
    return best_match, best_score

# Apply matching
internal_df[["matched_external_id", "match_score"]] = internal_df.apply(
    lambda row: match_external_id(row, external_df), axis=1, result_type="expand"
)

print(internal_df)
