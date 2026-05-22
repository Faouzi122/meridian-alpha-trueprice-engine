# Meridian Alpha Systems - TruePrice & Transparency Engine
## Automated Geopolitical & Maritime Freight Volatility Arbitrage

**Version:** 2.0.0

The **Meridian Alpha Engine** is a proprietary semantic volatility and arbitration engine designed for the AI Agent economy (A2A - Agent-to-Agent). It analyzes unstructured maritime feed data, port dispatches, and carbon surcharge fluctuations to determine the **TruePrice** of cargo routing under geopolitical disruptions (such as Red Sea or Cape of Good Hope reroutings).

---

## 1. Capabilities & MCP Tools

This engine is exposed as a native **Model Context Protocol (MCP)** server, making its capabilities directly discoverable and executable by LLMs and autonomous agents.

### Tool: `calculate_rerouting_financial_impact`
- **Description:** Computes the precise cost difference between standard shipping corridors and disrupted routes, accounting for dynamic bunker fuel spikes and EU ETS carbon pricing.
- **Parameters:**
  - `origin_port` (string, required): UN/LOCODE or port name (e.g. `Shanghai`).
  - `destination_port` (string, required): UN/LOCODE or port name (e.g. `Rotterdam`).
  - `container_type` (enum: `20ft`, `40ft`, required): Standard container size.

---

## 2. Dynamic L402 Microtransactions (Bitcoin Lightning)

To interact with the MCP tool at scale without subscription overhead, the server implements the **L402 (formerly LSAT)** open authentication standard for machine-to-machine payments.

```
AI Agent                    Meridian Server             LN Wallet / Node
   │                               │                            │
   │ 1. Execute Tool (no token)    │                            │
   ├──────────────────────────────>│                            │
   │                               │                            │
   │ 2. HTTP 402 Payment Required  │                            │
   │    (returns invoice lnbc...)  │                            │
   │<──────────────────────────────┤                            │
   │                               │                            │
   │ 3. Pay Invoice (150 sats)     │                            │
   ├───────────────────────────────┼───────────────────────────>│
   │                               │                            │
   │ 4. Receive Preimage           │                            │
   │<──────────────────────────────┼────────────────────────────┤
   │                               │                            │
   │ 5. Execute Tool (with proof)  │                            │
   │    Authorization: L402 mac:pre│                            │
   ├──────────────────────────────>│                            │
   │                               │                            │
   │ 6. HTTP 200 OK (Data Output)  │                            │
   │<──────────────────────────────┤                            │
```

For institutional developers, the server also accepts a permanent `X-API-Key` bypass header.

---

## 3. Global MCP Registry (Smithery.ai)

This server is listed on **Smithery.ai**. You can automatically install it into your local AI environment (Cursor, Claude Desktop, Cline, etc.) by running:

```bash
npx -y @smithery/cli install @faouzi122/meridian-alpha-trueprice-engine
```

To configure it manually in your `mcpServers` json, point to the remote instance:
```json
{
  "mcpServers": {
    "meridian-alpha": {
      "command": "npx",
      "args": ["-y", "@faouzi122/meridian-alpha-trueprice-engine"],
      "env": {
        "MERIDIAN_API_URL": "http://199.247.19.249:8002"
      }
    }
  }
}
```

---

*© 2026 Meridian Alpha Systems. All rights reserved. Sovereign Infrastructure.*
