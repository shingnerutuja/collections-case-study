# Counterfactual Analysis: Isolation of Targeting Strategy Impact

## Problem Statement
Leadership asks: *"What would recovery have looked like if we had not changed the targeting strategy midway through the year?"*

## Methodology & Identification Strategy
We employ a **Difference-in-Differences (DiD)** estimation framework combined with **Propensity Score Matching (PSM)**:
1. **Treatment Group:** Borrowers assigned to the new multi-channel targeting campaign post-month 6.
2. **Control Group:** Borrowers with identical baseline DPD, loan size, and geography retained on legacy dialing schedules.
3. **Matching Variables:** Baseline DPD, historical payment frequency, loan amount, and principal balance.

## Assumed Findings & Decomposition
* **Observed Growth:** +11.03% clean recovery growth.
* **Counterfactual Uplift (Strategy Change):** +2.40% net gain directly attributable to the targeting shift.
* **Base Portfolio Effect:** +8.63% driven by organic portfolio volume changes and macro recovery trends.

## Confounding Factors & Limitations
* **Confounders Controlled:** Macroeconomic seasonality and shift-level agent turnover.
* **Limitations:** Potential unobserved borrower behavioral shifts outside platform telemetry.
