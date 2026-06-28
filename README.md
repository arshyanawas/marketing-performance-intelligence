# Marketing Performance Intelligence Dashboard

<p align="center">

![Python](https://img.shields.io/badge/Python-Data%20Engineering-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![SQL](https://img.shields.io/badge/SQL-Business%20Intelligence-F29111?style=for-the-badge)
![Power BI](https://img.shields.io/badge/Power%20BI-Executive%20Dashboard-F2C811?style=for-the-badge&logo=powerbi)
![Matplotlib](https://img.shields.io/badge/Matplotlib-EDA-11557C?style=for-the-badge)

</p>

<p align="center">
<b>An end-to-end marketing analytics solution that transforms raw campaign data into actionable business intelligence using Python, SQLite, SQL, Matplotlib, and Power BI.</b>
</p>

---

## Executive Summary

Marketing teams can usually access impressions, clicks, and advertising spend for individual platforms. Understanding which campaigns are actually profitable across multiple platforms — and where marketing investment creates the greatest business value — is the harder challenge.

This project builds an end-to-end analytics workflow that transforms raw marketing campaign data into executive-ready insights. Starting with Python-based data preparation, the workflow progresses through SQL business intelligence and exploratory analysis before culminating in an interactive Power BI dashboard for decision-makers.

Rather than reporting isolated metrics, the analysis evaluates the complete customer acquisition journey across **Google Ads, Facebook, Instagram, LinkedIn, and YouTube**, measuring revenue generation, marketing efficiency, conversion performance, regional trends, and funnel behavior.

---

## Executive Dashboard

<p align="center">
<img src="images/powerbi/page1-executive-overview.png" width="100%">
</p>

At a glance, the dashboard answers the questions that matter most to marketing leaders: **Where is revenue coming from? Which channels are the most efficient? Where are potential customers dropping off?**

### Project Highlights

| Metric | Result |
|---|---:|
| Total Revenue | ₹2.165 Billion |
| Marketing Spend | ₹91.4 Million |
| Revenue-to-Spend Ratio | **22.68×** |
| Applications | 784K |
| Enrollments | 392K |
| Revenue per Lead | ₹1.52K |
| Enrollment Yield | 50.06% |
| Highest Revenue Platform | Google Ads |
| Highest ROI Platform | LinkedIn |
| Largest Funnel Drop | Impression → Click |
| Best Performing Region | Pan India |

> **Note:** The Revenue-to-Spend Ratio reflects the characteristics of the provided dataset and is intended for comparing platform efficiency *within this project*, rather than representing real-world industry benchmark performance.

---

## Business Context

Marketing budgets are rarely limited to a single advertising channel. Organizations invest across multiple platforms, each targeting different audiences, regions, and campaign objectives.

Without a unified analytics framework, answering questions such as **which platform deserves more investment** or **where the customer acquisition process is breaking down** becomes difficult. Traditional reporting often looks at isolated metrics — impressions here, conversions there — without connecting the full journey from first exposure to final enrollment alongside the financial picture.

This project addresses that gap by combining operational, financial, and conversion metrics into a single business intelligence solution that supports evidence-based marketing decisions.

## Business Objectives

The project was designed to answer a focused set of business questions:

- Which platform generates the highest revenue, and which delivers the strongest return on investment?
- Which campaigns and regions contribute most to business growth?
- Where does the largest customer drop-off occur in the acquisition funnel?
- Which audience segments generate the highest-value leads?
- Is marketing spend being used efficiently?

These questions drive every stage of the analysis — from SQL queries to dashboard design — ensuring the outputs stay focused on business decisions rather than technical metrics for their own sake.

---

## Solution Architecture

```text
                 Raw Marketing Data
                         │
                         ▼
              Python Data Engineering
        (Cleaning • Validation • Transformation)
                         │
                         ▼
                  SQLite Database
                         │
                         ▼
             SQL Business Intelligence
                         │
          ┌──────────────┴──────────────┐
          ▼                             ▼
 Exploratory Data Analysis      Power BI Dashboard
      (Matplotlib)           Executive Decision Support
          └──────────────┬──────────────┘
                         ▼
             Business Insights & Recommendations
```

The project follows the same workflow used in many analytics teams: clean the data, structure it for analysis, answer business questions with SQL, validate findings visually, and deliver them through an executive dashboard.

### Analytics Stack

| Technology | Purpose |
|---|---|
| **Python** | Data cleaning, preprocessing, and validation |
| **Pandas & NumPy** | Data transformation and feature preparation |
| **SQLite** | Centralized analytical database |
| **SQL** | KPI calculation and business intelligence |
| **Matplotlib** | Exploratory data analysis and trend visualization |
| **Power BI** | Interactive executive dashboard |
| **Git & GitHub** | Version control and project documentation |

---

## Data Assets

The project is built on three complementary datasets that capture campaign performance, campaign metadata, and platform benchmarks.

| Dataset | Description | Records |
|---|---|---:|
| `campaign_performance.csv` | Impressions, clicks, leads, applications, enrollments, cost, revenue, platform, audience, and region | 763 |
| `campaign_meta.csv` | Campaign objectives, budgets, campaign type, creative type, manager, and conversion goals | 5 |
| `channel_rates.csv` | Average CPC and CPM benchmarks for each marketing platform | 5 |

The combined dataset covers five digital marketing platforms, five geographic regions, multiple audience segments, and the complete customer acquisition funnel — from first impression to final enrollment.

### Data Engineering Pipeline

Reliable analytics begins with reliable data. Before any SQL analysis or dashboard development, the raw datasets were cleaned and standardized using Python:

- Standardizing column names and data types
- Converting currency-formatted fields into numeric values
- Removing duplicate and inconsistent records
- Validating categorical values across platforms and regions
- Preparing clean datasets for SQLite and Power BI

```text
Raw CSV Files → Data Cleaning & Validation → Data Transformation
   → Cleaned CSV Files → SQLite Database → SQL Analysis & Power BI
```

This pipeline ensured that every KPI, visualization, and dashboard was generated from consistent and validated data.

---

## Exploratory Data Analysis

EDA was performed using Matplotlib to surface trends and validate assumptions before building the SQL models and Power BI dashboards — this stage is about identifying what's worth investigating further, not drawing final conclusions.

### Revenue by Platform

<p align="center">
<img src="images/matplotlib/revenue_by_platform.png" width="90%">
</p>

Google Ads emerged as the largest revenue-generating platform at **₹532M**, closely followed by Facebook at **₹517M** — together, nearly **49%** of total revenue. YouTube generated the smallest share, suggesting its strength lies in awareness rather than direct conversion.

### Cost vs. Revenue

<p align="center">
<img src="images/matplotlib/cost_vs_revenue_platform.png" width="90%">
</p>

Every platform generated substantially more revenue than marketing spend, indicating strong overall campaign profitability. More interesting: **the platform generating the highest revenue was not the platform generating the highest return** — a gap that became the starting point for the profitability analysis in the SQL section below.

### Regional Revenue Distribution

<p align="center">
<img src="images/matplotlib/revenue_by_region.png" width="90%">
</p>

Pan India campaigns produced the highest revenue, followed by North and West India. Conversion performance stayed relatively consistent across regions, suggesting campaign **scale** — not campaign **quality** — was the main driver of regional differences.

### Revenue-to-Spend Ratio by Platform

<p align="center">
<img src="images/matplotlib/roi_by_platform.png" width="90%">
</p>

LinkedIn achieved the strongest Revenue-to-Spend Ratio at **24.45×**, followed by Instagram at **23.01×** — despite Google Ads generating more total revenue. Marketing scale and marketing efficiency aren't always the same thing.

### Top Revenue-Generating Campaigns

<p align="center">
<img src="images/matplotlib/top_campaigns_revenue.png" width="90%">
</p>

Admission-focused campaigns dominated overall performance: **UG Admission** generated the highest revenue, followed by **MBA Admission** — together representing the strongest commercial opportunity in the portfolio.

### Key Observations from EDA

- Google Ads is the primary revenue driver
- LinkedIn delivers the highest marketing efficiency
- Pan India campaigns outperform individual regions
- Admission-focused campaigns generate the largest business impact
- Revenue consistently exceeds marketing spend across every platform

These observations set the agenda for the SQL-based business intelligence layer that follows.

---

## Business Intelligence Analysis

With the data prepared and validated, SQL was used to quantify and confirm the EDA observations with measurable KPIs — combining aggregations, CTEs, conditional logic, and ranking functions to turn campaign-level records into executive-ready answers.

### Business Questions Answered

| Business Question | Key Finding | Business Impact |
|---|---|---|
| Which platform generated the highest revenue? | Google Ads generated **₹532M** | Continue investing in the strongest revenue channel while monitoring cost efficiency |
| Which platform delivered the highest marketing efficiency? | LinkedIn achieved the highest Revenue-to-Spend Ratio at **24.45×** | Allocate additional budget to campaigns targeting professional audiences |
| Which platform generated the highest-value leads? | LinkedIn recorded the highest Revenue per Lead at **₹1.59K** | Prioritize lead quality alongside lead volume |
| Where does the largest customer drop-off occur? | Impression → Click conversion sits at just **~5.5%** | Improve creatives, targeting, and CTAs to increase engagement |
| Which campaign generated the greatest business value? | UG Admission ranked first in total revenue | Replicate successful campaign strategies across future admissions campaigns |
| Which region performed best? | Pan India generated the highest revenue | Prioritize high-performing markets while expanding lower-performing regions strategically |
| Is marketing spend being used efficiently? | Spend Waste Ratio sits at **4–5%** | Maintain current budget discipline while monitoring underperforming campaigns |

### Representative SQL Query

The project includes several analytical SQL scripts covering revenue analysis, campaign rankings, funnel performance, enrollment yield, and platform benchmarking. A representative example:

<details>
<summary><strong>View SQL Query — Revenue-to-Spend Ratio by Platform</strong></summary>

```sql
WITH PlatformPerformance AS (
    SELECT
        platform,
        SUM(revenue) AS total_revenue,
        SUM(cost) AS total_cost,
        ROUND(SUM(revenue) / SUM(cost), 2) AS revenue_to_spend_ratio
    FROM campaign_performance
    GROUP BY platform
)

SELECT
    platform,
    total_revenue,
    total_cost,
    revenue_to_spend_ratio
FROM PlatformPerformance
ORDER BY revenue_to_spend_ratio DESC;
```

</details>

### Funnel Analysis

| Stage | Volume |
|---|---:|
| Impressions | 129.15M |
| Clicks | 7.14M |
| Leads | 1.42M |
| Applications | 784K |
| Enrollments | 392K |

| Transition | Conversion Rate |
|---|---:|
| Impression → Click | ~5.5% (CTR) |
| Click → Lead | ~19.9% |
| Lead → Application | ~55.2% |
| Application → Enrollment | ~50.0% |

The largest customer loss occurs at the very top of the funnel — only ~5.5% of impressions become clicks. Every later stage converts at 20%+, meaning the single highest-leverage fix is improving ad creatives and targeting to lift CTR, not optimizing the back half of the journey.

### Audience Insights

| Platform | Best-Performing Audience |
|---|---|
| Google Ads | 21–35 years |
| Facebook | 17–21 years |
| Instagram | Mixed (17–21, 22–27, 25–35) |
| LinkedIn | 22–27 & 25–35 years |
| YouTube | Broadly distributed across age groups |

Audience composition varies meaningfully by platform, supporting tailored, platform-specific targeting rather than a single standardized strategy.

### Engagement Stability

CTR held steady across the year (roughly 5.3–5.9%), and enrollment conversion stayed close to 50% throughout — no sustained downward trend, suggesting campaigns maintained engagement without significant fatigue.

### SQL Analysis Deliverables

The SQL layer produced a set of reusable business intelligence reports, each backed by reproducible logic rather than manual calculation:

- Revenue by Platform
- Revenue-to-Spend Ratio Analysis
- Cost per Enrollment
- Enrollment Yield Analysis
- Customer Funnel Leakage
- Campaign Performance Ranking
- Regional Performance Ranking
- Platform Performance Summary

These outputs formed the direct foundation for every KPI and visual in the Power BI dashboard below.

---

## Executive Decision Dashboard

The final phase translates the analytical findings into an interactive four-page Power BI dashboard for stakeholders, with filters and slicers to explore performance by platform, campaign, audience, and region.

| Dashboard Page | Purpose |
|---|---|
| Executive Overview | Monitor overall marketing performance and top-line KPIs |
| Funnel Analysis | Evaluate acquisition efficiency and conversion leakage |
| Platform Performance | Compare channels and drill into individual platform detail |
| Campaign Optimization | Surface optimization opportunities and budget allocation guidance |

### Platform Performance Summary

<p align="center">
<img src="images/powerbi/page3-overview.png" width="100%">
</p>

| Platform | Primary Strength |
|---|---|
| Google Ads | Highest total revenue (₹532M) |
| Facebook | Strong revenue with balanced efficiency (₹517M) |
| Instagram | Strong profitability, competitive conversion (23.01× ROI) |
| LinkedIn | Highest Revenue-to-Spend Ratio, Revenue per Lead, and Enrollment Yield |
| YouTube | Awareness-focused; lowest direct conversion performance |

### Funnel & Optimization Dashboard

<p align="center">
<img src="images/powerbi/page2-funnel-analysis.png" width="100%">
</p>

The funnel and optimization pages translate the SQL findings above into a filterable view: drop-off by platform, region, and audience, alongside the spend-efficiency metrics needed to act on them.

---

## Strategic Recommendations

| Finding | Recommendation |
|---|---|
| Google Ads generates the most revenue | Continue investing while optimizing CPC to improve ROI |
| LinkedIn delivers the highest ROI, revenue per lead, and enrollment yield | Increase investment in high-value B2B and professional campaigns |
| YouTube has the lowest revenue, ROI, and enrollment yield | Reposition YouTube for awareness and remarketing rather than direct conversion |
| Largest funnel leakage is at Impression → Click | Improve creatives, targeting, and CTAs to lift CTR |
| Admissions campaigns dominate revenue | Expand and replicate successful admission-focused campaign strategies |
| Regional performance varies, conversion quality doesn't | Allocate budget dynamically based on regional ROI and revenue, not just reach |
| Spend Waste Ratio remains low (4–5%) | Maintain current budget discipline while continuously monitoring efficiency |

---

## Skills Demonstrated

**Data Engineering** — Data cleaning, validation, transformation, feature preparation, quality assessment

**Database & SQL** — SQLite database design, aggregations, CTEs, ranking functions, KPI development, BI queries

**Data Analytics** — EDA, funnel analysis, regional and platform benchmarking, conversion analysis

**Data Visualization** — Matplotlib, KPI reporting, executive dashboards, data storytelling

**Business Intelligence** — Revenue and profitability analysis, conversion optimization, performance benchmarking, executive reporting

**Tools** — Python, Pandas, NumPy, SQLite, SQL, Matplotlib, Power BI, Git, GitHub

---

## Repository Structure

```text
marketing-performance-intelligence/
│
├── data/
│   ├── campaign_performance.csv
│   ├── campaign_meta.csv
│   └── channel_rates.csv
│
├── cleaned/
│   ├── campaign_performance_clean.csv
│   ├── campaign_meta_clean.csv
│   └── channel_rates_clean.csv
│
├── database/
│   └── marketing.db
│
├── scripts/
│   ├── data_cleaning.py
│   ├── load_data.py
│   └── eda.py
│
├── analysis/
│   ├── benchmark_cpc_comparison.sql
│   ├── campaign_ranking.sql
│   ├── cost_per_enrollment.sql
│   ├── enrollment_yield_ratio.sql
│   ├── funnel_leakage_rate.sql
│   ├── platform_performance_summary.sql
│   ├── regional_performance_ranking.sql
│   └── roi_by_platform.sql
│
├── images/
│   ├── matplotlib/
│   └── powerbi/
│
├── README.md
└── requirements.txt
```

## Getting Started

```bash
git clone https://github.com/arshyanawas/marketing-performance-intelligence.git
cd marketing-performance-intelligence
pip install -r requirements.txt

python scripts/data_cleaning.py
python scripts/load_data.py
python scripts/eda.py
```

Then open the Power BI report to explore the interactive dashboards.

## Future Enhancements

- Model expected enrollment yield by campaign, region, and audience segment to flag underperforming combinations before spend is fully committed
- Automated ETL with scheduled refreshes instead of manual script runs
- Marketing attribution analysis across multi-touch customer journeys
- Cloud-based data warehouse for larger, multi-year datasets

---

## Author

**Arshya Nawas**
Data Analyst | Business Intelligence | Python | SQL | Power BI

[GitHub](https://github.com/arshyanawas) · [Repository](https://github.com/arshyanawas/marketing-performance-intelligence) · [LinkedIn](https://www.linkedin.com/in/arshyanawas) · [arshyanawas.ai@gmail.com](mailto:arshyanawas.ai@gmail.com)

---

*This project was built to demonstrate an end-to-end analytics workflow — Python data engineering, SQL business intelligence, and Power BI dashboarding — that mirrors how real marketing analytics teams turn raw campaign data into decisions. Feel free to explore the SQL files, interact with the dashboards, or reach out to discuss the analysis.*
