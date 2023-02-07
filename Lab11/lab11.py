import pandas as pd

# Read the dataset into a Pandas DataFrame
data = pd.read_csv("owid-covid-data.csv")

# Group the data by "continent" and calculate the sum of new cases and total deaths for each continent
grouped = data.groupby("continent").agg({"new_cases": "sum", "total_deaths": "sum"})

# Print the result
print(grouped)
