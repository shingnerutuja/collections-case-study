-- Step 1: Create Cleaned & Deduplicated Payments Fact Table
CREATE OR REPLACE TABLE fact_payments_cleaned AS
WITH deduplicated_payments AS (
    SELECT 
        payment_id,
        account_id,
        borrower_id,
        event_at,
        amount,
        payment_status,
        payment_method,
        provider_id,
        ROW_NUMBER() OVER (
            PARTITION BY payment_id 
            ORDER BY event_at DESC
        ) AS row_num
    FROM raw_payments
)
SELECT 
    payment_id,
    account_id,
    borrower_id,
    CAST(event_at AS DATE) AS payment_date,
    DATE_TRUNC('month', CAST(event_at AS DATE)) AS payment_month,
    amount,
    payment_status,
    payment_method,
    provider_id
FROM deduplicated_payments
WHERE row_num = 1 
  AND payment_status = 'SUCCESS';

-- Step 2: Create Consolidated Agent Dimension Table
CREATE OR REPLACE TABLE dim_agents_cleaned AS
SELECT 
    agent_name,
    COUNT(DISTINCT agent_id) AS total_mapped_system_ids,
    MIN(created_at) AS first_seen_at,
    MAX(created_at) AS last_seen_at
FROM raw_agents
GROUP BY agent_name;

-- Step 3: Verified Monthly Recovery Performance Summary
CREATE OR REPLACE TABLE summary_monthly_recovery_performance AS
SELECT 
    payment_month,
    COUNT(payment_id) AS total_successful_transactions,
    SUM(amount) AS total_cleaned_recovery_amount,
    LAG(SUM(amount)) OVER (ORDER BY payment_month) AS previous_month_amount,
    ROUND(
        (SUM(amount) - LAG(SUM(amount)) OVER (ORDER BY payment_month)) 
        / NULLIF(LAG(SUM(amount)) OVER (ORDER BY payment_month), 0) * 100, 
        2
    ) AS mom_cleaned_growth_pct
FROM fact_payments_cleaned
GROUP BY payment_month
ORDER BY payment_month;
