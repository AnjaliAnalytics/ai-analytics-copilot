\# System Limitations



1\. \*\*Context Limits:\*\* Local model outputs must follow strict length rules to prevent token clipping.

2\. \*\*Schema Restrictions:\*\* Customer segmentation queries are rejected because raw transaction logs lack account IDs.

3\. \*\*Concurrency:\*\* Local Ollama model runs sequentially on available GPU/CPU threads.

