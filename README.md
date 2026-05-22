# Meridian Alpha Systems - TruePrice & Transparency Engine
## Automated Geopolitical & Maritime Freight Volatility Arbitrage

**Version:** 2.0.0

API for AI Agents: Instantly calculate hidden maritime routing surcharges and geopolitical risk premiums. 

Designed for the A2A (Agent-to-Agent) economy, our API exposes standard REST endpoints and a native MCP (Model Context Protocol) bridge targeting specific geopolitical anomalies (e.g., Red Sea / Cape of Good Hope rerouting costs).

### Core Capabilities
- **Semantic Volatility Engine:** Analyzes unstructured text (news dispatches, port updates, military alerts).
- **Contextual Isolation:** Differentiates risk between major corridors (e.g., Transpacific vs. Suez/Europe).
- **Financial Quantification:** Translates panic into exact monetary surcharges, delivering a TruePrice estimate.

### Integration
We support two primary integration pathways:

1. **REST API:** Standard HTTP requests documented in our [OpenAPI Specification](openapi/openapi.json). Perfect for traditional software infrastructure.
2. **MCP Bridge:** A native integration for autonomous AI agents (Claude, Gemini, etc.) to discover and utilize the `detect_red_sea_anomaly_cost` tool. See the [MCP Manifest](mcp_server/manifest.json).

### Monetization & Paywall Clearance
To unlock the production paywall and obtain your cryptographic master token, you must subscribe to our official channel on the API Hub:

👉 **[Access the Meridian Alpha Pricing Tiers on RapidAPI](https://rapidapi.com/meridian-alpha-hub/api/trueprice-ocean-freight-arbitrage-engine)**

#### Production cURL Execution Example:
```bash
curl --request POST \
	--url https://trueprice-ocean-freight-arbitrage-engine.p.rapidapi.com/analyze/compare \
	--header 'Content-Type: application/json' \
	--header 'X-API-Key: YOUR_MERIDIAN_ALPHA_MASTER_KEY' \
	--header 'x-rapidapi-host: trueprice-ocean-freight-arbitrage-engine.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_MARKETPLACE_TOKEN' \
	--data '{"text":"Severe military escalations in the Red Sea cause container rerouting."}'
```

---

*© 2026 Meridian Alpha Systems. All rights reserved. Programmatic and Capability Interface.*
