# Forecasting Financial Inclusion in Ethiopia

> **10 Academy – Artificial Intelligence Mastery**
>
> **Week 11 Challenge**
>
> **Task 1: Data Exploration and Enrichment**
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

# Future Work

Subsequent tasks will include:

- Exploratory Data Analysis
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