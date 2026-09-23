\# API Setup Guide



\## 1. NocoDB Configuration

\- Endpoint: `http://localhost:8080/api/v2/tables/`

\- Authentication Header: `xc-token`

\- Tables Required: `Sales\_Data`, `Data\_Dictionary`



\## 2. Ollama Setup

\- Host: `http://host.docker.internal:11434`

\- Model: `llama3.2:latest`

\- Locked Context Length: `4096`

\- Temperature: `0.2`

