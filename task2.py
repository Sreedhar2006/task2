import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df1 = pd.read_csv("Unemployment in India.csv")
df2 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

df1['Date'] = pd.to_datetime(df1['Date'], dayfirst=True)
df2['Date'] = pd.to_datetime(df2['Date'], dayfirst=True)

df1['Source'] = 'Dataset1'
df2['Source'] = 'Dataset2'

df = pd.concat([df1, df2], ignore_index=True)

df = df.dropna(subset=['Estimated Unemployment Rate (%)'])

national_trend = df.groupby('Date')['Estimated Unemployment Rate (%)'].mean().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(data=national_trend, x='Date', y='Estimated Unemployment Rate (%)', marker='o')
plt.axvline(pd.to_datetime('2020-03-24'), color='red', linestyle='--', label='COVID Lockdown Start')
plt.title('India Unemployment Rate Trend (National Average)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

covid_peak = df[(df['Date'] >= '2020-04-01') & (df['Date'] <= '2020-05-31')]
peak_avg = covid_peak.groupby('Region')['Estimated Unemployment Rate (%)'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=peak_avg.values, y=peak_avg.index, palette='coolwarm')
plt.title('Average Unemployment Rate by Region during COVID-19 Lockdown (Apr–May 2020)')
plt.xlabel('Unemployment Rate (%)')
plt.ylabel('Region')
plt.tight_layout()
plt.show()

df['Month'] = df['Date'].dt.month
monthly_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker='o')
plt.title('Monthly Average Unemployment Rate (Seasonal Pattern)')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(range(1,13))
plt.grid(True)
plt.tight_layout()
plt.show()