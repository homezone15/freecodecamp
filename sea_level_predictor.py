import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the dataset
df = pd.read_csv("epa-sea-level.csv")

# Create scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

# First line of best fit (1880 to latest)
res_full = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_full = pd.Series(range(1880, 2051))
y_full = res_full.intercept + res_full.slope * x_full
plt.plot(x_full, y_full, 'r', label='Fit: 1880–2050')

# Second line of best fit (2000 to latest)
df_recent = df[df['Year'] >= 2000]
res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
x_recent = pd.Series(range(2000, 2051))
y_recent = res_recent.intercept + res_recent.slope * x_recent
plt.plot(x_recent, y_recent, 'g', label='Fit: 2000–2050')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
