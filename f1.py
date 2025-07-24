# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("f1_2024_results.csv")

# Preview the first few rows
print("HEAD OF DATAFRAME")
print(df.head())
print("\n")

# Print a summary of the dataframe (columns, non-null counts, dtypes)
print("DATAFRAME INFO")
df.info()
print("\n")

# Check for missing values in each column
print("MISSING VALUES CHECK")
print(df.isnull().sum())
print("\n")

# Get the number of unique races
num_races = df['Race'].nunique()
print("TOTAL RACES IN 2024:", num_races)
print("\n")

# Find the driver with the most wins
most_wins = df['Winner'].value_counts().head(1)
print("DRIVER WITH MOST WINS:")
print(most_wins)
print("\n")

# Group the dataset by team and sum up their points
team_points = df.groupby('Team')['Points'].sum().sort_values(ascending=False)
print("TOTAL POINTS BY TEAM:")
print(team_points)
print("\n")

# Plot a bar chart showing total points per team
plt.figure(figsize=(10, 5))
team_points.plot(kind='bar', color='dodgerblue', edgecolor='black')
plt.title('Total Points by Team (F1 2024 Season)', fontsize=14)
plt.ylabel("Total Points")
plt.xlabel("Team")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
