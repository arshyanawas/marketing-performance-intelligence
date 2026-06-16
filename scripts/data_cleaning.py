import pandas as pd
import os

# Create cleaned folder
os.makedirs("cleaned", exist_ok=True)


# Load Raw Files


campaign_performance = pd.read_csv(
    "data/campaign_performance.csv",
    encoding="cp1252"
)

campaign_meta = pd.read_csv(
    "data/campaign_meta.csv",
    encoding="cp1252"
)

channel_rates = pd.read_csv(
    "data/channel_rates.csv",
    encoding="cp1252"
)


# Rename Columns

campaign_performance.rename(columns={
    "Date": "campaign_date",
    "CampaignID": "campaign_id",
    "CampaignName": "campaign_name",
    "Platform": "platform",
    "TargetAudience": "target_audience",
    "Impressions": "impressions",
    "Clicks": "clicks",
    "Leads": "leads",
    "Applications": "applications",
    "Enrollments": "enrollments",
    "Cost (?)": "cost",
    "Revenue (?)": "revenue",
    "Region": "region"
}, inplace=True)

campaign_meta.rename(columns={
    "CampaignID": "campaign_id",
    "Objective": "objective",
    "StartDate": "start_date",
    "EndDate": "end_date",
    "Budget (?)": "budget",
    "Campaign Type": "campaign_type",
    "Creative Type": "creative_type",
    "Manager": "manager",
    "Channel": "channel",
    "Conversion Goal": "conversion_goal"
}, inplace=True)

channel_rates.rename(columns={
    "Channel": "channel",
    "AvgCPM": "avg_cpm",
    "AvgCPC": "avg_cpc",
    "Remarks": "remarks"
}, inplace=True)


# Convert Dates


campaign_performance["campaign_date"] = pd.to_datetime(
    campaign_performance["campaign_date"]
)

campaign_meta["start_date"] = pd.to_datetime(
    campaign_meta["start_date"]
)

campaign_meta["end_date"] = pd.to_datetime(
    campaign_meta["end_date"]
)


# Clean Currency Columns


for col in ["cost", "revenue"]:
    campaign_performance[col] = (
        campaign_performance[col]
        .astype(str)
        .str.replace("?", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
    )

    campaign_performance[col] = pd.to_numeric(
        campaign_performance[col]
    )

campaign_meta["budget"] = (
    campaign_meta["budget"]
    .astype(str)
    .str.replace("?", "", regex=False)
    .str.replace(",", "", regex=False)
    .str.strip()
)

campaign_meta["budget"] = pd.to_numeric(
    campaign_meta["budget"]
)


# Save Clean Files


campaign_performance.to_csv(
    "cleaned/campaign_performance_clean.csv",
    index=False
)

campaign_meta.to_csv(
    "cleaned/campaign_meta_clean.csv",
    index=False
)

channel_rates.to_csv(
    "cleaned/channel_rates_clean.csv",
    index=False
)

print("Cleaning completed successfully!")