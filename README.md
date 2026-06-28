# Marketing Performance Intelligence Dashboard

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![SQL](https://img.shields.io/badge/SQL-SQLite-green?style=for-the-badge&logo=sqlite)
![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-Data_Source-217346?style=for-the-badge&logo=microsoft-excel)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=for-the-badge)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas)
![GitHub](https://img.shields.io/badge/GitHub-Portfolio_Project-black?style=for-the-badge&logo=github)

</p>

---

## Marketing Performance Intelligence Dashboard

An end-to-end **Marketing Analytics** project that transforms raw campaign data into actionable business intelligence through **Python**, **SQL**, **Power BI**, and **Exploratory Data Analysis**.

The project simulates the workflow of a Data Analyst working within a marketing team—starting from raw Excel files, performing data cleaning and transformation, conducting SQL-based business analysis, building analytical visualizations in Python, and finally delivering an executive Power BI dashboard for decision-makers.

Instead of focusing only on descriptive reporting, this project identifies:

- Campaign profitability
- Customer acquisition efficiency
- Marketing funnel leakage
- Platform-wise ROI
- Regional performance
- Cost optimization opportunities
- Revenue generation trends

The final deliverable demonstrates how marketing data can be converted into strategic insights that support data-driven business decisions.

---

## Dashboard Preview

### Executive Dashboard

> **Image Placeholder**

```text
images/powerbi/dashboard_page1.png
```

---

### Marketing Performance Dashboard

> **Image Placeholder**

```text
images/powerbi/dashboard_page2.png
```

---

### Platform Performance Dashboard

> **Image Placeholder**

```text
images/powerbi/dashboard_page3.png
```

---

## Project Highlights

| Feature | Description |
|----------|-------------|
| End-to-End Analytics Pipeline | Complete workflow from raw Excel data to executive dashboard |
| Data Cleaning | Python-based preprocessing and standardization |
| SQL Business Analysis | Multiple analytical SQL queries solving real marketing problems |
| Exploratory Data Analysis | Professional visualizations using Matplotlib |
| Interactive Dashboard | Multi-page Power BI dashboard with slicers and KPIs |
| Marketing KPI Tracking | ROI, Cost per Enrollment, Funnel Leakage, Revenue, Applications, Enrollments and more |
| Business Recommendations | Actionable insights for improving marketing performance |
| Portfolio Ready | Structured as a real-world analytics case study suitable for recruiters |

---

> **Project Goal**
>
> Build a comprehensive Marketing Intelligence solution that enables stakeholders to evaluate campaign performance, identify revenue opportunities, optimize acquisition costs, and improve marketing effectiveness using modern analytics tools.

# Project Overview

## Introduction

Marketing teams invest significant budgets across multiple digital platforms with the expectation of generating quality leads, customer applications, and successful enrollments. However, without a structured analytics framework, it becomes difficult to answer critical business questions such as:

- Which platform generates the highest return on investment?
- Where is the marketing funnel losing the most potential customers?
- Which campaigns deserve additional investment?
- Which regions consistently outperform others?
- Are marketing costs translating into profitable revenue?

This project addresses these questions by developing an end-to-end Marketing Performance Intelligence Dashboard that combines data engineering, exploratory analysis, SQL-based business reporting, and interactive dashboarding into a single analytics solution.

The workflow mirrors a real-world business intelligence project, beginning with raw marketing campaign data stored in Excel and progressing through data cleaning, database creation, SQL analysis, Python visualizations, and an executive-level Power BI dashboard.

---

## Project Scope

The project analyzes marketing campaign performance across multiple dimensions, including:

- Marketing platforms
- Campaigns
- Geographic regions
- Customer acquisition funnel
- Marketing expenditure
- Revenue generation
- Conversion performance

By integrating these perspectives, the dashboard enables stakeholders to monitor campaign effectiveness, evaluate marketing efficiency, and identify areas for optimization.

---

## Key Business Questions

The analysis is designed to answer several business-critical questions:

| Business Question | Analytical Approach |
|-------------------|---------------------|
| Which marketing platform generates the highest revenue? | Platform-wise revenue analysis |
| Which campaigns deliver the best ROI? | ROI calculation and campaign ranking |
| Which region contributes the most revenue? | Regional performance analysis |
| How efficiently are leads converted into enrollments? | Funnel conversion analysis |
| Where does the largest customer drop-off occur? | Funnel leakage calculation |
| Which campaigns have the highest acquisition cost? | Cost per Enrollment analysis |
| Which platforms produce the highest enrollment yield? | Enrollment Yield Ratio calculation |
| How does campaign spending compare with generated revenue? | Cost vs Revenue comparison |

---

## End-to-End Analytics Pipeline

This project follows a structured analytics workflow commonly used in industry.

```text
Raw Excel Dataset
        │
        ▼
Python Data Cleaning
(Pandas)
        │
        ▼
Cleaned CSV Files
        │
        ▼
SQLite Database
        │
        ▼
SQL Business Analysis
        │
        ▼
Exploratory Data Analysis
(Matplotlib)
        │
        ▼
Power BI Dashboard
        │
        ▼
Business Insights &
Strategic Recommendations
```

---

## Deliverables

The repository includes the complete analytics pipeline, including:

| Deliverable | Description |
|-------------|-------------|
| Cleaned Datasets | Preprocessed marketing data ready for analysis |
| Python Scripts | Data cleaning and EDA workflows |
| SQLite Database | Structured relational database for SQL analysis |
| SQL Scripts | Business-oriented analytical queries |
| Matplotlib Visualizations | Exploratory charts highlighting campaign performance |
| Power BI Dashboard | Interactive dashboard with KPIs, filters, and drill-down analysis |
| Business Insights | Key findings derived from data analysis |
| Strategic Recommendations | Data-driven recommendations for marketing optimization |

---

## Expected Business Value

The Marketing Performance Intelligence Dashboard helps stakeholders:

- Monitor overall marketing performance from a single dashboard.
- Compare campaign effectiveness across multiple advertising platforms.
- Identify underperforming campaigns before additional budget is allocated.
- Detect inefficiencies within the customer acquisition funnel.
- Optimize marketing spend by focusing on high-performing channels.
- Support strategic decision-making using data-driven performance metrics.
- Improve return on investment through actionable business insights.

---

> **Case Study Focus**
>
> Rather than presenting isolated charts or SQL queries, this project demonstrates a complete analytics solution that reflects the responsibilities of a Data Analyst—from data preparation and business analysis to executive reporting and strategic decision support.

## Part 3 — Business Problem

````markdown id="opgqzu"
# Business Problem

## Background

Modern organizations invest substantial marketing budgets across multiple digital channels such as Google Ads, Facebook, Instagram, LinkedIn, and YouTube to attract potential customers. While these campaigns generate large volumes of impressions, clicks, and leads, measuring their true business impact requires more than surface-level reporting.

Marketing teams often have access to operational data but lack a unified analytics solution that connects campaign performance with business outcomes such as applications, enrollments, revenue, and return on investment.

Without meaningful analysis, organizations risk allocating budgets based on assumptions rather than evidence, resulting in inefficient spending and missed growth opportunities.

---

## Business Challenges

The organization needs to answer several critical questions before making future marketing investments.

### 1. Budget Allocation

Marketing spend is distributed across multiple advertising platforms, but it is unclear which channels consistently generate profitable outcomes.

Questions include:

- Which platform provides the highest return on investment?
- Which campaigns justify additional investment?
- Which channels consume budget without delivering proportional revenue?

---

### 2. Customer Funnel Inefficiencies

A customer progresses through several stages before becoming an enrolled customer.

```text
Impressions
      ↓
Clicks
      ↓
Leads
      ↓
Applications
      ↓
Enrollments
```

At each stage, potential customers are lost.

The business lacks visibility into:

- Where the largest customer drop-offs occur.
- Which stages require optimization.
- How efficiently leads are converted into enrollments.

Understanding funnel leakage is essential for improving conversion rates and maximizing marketing effectiveness.

---

### 3. Campaign Performance Comparison

Not all campaigns perform equally.

Some campaigns may:

- Generate high impressions but very few conversions.
- Produce many leads with low enrollment rates.
- Deliver excellent ROI despite lower spending.
- Achieve strong revenue with relatively modest budgets.

The business requires a standardized framework for comparing campaigns using consistent performance metrics.

---

### 4. Regional Performance Differences

Marketing campaigns target multiple geographic regions.

Management wants to understand:

- Which regions generate the highest revenue.
- Which regions deliver the strongest enrollment performance.
- Whether marketing investments should be redistributed geographically.
- Where additional growth opportunities exist.

---

### 5. Rising Customer Acquisition Costs

Increasing marketing expenditure does not always translate into higher enrollments.

Without monitoring acquisition costs, organizations may unknowingly spend more to acquire each customer while reducing overall profitability.

The business therefore needs to evaluate:

- Cost per Enrollment (CPE)
- Revenue generated relative to marketing spend
- Campaign profitability
- Marketing efficiency across platforms

---

## Why This Project Was Needed

The existing reporting process provided isolated performance metrics but lacked a consolidated view of marketing effectiveness.

Decision-makers required an analytics solution capable of:

- Consolidating marketing data into a single source of truth.
- Tracking key marketing KPIs in real time.
- Identifying high-performing and underperforming campaigns.
- Measuring conversion efficiency throughout the customer journey.
- Supporting strategic budgeting decisions with quantitative evidence.

To address these needs, this project develops a complete Marketing Performance Intelligence Dashboard that integrates data preparation, SQL analytics, visualization, and interactive business intelligence reporting.

---

## Business Impact

By implementing this analytics solution, stakeholders can:

| Business Need | Analytical Solution |
|---------------|---------------------|
| Improve marketing ROI | Compare revenue against campaign costs across platforms |
| Optimize budget allocation | Identify the highest-performing campaigns and channels |
| Reduce funnel leakage | Analyze conversion rates at every stage of the customer journey |
| Increase operational efficiency | Monitor key KPIs through an interactive dashboard |
| Support strategic planning | Use data-driven insights for future marketing decisions |
| Enhance regional performance | Evaluate campaign effectiveness across different regions |

---

## Problem Statement

The organization lacks a centralized analytics framework to evaluate marketing campaign performance across platforms, regions, and customer acquisition stages. As a result, marketing decisions are made with limited visibility into campaign profitability, funnel efficiency, and return on investment.

This project addresses the problem by building an end-to-end Marketing Performance Intelligence Dashboard that transforms raw marketing data into actionable insights through Python, SQL, Matplotlib, and Power BI, enabling stakeholders to make informed, data-driven decisions.
````
