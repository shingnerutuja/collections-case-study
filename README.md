# collections-case-study
Recovery Performance Audit &amp; Data Quality Reconciliation - Rutuja Shingne (COEP Technological university - Mechanical Engineering)



# Recovery Performance Audit & Data Quality Reconciliation

**Submitted By:** Rutuja Shingne  
**Institution:** COEP Technological University  
**Branch:** Mechanical Engineering  

---

## Executive Summary
This repository contains the complete analytical pipeline, data quality forensics, independent recovery metrics, and strategic investment roadmap for the 12-month recovery audit.

## Repository Directory & Deliverables
* 📄 **[Master Executive Report (PDF)](./Collections%20Case%20Study..pdf):** Full compiled report containing all core deliverables.
* 🛢️ **[Production SQL Transformations](./transformations.sql):** SQL deduplication, agent aggregation, and data mart modeling.
* 🐍 **[Data Forensics Script](./data_forensics.py):** Python pipeline for data quality checks and MoM growth reconciliation.
* 💰 **[₹10 Cr Investment Recommendation](./INVESTMENT_RECOMMENDATION.md):** Detailed capital allocation plan for Option 4 (Better Borrower Targeting).
* 📐 **[Independent Metric Definitions](./METRIC_DEFINITIONS.md):** Re-defined RPC, PTP Kept Rate, and Clean Recovery Rate formulas.
* 🔬 **[Counterfactual Analysis](./COUNTERFACTUAL_ANALYSIS.md):** Difference-in-Differences methodology for targeting impact evaluation.

---

## Key Performance Findings
* **Claimed Raw Growth (Mar 2026):** +12.23% ($275.17M)
* **Verified Clean Growth (Mar 2026):** +11.03% ($188.91M)
* **Reporting Inflation Gap:** +$86.26M per month due to failed payment attempts and duplicate `payment_id` logs.
* **Agent System ID Mapping:** 1,000 system `agent_id` records mapped back to 10 unique human agent master profiles.
