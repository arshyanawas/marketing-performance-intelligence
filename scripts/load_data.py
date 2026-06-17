import pandas as pd
import sqlite3

# Connect to SQLite


conn = sqlite3.connect("database/marketing.db")

# Load Cleaned CSV Files

campaign_performance = pd.read_csv(
    "cleaned/campaign_performance_clean.csv"
)

campaign_meta = pd.read_csv(
    "cleaned/campaign_meta_clean.csv"
)

channel_rates = pd.read_csv(
    "cleaned/channel_rates_clean.csv"
)


# Load into SQLite


campaign_performance.to_sql(
    "campaign_performance",
    conn,
    if_exists="replace",
    index=False
)

campaign_meta.to_sql(
    "campaign_meta",
    conn,
    if_exists="replace",
    index=False
)

channel_rates.to_sql(
    "channel_rates",
    conn,
    if_exists="replace",
    index=False
)


# Validation

print("Campaign Performance Rows:",
      pd.read_sql_query(
          "SELECT COUNT(*) AS total FROM campaign_performance",
          conn
      ))

print("\nCampaign Meta Rows:",
      pd.read_sql_query(
          "SELECT COUNT(*) AS total FROM campaign_meta",
          conn
      ))

print("\nChannel Rates Rows:",
      pd.read_sql_query(
          "SELECT COUNT(*) AS total FROM channel_rates",
          conn
      ))

conn.close()

print("\nData loaded successfully!")