# Meridian Alpha Systems - TruePrice & Transparency Engine
## Automated Geopolitical & Maritime Freight Volatility Arbitrage

**Version:** 1.0.0

Meridian Alpha Systems provides a high-performance, algorithmic evaluation of geopolitical news, identifying hidden surcharges and calculating TruePrice estimates for 20ft and 40ft maritime containers. 

Designed for the A2A (Agent-to-Agent) economy, our API exposes standard REST endpoints and a native MCP (Model Context Protocol) bridge, allowing autonomous agents to execute rapid, sub-15ms volatility arbitrage.

### Core Capabilities
- **Semantic Volatility Engine:** Analyzes unstructured text (news dispatches, port updates, military alerts).
- **Contextual Isolation:** Differentiates risk between major corridors (e.g., Transpacific vs. Suez/Europe).
- **Financial Quantification:** Translates panic into exact monetary surcharges, delivering a TruePrice estimate.

### Integration
We support two primary integration pathways:

1. **REST API:** Standard HTTP requests documented in our [OpenAPI Specification](openapi/openapi.json). Perfect for traditional software infrastructure.
2. **MCP Bridge:** A native integration for autonomous AI agents (Claude, Gemini, etc.) to discover and utilize the `get_true_freight_arbitrage` tool. See the [MCP Manifest](mcp_server/manifest.json).

### Security
All endpoints are secured via an institutional `X-API-Key`.

---
*© 2026 Meridian Alpha Systems. All rights reserved.*
