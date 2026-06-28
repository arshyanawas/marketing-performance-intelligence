import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


# Load Data


df = pd.read_csv("../cleaned/campaign_performance_clean.csv")

# Create output folder
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)


# 1. Revenue by Platform


platform_revenue = (
    df.groupby("platform")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
platform_revenue.plot(kind="bar")
plt.title("Revenue by Platform")
plt.xlabel("Platform")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(output_dir / "revenue_by_platform.png")
plt.close()



# 2. Cost vs Revenue by Platform


platform_metrics = (
    df.groupby("platform")[["cost", "revenue"]]
    .sum()
    .sort_values("revenue", ascending=False)
)

plt.figure(figsize=(8,5))

x = range(len(platform_metrics))

plt.bar(
    [i - 0.2 for i in x],
    platform_metrics["cost"],
    width=0.4,
    label="Cost"
)

plt.bar(
    [i + 0.2 for i in x],
    platform_metrics["revenue"],
    width=0.4,
    label="Revenue"
)

plt.xticks(x, platform_metrics.index)
plt.title("Cost vs Revenue by Platform")
plt.xlabel("Platform")
plt.ylabel("Amount")
plt.legend()

plt.tight_layout()
plt.savefig(output_dir / "cost_vs_revenue_platform.png")
plt.close()


# 3. ROI by Platform


roi_df = (
    df.groupby("platform")[["revenue", "cost"]]
    .sum()
)

roi_df["roi"] = (
    (roi_df["revenue"] - roi_df["cost"])
    / roi_df["cost"]
) * 100

roi_df = roi_df.sort_values("roi", ascending=False)

plt.figure(figsize=(8,5))
plt.bar(roi_df.index, roi_df["roi"])
plt.title("ROI by Platform")
plt.xlabel("Platform")
plt.ylabel("ROI (%)")
plt.tight_layout()
plt.savefig(output_dir / "roi_by_platform.png")
plt.close()


# 4. Revenue by Region


region_revenue = (
    df.groupby("region")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8,5))
region_revenue.plot(kind="bar")
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig(output_dir / "revenue_by_region.png")
plt.close()


# 5. Top 5 Campaigns by Revenue


campaign_revenue = (
    df.groupby("campaign_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(8,5))
campaign_revenue.sort_values().plot(kind="barh")
plt.title("Top 5 Campaigns by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Campaign")
plt.tight_layout()
plt.savefig(output_dir / "top_campaigns_revenue.png")
plt.close()


# Success Message


print("\nVisualization files created successfully!\n")
print("Saved to:")
print(output_dir.resolve())