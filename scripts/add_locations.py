import pandas as pd

df = pd.read_csv("college_names.csv")

print("Total Colleges:", len(df))

for i, college in enumerate(df["college_name"], start=1):
    print(f"{i}. {college}")