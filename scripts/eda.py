import pandas as pd

# Load CSV Files
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
# Profiling Function

def profile_dataframe(df, name):

    print("\n" + "=" * 60)
    print(name.upper())
    print("=" * 60)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nFirst 5 Rows:")
    print(df.head())

# Run Profiling

profile_dataframe(
    campaign_performance,
    "Campaign Performance"
)

profile_dataframe(
    campaign_meta,
    "Campaign Meta"
)

profile_dataframe(
    channel_rates,
    "Channel Rates"
)

print("\nUnique Platforms:")
print(campaign_performance["Platform"].unique())

print("\nUnique Regions:")
print(campaign_performance["Region"].unique())

print("\nUnique Target Audiences:")
print(campaign_performance["TargetAudience"].unique())

print("\nSample Cost Values:")
print(campaign_performance["Cost (?)"].head())

print("\nSample Revenue Values:")
print(campaign_performance["Revenue (?)"].head())

print("\nSample Budget Values:")
print(campaign_meta["Budget (?)"].head())