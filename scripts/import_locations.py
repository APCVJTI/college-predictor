import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:Achyut%402006@localhost/college_predictor"
)

df = pd.read_excel("final_college_locations_clean.xlsx")

df.to_sql(
    "college_locations",
    engine,
    if_exists="replace",
    index=False
)

print("Locations imported successfully!")