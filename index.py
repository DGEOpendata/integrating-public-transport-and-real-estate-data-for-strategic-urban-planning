python
import pandas as pd

# Load datasets
public_transport_data = pd.read_csv('Public_Transportation_Usage_Statistics.csv')
real_estate_data = pd.read_excel('Real_Estate_Transactions.xlsx')

# Example analysis: Correlate high usage transport routes with real estate transactions
# Summarize transport usage by area
transport_summary = public_transport_data.groupby('Route Area')['Number of Passengers'].sum().reset_index()

# Summarize real estate transactions by area
real_estate_summary = real_estate_data.groupby('Area')['Transaction Value'].sum().reset_index()

# Merge datasets on area
merged_data = pd.merge(transport_summary, real_estate_summary, left_on='Route Area', right_on='Area')

# Calculate correlation
correlation = merged_data['Number of Passengers'].corr(merged_data['Transaction Value'])

print(f'Correlation between transport usage and real estate transactions: {correlation}')
