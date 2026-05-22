import os
import requests
from langchain.tools import tool

# Meridian Alpha Systems - A2A Maritime Intelligence
# This wrapper allows seamless integration with LangChain / CrewAI agents.

MERIDIAN_API_URL = os.getenv("MERIDIAN_API_URL", "http://199.247.19.249:8002/mcp/v1/tools/execute")
MERIDIAN_API_KEY = os.getenv("MERIDIAN_API_KEY", "") # Retrieve your Master Key via RapidAPI or use L402
MERIDIAN_L402_TOKEN = os.getenv("MERIDIAN_L402_TOKEN", "") # Use if paying per-request via Skyfire / Lightning

@tool
def calculate_true_price_tool(origin_port: str, destination_port: str, container_type: str) -> dict:
    """
    Calculates the TruePrice of maritime shipping and detects hidden financial anomalies.
    Essential for determining the actual cost including Red Sea rerouting and EU ETS Carbon Surcharges.
    
    Args:
        origin_port (str): UN/LOCODE or port name (e.g., 'Shanghai').
        destination_port (str): UN/LOCODE or port name (e.g., 'Rotterdam').
        container_type (str): '20ft' or '40ft'.
        
    Returns:
        dict: The TruePrice breakdown including surcharges and market psychology index.
    """
    
    headers = {
        "Content-Type": "application/json"
    }
    
    # Apply L402 / Skyfire or Subscription Master Key
    if MERIDIAN_L402_TOKEN:
        headers["Authorization"] = f"L402 {MERIDIAN_L402_TOKEN}"
    elif MERIDIAN_API_KEY:
        headers["X-API-Key"] = MERIDIAN_API_KEY
    else:
        return {"error": "Authentication required. Please provide MERIDIAN_API_KEY or MERIDIAN_L402_TOKEN in your environment."}

    payload = {
        "name": "calculate_rerouting_financial_impact",
        "arguments": {
            "origin_port": origin_port,
            "destination_port": destination_port,
            "container_type": container_type
        }
    }

    try:
        response = requests.post(MERIDIAN_API_URL, json=payload, headers=headers, timeout=10)
        if response.status_code == 402:
            return {"error": "L402 Payment Required", "invoice": response.headers.get("WWW-Authenticate")}
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API Request Failed: {str(e)}"}

# Example Usage for an Agent:
# from langchain.agents import initialize_agent
# agent = initialize_agent([calculate_true_price_tool], llm, agent="zero-shot-react-description")
