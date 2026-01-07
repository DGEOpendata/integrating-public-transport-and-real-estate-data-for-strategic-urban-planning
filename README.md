## Integrating Public Transport and Real Estate Data for Strategic Urban Planning

### Overview
This project aims to integrate public transportation usage data with real estate market transactions to enhance urban planning strategies in Abu Dhabi. By analyzing patterns and correlations between these datasets, city planners and policy makers can make data-driven decisions that optimize infrastructure and resource allocation.

### Datasets Used
- **Public Transportation Usage Statistics**: Provides data on passenger numbers, peak usage times, and satisfaction ratings for various transport modes.
- **Real Estate Market Transactions**: Contains information on property sales, transaction values, and property types.

### Implementation Steps
1. **Data Loading**: Load the datasets using Pandas.
   python
   import pandas as pd
   public_transport_data = pd.read_csv('Public_Transportation_Usage_Statistics.csv')
   real_estate_data = pd.read_excel('Real_Estate_Transactions.xlsx')
   

2. **Data Summarization**: Group data by relevant areas and calculate summaries.
   python
   transport_summary = public_transport_data.groupby('Route Area')['Number of Passengers'].sum().reset_index()
   real_estate_summary = real_estate_data.groupby('Area')['Transaction Value'].sum().reset_index()
   

3. **Data Merging**: Merge datasets on common areas to facilitate correlation analysis.
   python
   merged_data = pd.merge(transport_summary, real_estate_summary, left_on='Route Area', right_on='Area')
   

4. **Correlation Analysis**: Analyze the correlation between transport usage and real estate transactions.
   python
   correlation = merged_data['Number of Passengers'].corr(merged_data['Transaction Value'])
   print(f'Correlation between transport usage and real estate transactions: {correlation}')
   

### Conclusion
By integrating and analyzing these datasets, stakeholders can gain valuable insights into the interactions between public transport usage and real estate market dynamics. This approach supports strategic urban planning and helps in making informed decisions to improve city infrastructure and services.