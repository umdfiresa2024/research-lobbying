import pandas as pd
from Bio import pairwise2
import math
import re

# Load the cleaned CRSP and flight data
crsp = pd.read_csv('../cleaned-crsp.csv')
flight = pd.read_csv('../cleaned-flight.csv')

L = len(flight)
n = 1

# Create a list of the cleaned company names from the CRSP data
cleaned_company_names = crsp['Company'].unique()

# Function to normalize common company suffixes


def normalize_company_name(name):
    name = str(name).lower()
    # Replace common suffixes with a standard 'co'
    name = re.sub(r'\b(company|corp|corporation|co)\b', 'co', name)
    return name


# Normalize CRSP company names and map them back to original names
crsp['Normalized Name'] = crsp['Company'].apply(normalize_company_name)
normalized_to_actual = dict(zip(crsp['Normalized Name'], crsp['Company']))

# Function to match flight company names to CRSP company names using Smith-Waterman algorithm


def match_company_name_smith_waterman(company_name, crsp_names):
    global n
    company_name = normalize_company_name(company_name)

    best_score = -float('inf')
    best_match = "None"

    # Perform alignment of flight company name with each CRSP company name
    for crsp_name in crsp_names:
        # Perform local alignment using Smith-Waterman algorithm
        alignments = pairwise2.align.localxx(company_name, crsp_name)
        # The alignment score is in the 3rd position of the tuple
        score = alignments[0][2]

        # Keep track of the best score and corresponding CRSP company name
        if score > best_score:
            best_score = score
            best_match = crsp_name

    # Progress bar
    prog = math.floor(n / L * 10)
    print(f"{n}/{L} | {'o' * prog}{'_' * (10 - (prog))} | {prog * 10}%", end='\r')
    n += 1

    return best_match  # Return the best matched CRSP name


# Ensure the 'Company' column in flight data is treated as strings
flight['Company'] = flight['Company'].astype(str)

# Apply the matching function using Smith-Waterman to the 'Company' column in flight data
cleaned_flight_df = flight[['Company', 'Total GHG']]
cleaned_flight_df['Matched'] = flight['Company'].apply(
    lambda x: match_company_name_smith_waterman(x, cleaned_company_names))

# Map the normalized company name back to the actual CRSP company name
cleaned_flight_df['Matched'] = cleaned_flight_df['Matched'].map(
    normalized_to_actual)

# Save the cleaned data
cleaned_flight_df.to_csv('merged_flight_data.csv', index=False)
print("df saved")
