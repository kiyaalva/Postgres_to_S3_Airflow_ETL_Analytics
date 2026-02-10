import pandas as pd
from sqlalchemy import create_engine

# Connect to PostgreSQL
engine = create_engine("postgresql://postgres:kiya25@localhost/marketing_campaign")

# Load CSV
data = pd.read_csv('D:\K\RESUME\AWS\data\WA_Marketing_Campaign.csv')

# Convert data types if necessary
data['week'] = data['week'].astype(int)
data['SalesInThousands'] = data['SalesInThousands'].astype(float)

# Load into DB
data.to_sql('campaign_sales', engine, if_exists='replace', index=False)
