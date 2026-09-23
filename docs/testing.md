\# Validation Test Suite



| Query Type | Input Query | Expected Result |

| :--- | :--- | :--- |

| Direct Column | "What is total sales by region?" | Queries physical `Sales` and `Region` columns. |

| Calculated Metric | "What is our profit margin?" | Applies formula `(SUM(Profit)/SUM(Sales))\*100`. |

| Missing Entity | "Who is our top customer?" | Rejects query citing Data Dictionary restriction. |

| Executive Mode | "Give me an executive summary" | Outputs full summary with KPIs, insights, investigations, actions, and regional breakdown. |

