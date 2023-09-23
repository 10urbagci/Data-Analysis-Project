import pandas as pd

df = pd.read_csv("data.csv")

# drop city column
df.drop('city', axis=1, inplace=True)

print(df.columns)

# Update CSV file
df.to_csv("measurements1_updated.csv", index=False)
