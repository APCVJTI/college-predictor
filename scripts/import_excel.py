import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# MySQL connection
username = "root"
password = quote_plus("Achyut@2006")
host = "localhost"
database = "college_predictor"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# Read Excel file
df = pd.read_excel("data/college_cutoffs_clean.xlsx")

print("Rows:", len(df))
print(df.head())

# Upload to MySQL
df.to_sql(
    "college_cutoffs",
    con=engine,
    if_exists="append",
    index=False
)

print("Data uploaded successfully!")