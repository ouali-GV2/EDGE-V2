import os
import json
from datetime import datetime, timedelta

import pandas as pd

from utils.logger import get_logger
from utils.api_guard import safe_get
from utils.cache import Cache

from src.universe_loader import load_universe
from src.signal_engine import generate_signal

from config import FINNHUB_API_KEY

logger = get_logger("WEEKLY_AUDIT")

os.makedirs("data/audit_reports", exist_ok=True)

cache = Cache(ttl=3600)

FINNHUB_GAINERS = "https://finnhub.io/api/v1/stock/top-gainers"


# ============================
# Fetch real market top gainers
# ============================

def fetch_top_gainers():

    params = {
        "token": FINNHUB_API_KEY
    }

    r = safe_get(FINNHUB_GAINERS, params=params)
    data = r.json()

    tickers = []

    for item in data:
        t = item.get("symbol")
        if t:
            tickers.append(t)

    logger.info(f"Fetched {len(tickers)} real top gainers")

    return tickers


# ============================
# Get EDGE detected tickers
# ============================

def get_edge_detected():

    universe = load_universe()
    tickers = universe["ticker"].tolist()

    detected = []

    for t in tickers:
        s = generate_signal(t)
        if s and s["signal"] in ["BUY", "BUY_STRONG"]:
            detected.append({
                "ticker": t,
                "score": s["monster_score"],
                "confidence": s["confidence"]
            })

    return pd.DataFrame(detected)


# ============================
# Weekly audit core
# ============================

def run_weekly_audit():

    real_gainers = fetch_top_gainers()

    edge_df = get_edge_detected()

    detected_set = set(edge_df["ticker"])
    gainer_set = set(real_gainers)

    hits = detected_set.intersection(gainer_set)
    missed = gainer_set - detected_set
    false_positive = detected_set - gainer_set

    report = {
        "date": datetime.utcnow().strftime("%Y-%m-%d"),
        "real_top_gainers": list(gainer_set),
        "edge_detected": edge_df.to_dict(orient="records"),
        "hits": list(hits),
        "missed": list(missed),
        "false_positive": list(false_positive),
        "hit_rate": round(len(hits) / max(1, len(gainer_set)), 3)
    }

    filename = f"data/audit_reports/weekly_audit_{datetime.utcnow().strftime('%Y%m%d')}.json"

    with open(filename, "w") as f:
        json.dump(report, f, indent=2)

    logger.info(f"Weekly audit saved: {filename}")
    logger.info(f"Hit rate: {report['hit_rate']*100:.2f}%")

    return report


# ============================
# CLI
# ============================

if __name__ == "__main__":
    result = run_weekly_audit()
    print(json.dumps(result, indent=2))
