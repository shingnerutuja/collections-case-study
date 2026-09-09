# Complete Data Integrity & Verification Audit Pipeline
import pandas as pd

# Load Datasets
payments = pd.read_csv('payments.csv')
agents = pd.read_csv('agents.csv')

# 1. Payment Deduplication & Status Audit
total_records = len(payments)
unique_ids = payments['payment_id'].nunique()
duplicate_count = total_records - unique_ids

print("=== 1. PAYMENTS INTEGRITY ===")
print(f"Total Payment Records: {total_records}")
print(f"Unique Payment IDs: {unique_ids}")
print(f"Duplicate Payment IDs: {duplicate_count}")

# 2. Agent Identity Fragmentation Check
agent_summary = agents.groupby('agent_name')['agent_id'].nunique().reset_index()
agent_summary.columns = ['Agent Name', 'Mapped System IDs']

print("\n=== 2. AGENT IDENTITY FRAGMENTATION ===")
print(f"Total Unique Agent Names: {agents['agent_name'].nunique()}")
print(f"Total Unique Agent IDs: {agents['agent_id'].nunique()}")
print(agent_summary.to_string(index=False))

# 3. Monthly Recovery Growth Reconciliation (Raw vs Clean)
payments['event_at'] = pd.to_datetime(payments['event_at'])

# Raw calculation
raw = payments.groupby(payments['event_at'].dt.to_period('M'))['amount'].sum().reset_index()
raw['MoM_Raw_%'] = raw['amount'].pct_change() * 100

# Cleaned calculation
payments_clean = payments[payments['payment_status'] == 'SUCCESS'].drop_duplicates(subset=['payment_id'])
cleaned = payments_clean.groupby(payments_clean['event_at'].dt.to_period('M'))['amount'].sum().reset_index()
cleaned['MoM_Cleaned_%'] = cleaned['amount'].pct_change() * 100

# Comparison
comparison = pd.merge(raw, cleaned, on='event_at', suffixes=('_Raw', '_Cleaned'))
comparison['Inflation_Gap'] = comparison['amount_Raw'] - comparison['amount_Cleaned']

print("\n=== 3. MONTHLY RECOVERY COMPARISON ===")
print(comparison.to_string(index=False))
