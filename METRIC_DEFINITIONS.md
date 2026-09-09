# Independent Recovery Metric Definitions

| Metric Name | Independent Proposed Formula | Numerator | Denominator | Rationale & Challenge to Legacy Metric |
| :--- | :--- | :--- | :--- | :--- |
| **Clean Recovery Rate** | Verified Cash Recovered / Outstanding Principal | Sum of `SUCCESS` Payment Amounts ($) | Total Portfolio Outstanding Balance ($) | Eliminates failed retries and duplicate transaction IDs from revenue claims. |
| **Right Party Contact (RPC) Rate** | Verified Contacts / Unique Dialed Accounts | Unique Accounts with Disposition = `RPC` | Total Unique Accounts Attempted | Uses unique accounts instead of raw call count to prevent dialer retry inflation. |
| **PTP Kept Rate** | Kept Promises / Total Promises Made | Distinct `payment_id` tied to `PTP` within 7 Days | Total Recorded `PTP` Dispositions | Measures actual cash conversion rather than agent verbal commitments. |
| **Recovery Per Agent-Hour** | Clean Recovery / Active Shift Hours | Total Verified Cash ($) | Consolidated Shift Hours (via Master Agent ID) | Aggregates fragmented `agent_id` instances to measure true human performance. |
| **Cost Per ₹ Recovered** | Total Operational Expense / Verified Cash | Operations + Vendor Telephony Cost (₹) | Total Verified Cash Recovered (₹) | Reflects true efficiency by excluding uncollected or failed payment attempts. |
