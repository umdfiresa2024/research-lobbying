import pandas as pd
import re

# Load the flight data
flight = pd.read_csv('../../../flight_2010.csv')

# Function to process each row and extract the company names and their respective GHG contributions
def calculate_ghg(row):
    # Convert to string to avoid float issues
    companies = str(row['PARENT COMPANIES'])
    ghg_quantity = row['GHG QUANTITY (METRIC TONS CO2e)']

    # Check if the companies field is valid (not empty or missing)
    if pd.isna(companies):
        return []

    # Extract company names and percentages, accounting for the semicolon
    pattern = r'([^;()]+)\s\((\d+)%\)'
    matches = re.findall(pattern, companies)

    # Calculate each company's GHG contribution
    company_ghg = []
    for match in matches:
        company_name = match[0].strip()
        percentage = int(match[1]) / 100  # Convert percentage to a decimal
        company_ghg.append((company_name, percentage * ghg_quantity))

    return company_ghg

# Initialize a dictionary to accumulate the GHG contributions for each company
ghg_totals = {}

# Iterate through each row of the flight dataframe
for index, row in flight.iterrows():
    contributions = calculate_ghg(row)
    for company, ghg in contributions:
        if company in ghg_totals:
            ghg_totals[company] += ghg
        else:
            ghg_totals[company] = ghg

# Convert the dictionary to a DataFrame
result_df = pd.DataFrame(list(ghg_totals.items()), columns=['Company', 'Total GHG'])

# Display the result
print(result_df)

# Save the result to a CSV file
result_df.to_csv("cleaned-flight.csv", index=False)
