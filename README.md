# Forecasting Financial Inclusion in Ethiopia

> **10 Academy – Artificial Intelligence Mastery**
>
> **Week 11 Challenge**
>
> **Tasks 1 & 2: Data Exploration, Enrichment, and Exploratory Data Analysis**
>
> **Student:** Lalise Fufi

---

# Project Overview

Financial inclusion plays a critical role in economic development by enabling individuals and businesses to access formal financial services. Ethiopia has experienced rapid growth in digital financial services through innovations such as **Telebirr**, **M-Pesa Ethiopia**, **Fayda Digital ID**, and expanding telecommunications infrastructure. However, despite these developments, financial account ownership and digital payment adoption remain below global averages.

This project was completed as part of the **10 Academy Artificial Intelligence Mastery – Week 11 Challenge**. The objective is to build the foundation for a forecasting system capable of predicting Ethiopia's financial inclusion trends by first understanding, exploring, and enriching the provided unified financial inclusion dataset.

---

# Business Problem

Selam Analytics has been commissioned by a consortium of stakeholders—including the National Bank of Ethiopia, development finance institutions, and mobile money operators—to develop a forecasting system that predicts Ethiopia's financial inclusion progress.

The forecasting system aims to answer the following questions:

- What factors drive financial inclusion in Ethiopia?
- How do policies, infrastructure investments, and product launches affect financial inclusion?
- How will Access and Usage indicators evolve during 2025–2027?

The primary forecasting targets are:

- **Access:** Account Ownership Rate
- **Usage:** Digital Payment Adoption Rate

---

# Objectives

The objectives of Task 1 are to:

- Understand the unified financial inclusion dataset.
- Explore the dataset structure and schema.
- Assess data quality.
- Analyze observations, events, and impact relationships.
- Enrich the dataset with additional records useful for forecasting.
- Save analysis-ready datasets for subsequent modeling tasks.
- Perform comprehensive exploratory data analysis.
- Identify drivers of financial inclusion.
- Analyze infrastructure, events, and usage patterns.
- Generate insights to support forecasting.

---

# Repository Structure

```text
ethiopia-fi-forecast-week11/
│
├── .github/
│   └── workflows/
│
├── data/
│   ├── raw/
│   │   ├── ethiopia_fi_unified_data.xlsx
│   │   ├── reference_codes.csv
│   │
│   └── processed/
│       ├── ethiopia_fi_enriched.csv
│       └── impact_links_enriched.csv
│
├── notebooks/
│   └── Task_1_Data_Exploration.ipynb
│   └── Task_2_Exploratory_Data_Analysis.ipynb
│     
│
├── reports/
│   └── figures/
│
├── docs/
│   └── data_enrichment_log.md
│
├── src/
│
├── tests/
│
├── requirements.txt
│
└── README.md
```

---

# Dataset Description

The starter dataset follows a **unified schema**, where every record shares the same columns while the `record_type` field determines how each row should be interpreted.

The dataset contains four record types:

| Record Type | Description |
|-------------|-------------|
| Observation | Quantitative financial inclusion measurements |
| Event | Policies, product launches, milestones, infrastructure developments |
| Impact Link | Relationships connecting events with indicators |
| Target | Official financial inclusion targets |

The dataset is accompanied by:

- `reference_codes.csv`
- Schema documentation
- Data enrichment guide

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git
- GitHub

---

# Installation

Clone the repository.

```bash
git clone https://github.com/<username>/ethiopia-fi-forecast-week11.git

cd ethiopia-fi-forecast-week11
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

# Project Workflow

Task 1 follows the workflow below.

```text
Load Dataset
      │
      ▼
Understand Schema
      │
      ▼
Data Quality Assessment
      │
      ▼
Observation Analysis
      │
      ▼
Event Analysis
      │
      ▼
Impact Link Analysis
      │
      ▼
Relationship Analysis
      │
      ▼
Data Enrichment
      │
      ▼
Save Processed Dataset
```

---

# Task 1 Implementation

## 1. Data Loading

Loaded:

- Unified Financial Inclusion Dataset
- Impact Links Sheet
- Reference Codes

The Excel workbook contains:

- **ethiopia_fi_unified_data**
- **Impact_sheet**

Reference codes were loaded from:

```
reference_codes.csv
```

---

## 2. Schema Understanding

The unified schema contains **34 common fields** shared across every record type.

Key fields include:

- record_id
- record_type
- pillar
- indicator
- indicator_code
- observation_date
- source_name
- confidence
- impact_direction
- relationship_type
- notes

---

## 3. Dataset Exploration

The dataset consists of:

| Record Type | Count |
|-------------|------:|
| Observation | 30 |
| Event | 10 |
| Target | 3 |

Total records:

**43**

---

### Financial Inclusion Pillars

- ACCESS
- USAGE
- GENDER
- AFFORDABILITY

---

### Source Types

The data originates from:

- Operators
- Surveys
- Regulators
- Research publications
- Policy documents
- Calculated metrics
- News sources

---

### Confidence Levels

The majority of records have **High confidence**, indicating that most values originate from reliable official or research sources.

---

# Observation Analysis

Observation records represent quantitative financial inclusion measurements.

Results include:

- 30 observations
- 19 unique indicators
- Time span:

2014 – 2025

Major indicators include:

- Account Ownership
- Mobile Money Accounts
- 4G Coverage
- Mobile Penetration
- Fayda Digital ID
- Telebirr Users
- ATM Usage
- Digital Payments
- Gender Gap
- Data Affordability

---

# Event Analysis

The dataset contains ten important events.

Categories include:

- Product Launch
- Policy
- Infrastructure
- Market Entry
- Partnership
- Milestone
- Pricing

Timeline:

2021–2025

These events describe major developments in Ethiopia's digital financial ecosystem.

---

# Impact Link Analysis

The Impact Sheet models causal relationships between events and indicators.

Results include:

- 14 impact links
- Direct relationships dominate
- Most impacts increase financial inclusion
- Average impact lag:

Approximately 8 months

Frequently affected indicators include:

- Account Ownership
- P2P Transactions
- Data Affordability
- Mobile Money Usage

---

# Event–Impact Relationship Analysis

Events were merged with impact links using:

```
parent_id
```

This created a unified dataset connecting:

- Events
- Indicators
- Expected impact
- Magnitude
- Direction
- Evidence
- Lag

This merged dataset provides the basis for later forecasting and intervention modeling.

---

# Data Enrichment

The dataset was enriched by introducing new records while preserving the original schema.

Added records include:

## Observations

- Financial Institution Branch Density
- QR Code Payment Transactions

## Events

- Digital Financial Services Strategy

## Impact Links

- Policy effect on Account Ownership

These additions improve forecasting capability by expanding both explanatory variables and event coverage.

---

# Output Files

The following datasets were generated.

```
data/processed/

ethiopia_fi_enriched.csv

impact_links_enriched.csv
```

Additional documentation:

```
docs/

data_enrichment_log.md
```

---

# Visualizations

The notebook includes:

- Record Type Distribution
- Financial Inclusion Pillars
- Source Type Distribution
- Confidence Distribution
- Indicator Coverage
- Event Categories
- Impact Relationships
- Event–Impact Mapping

---

# Key Findings

The exploratory analysis produced several important insights.

### Financial Access

Account ownership remains the most consistently measured financial inclusion indicator.

### Digital Finance

Telebirr and M-Pesa have significantly expanded Ethiopia's digital payment ecosystem.

### Infrastructure

Infrastructure expansion—including 4G coverage and digital identity—plays a major enabling role.

### Policy

Government policies and regulatory reforms appear to influence multiple financial inclusion indicators.

### Impact Relationships

Most modeled event impacts are positive, with effects typically occurring within one year.

---

# Data Enrichment Summary

The enrichment process added:

| Type | Records Added |
|------|--------------:|
| Observations | 2 |
| Events | 1 |
| Impact Links | 1 |

The enriched dataset preserves the original schema while improving forecasting readiness.

---

# Git Workflow

Development followed Git best practices.

Major commits include:

```text
Initialize project structure

Load unified financial inclusion dataset

Perform exploratory data analysis

Analyze observations and events

Analyze impact relationships

Merge event and impact datasets

Add enriched financial inclusion records

Save processed datasets

Document data enrichment process
```

---
---

# Task 2: Exploratory Data Analysis (EDA)

## Objective

Task 2 focuses on understanding the characteristics of Ethiopia's financial inclusion data through exploratory analysis. The goal is to identify trends, relationships, data quality issues, infrastructure drivers, and event impacts that influence financial inclusion outcomes and provide a strong foundation for forecasting.

---

# Task 2 Workflow

```text
Load Enriched Dataset
        │
        ▼
Dataset Overview
        │
        ▼
Data Quality Assessment
        │
        ▼
Access Analysis
        │
        ▼
Usage Analysis
        │
        ▼
Infrastructure & Enablers Analysis
        │
        ▼
Event Timeline Analysis
        │
        ▼
Correlation Analysis
        │
        ▼
Key Insights & Conclusions
```

---

# Dataset Overview

The exploratory analysis begins by summarizing the enriched dataset.

The analysis includes:

- Distribution of record types
- Financial inclusion pillars
- Source types
- Confidence levels
- Indicator coverage
- Temporal coverage
- Missing values assessment

Key findings:

- Observation records form the majority of analytical data.
- Access and Usage indicators dominate the dataset.
- Most records originate from official operator reports and surveys.
- Over 90% of records are classified as High confidence.
- Coverage spans from **2011–2025**, although many indicators contain only a few observations.

---

# Data Quality Assessment

Several quality checks were performed before analysis.

The assessment included:

- Missing value analysis
- Duplicate record detection
- Confidence distribution
- Indicator coverage
- Temporal completeness

### Findings

- No duplicate records were identified.
- Most missing values occur because the unified schema stores different record types within the same table.
- Event records naturally omit numerical observation fields.
- Impact link records omit several observation-specific attributes.
- Overall data quality is suitable for exploratory analysis and forecasting.

---

# Access (Account Ownership) Analysis

The Access pillar represents the percentage of Ethiopian adults who own a financial account.

Analysis performed:

- Historical trend visualization
- Growth rate calculation
- Year-over-year comparison
- Investigation of the 2021–2024 slowdown

### Key Findings

- Account ownership increased steadily between 2011 and 2021.
- Growth slowed considerably between 2021 and 2024, increasing by only three percentage points.
- Despite rapid expansion of mobile money services, overall financial account ownership did not accelerate proportionally.
- This suggests structural barriers beyond infrastructure expansion, including financial literacy, rural access, regulatory adoption, and user behavior.

---

# Usage (Digital Payments) Analysis

Digital payment adoption was analyzed using mobile money and payment-related indicators.

The analysis includes:

- Mobile money account ownership
- Telebirr growth
- M-Pesa adoption
- Digital payment indicators
- Registered versus active users

### Key Findings

- Mobile money adoption increased significantly after Telebirr's launch.
- Digital payment usage continues to expand through peer-to-peer transactions.
- Registered accounts substantially exceed active users, indicating a usage gap.
- Peer-to-peer transfers remain the dominant digital payment use case.

---

# Infrastructure and Enablers Analysis

Infrastructure indicators were evaluated to understand their contribution to financial inclusion.

Indicators analyzed include:

- Mobile penetration
- 4G network coverage
- Fayda Digital ID
- ATM infrastructure
- Data affordability

### Findings

- Mobile penetration continues to improve across Ethiopia.
- Expansion of 4G coverage creates favorable conditions for digital finance.
- Fayda Digital ID strengthens customer onboarding and electronic Know Your Customer (eKYC) processes.
- Data affordability remains an important determinant of digital payment adoption.
- Infrastructure variables appear to function as leading indicators for financial inclusion growth.

---

# Event Timeline Analysis

The dataset contains important policy and market events affecting financial inclusion.

Major events include:

- Telebirr Launch
- Safaricom Market Entry
- M-Pesa Launch
- National Financial Inclusion Strategy
- Infrastructure Expansion
- Pricing Reforms
- Strategic Partnerships

The event timeline was compared with major financial inclusion indicators.

### Findings

- Telebirr corresponds with substantial growth in digital payment indicators.
- Safaricom's market entry aligns with infrastructure investment.
- Policy interventions generally precede improvements in Access and Usage indicators.
- Multiple events influence the same indicator simultaneously, highlighting the importance of impact modeling.

---

# Correlation Analysis

Correlation analysis was performed using numerical indicators.

The analysis investigated relationships between:

- Access indicators
- Usage indicators
- Infrastructure metrics
- Gender indicators
- Affordability measures

### Findings

- Infrastructure variables demonstrate positive relationships with Access and Usage.
- Mobile money indicators are closely associated with digital payment adoption.
- Gender gap indicators remain negatively associated with overall inclusion.
- Affordability variables influence long-term adoption.

The analysis supports selecting infrastructure and digital payment metrics as important forecasting features.

---

# Event–Indicator Relationship Analysis

Existing impact links were analyzed to understand causal assumptions within the dataset.

The analysis examined:

- Direct versus indirect impacts
- Impact magnitude
- Expected lag
- Evidence basis
- Comparable country references

### Findings

- Direct relationships account for the majority of modeled impacts.
- Most modeled effects increase financial inclusion.
- Average implementation lag is approximately eight months.
- Literature and empirical evidence are the primary sources supporting impact estimates.

These relationships will be incorporated into the forecasting model during subsequent tasks.

---

# Visualizations Produced

Task 2 generated the following figures:

- Record Type Distribution
- Pillar Distribution
- Source Type Distribution
- Confidence Distribution
- Indicator Coverage
- Temporal Coverage Heatmap
- Missing Values Visualization
- Account Ownership Trend
- Account Ownership Growth Rate
- Mobile Money Trend
- Telebirr and M-Pesa Growth
- Infrastructure Indicators
- Event Timeline
- Event Category Distribution
- Correlation Heatmap
- Impact Relationship Distribution
- Leading Indicator Analysis

All visualizations are stored under:

```

reports/figures/

```

---

# Key Insights

The exploratory analysis produced several important findings.

## 1. Financial inclusion continues to improve but growth has slowed.

Account ownership increased significantly between 2011 and 2021 but experienced only modest growth between 2021 and 2024.

---

## 2. Mobile money expansion alone is insufficient.

Although Telebirr and M-Pesa rapidly increased registered users, this growth has not translated proportionally into financial account ownership.

---

## 3. Infrastructure is a major enabling factor.

Expansion of mobile penetration, 4G coverage, and digital identity services creates favorable conditions for increased financial inclusion.

---

## 4. Policy interventions have measurable impacts.

Product launches, regulatory reforms, infrastructure projects, and partnerships influence multiple financial inclusion indicators through direct and indirect relationships.

---

## 5. Data limitations remain.

Several indicators contain only one or two observations, limiting statistical forecasting approaches.

These limitations motivate combining trend forecasting with event-based intervention modeling.

---

# Output Files

Task 2 produced:

```

reports/
│
├── figures/
│   ├── account_ownership_trend.png
│   ├── growth_rate.png
│   ├── mobile_money_trend.png
│   ├── infrastructure_analysis.png
│   ├── event_timeline.png
│   ├── correlation_heatmap.png
│   └── ...

```

Notebook:

```

notebooks/
Task_2_Exploratory_Data_Analysis.ipynb

```

---

# Git Workflow

Task 2 development followed Git best practices.

Major commits include:

```text
Create Task 2 exploratory data analysis notebook

Analyze dataset overview and quality

Perform access analysis

Analyze digital payment usage

Analyze infrastructure indicators

Create event timeline visualization

Perform correlation analysis

Summarize EDA insights

Complete Task 2 exploratory analysis
```

---

# Next Steps

Task 3 will focus on:

- Building the Event–Indicator Association Matrix
- Event Impact Modeling
- Comparable Country Analysis
- Impact Validation
- Methodology Documentation

These outputs will support forecasting Ethiopia's financial inclusion indicators for 2025–2027.

---

# Future Work

Subsequent tasks will include:

- Event Impact Modeling
- Association Matrix Construction
- Forecasting Access and Usage
- Streamlit Dashboard Development

---

# Author

**Lalise Fufi**

10 Academy – Artificial Intelligence Mastery

Week 11 Challenge

---

# References

- World Bank Global Findex
- National Bank of Ethiopia
- Ethio Telecom
- GSMA
- IMF Financial Access Survey
- EthSwitch
- Fayda Digital ID
- 10 Academy Week 11 Challenge Documentation

---