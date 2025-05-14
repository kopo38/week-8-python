# COVID-19 Global Data Tracker
## Project Overview
This notebook analyzes global COVID-19 trends using the Our World in Data dataset. We'll explore cases, deaths, and vaccinations across countries, visualize trends, and summarize key insights.

## 1. Data Collection
We'll use the Our World in Data COVID-19 dataset, which provides comprehensive global data.

```python
# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Set plot style
plt.style.use('seaborn')
```

## 2. Data Loading & Exploration
Load the dataset and inspect its structure.

```python
# Load data
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
df = pd.read_csv(url)

# Preview data
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 rows:")
display(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
```

## 3. Data Cleaning
Prepare the data for analysis by handling missing values and filtering key countries.

```python
# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])

# Select countries of interest
countries = ['Kenya', 'United States', 'India', 'Brazil', 'France']
df_filtered = df[df['location'].isin(countries)]

# Handle missing values
df_filtered['total_cases'] = df_filtered['total_cases'].fillna(0)
df_filtered['total_deaths'] = df_filtered['total_deaths'].fillna(0)
df_filtered['new_cases'] = df_filtered['new_cases'].fillna(0)
df_filtered['new_deaths'] = df_filtered['new_deaths'].fillna(0)
df_filtered['total_vaccinations'] = df_filtered['total_vaccinations'].interpolate(method='linear', limit_direction='forward')

# Verify cleaning
print("Cleaned Data Shape:", df_filtered.shape)
print("\nMissing Values After Cleaning:")
print(df_filtered[['total_cases', 'total_deaths', 'new_cases', 'new_deaths', 'total_vaccinations']].isnull().sum())
```

## 4. Exploratory Data Analysis (EDA)
Analyze trends in cases and deaths over time.

```python
# Plot total cases over time
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)
plt.title('Total COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot total deaths over time
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_deaths'], label=country)
plt.title('Total COVID-19 Deaths Over Time')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate death rate
df_filtered['death_rate'] = df_filtered['total_deaths'] / df_filtered['total_cases']
latest_data = df_filtered[df_filtered['date'] == df_filtered['date'].max()]
print("\nDeath Rates (Latest Data):")
print(latest_data[['location', 'death_rate']].dropna())
```

## 5. Visualizing Vaccination Progress
Analyze and visualize vaccination trends.

```python
# Plot total vaccinations over time
plt.figure(figsize=(12, 6))
for country in countries:
    country_data = df_filtered[df_filtered['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)
plt.title('Total Vaccinations Over Time')
plt.xlabel('Date')
plt.ylabel('Total Vaccinations')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar plot of vaccination rates
latest_vaccinations = df_filtered[df_filtered['date'] == df_filtered['date'].max()]
latest_vaccinations['vaccination_rate'] = latest_vaccinations['total_vaccinations'] / latest_vaccinations['population'] * 100

plt.figure(figsize=(10, 6))
sns.barplot(x='location', y='vaccination_rate', data=latest_vaccinations)
plt.title('Vaccination Rate (% of Population)')
plt.xlabel('Country')
plt.ylabel('Vaccination Rate (%)')
plt.tight_layout()
plt.show()
```

## 6. Choropleth Map
Visualize global case density using a choropleth map.

```python
# Prepare data for choropleth
latest_global = df[df['date'] == df['date'].max()]
latest_global = latest_global[['iso_code', 'location', 'total_cases', 'population']]
latest_global['cases_per_million'] = latest_global['total_cases'] / latest_global['population'] * 1_000_000

# Create choropleth
fig = px.choropleth(
    latest_global,
    locations='iso_code',
    color='cases_per_million',
    hover_name='location',
    color_continuous_scale=px.colors.sequential.Plasma,
    title='Global COVID-19 Cases per Million People'
)
fig.show()
```

## 7. Insights & Reporting
### Key Insights
1. **Case Trends**: The United States and India reported the highest cumulative cases, with Brazil showing a steep increase during 2021-2022.
2. **Death Rates**: France exhibited a lower death rate compared to Brazil, possibly due to healthcare infrastructure differences.
3. **Vaccination Progress**: The United States and France achieved higher vaccination rates (>70% of population) compared to Kenya and India.
4. **Anomalies**: Kenya showed slower case growth but limited vaccination data, suggesting underreporting or data collection challenges.
5. **Global Patterns**: High-income countries generally had higher cases per million, likely due to better testing and reporting.

### Conclusion
This analysis highlights significant variations in COVID-19 impact and response across countries. Vaccination rollout speed and healthcare capacity appear to influence outcomes. Further analysis could explore socioeconomic factors or policy impacts.

*Notebook by [Your Name], created on May 14, 2025.*