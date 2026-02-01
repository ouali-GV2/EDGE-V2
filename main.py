import time
import threading
import datetime

from utils.logger import get_logger
from utils.time_utils import is_premarket, is_market_open, is_market_closed
from utils.api_guard import api_safe_call

from src.universe_loader import load_universe
from src.signal_engine import generate_signal
from src.portfolio_engine import process_signal

from alerts.telegram_alerts import send_signal_alert
from monitoring.system_guardian import run_system_guardian
from weekly_deep_audit import run_weekly_audit

logger = get_logger("MAIN")

# ============================
# EDGE CORE CYCLE
# ============================

def edge_cycle():
    """
    Cycle principal du moteur EDGE - VERSION SIMPLIFIÉE FONCTIONNELLE
    """
    universe = load_universe()

    if universe is None or universe.empty:
        logger.warning("Universe empty - skipping cycle")
        return

    logger.info(f"Scanning {len(universe)} tickers")

    for _, row in universe.iterrows():

        ticker = row["ticker"]

        try:
            # ------------------------
            # SIGNAL GENERATION
            # ------------------------
            # generate_signal() encapsule toute la logique:
            # - Récupère les events via get_events_by_ticker()
            # - Calcule les features
            # - Calcule le monster_score
            # - Détermine le signal (BUY/BUY_STRONG/HOLD)
            
            signal = generate_signal(ticker)

            if not signal or signal["signal"] == "HOLD":
                continue

            # ------------------------
            # ENSEMBLE (CONFLUENCE)
            # ------------------------
            # Applique le boost de confluence sur le signal
            from src.ensemble_engine import apply_confluence
            signal = apply_confluence(signal)

            # ------------------------
            # PORTFOLIO ENGINE
            # ------------------------
            # Calcule la taille de position et les stops
            trade_plan = process_signal(signal)
            
            if not trade_plan:
                logger.warning(f"Could not create trade plan for {ticker}")
                continue
            
            logger.info(
                f"TRADE PLAN: {trade_plan['signal']} {trade_plan['shares']} shares of {ticker} "
                f"@ ${trade_plan['entry']} (stop: ${trade_plan['stop']})"
            )

            # ------------------------
            # ALERT
            # ------------------------
            send_signal_alert(trade_plan)

        except Exception as e:
            logger.error(f"EDGE error on {ticker}: {e}", exc_info=True)


# ============================
# WEEKLY AUDIT SCHEDULER
# ============================

last_audit_day = None

def should_run_weekly_audit():
    now = datetime.datetime.utcnow()
    return now.weekday() == 4 and now.hour == 22  # Friday 22h UTC


# ============================
# MAIN LOOP
# ============================

def run_edge():

    global last_audit_day

    logger.info("GV2-EDGE LIVE ENGINE STARTED")

    while True:

        try:
            now = datetime.datetime.utcnow().date()

            # ---- Weekly audit ----
            if should_run_weekly_audit() and now != last_audit_day:
                logger.info("Running Weekly Deep Audit")
                run_weekly_audit()
                last_audit_day = now

            # ---- Trading sessions ----
            if is_premarket():
                logger.info("PRE-MARKET session")
                edge_cycle()
                time.sleep(300)  # every 5 min

            elif is_market_open():
                logger.info("REGULAR MARKET session")
                edge_cycle()
                time.sleep(180)  # every 3 min

            elif is_market_closed():
                logger.info("Market closed - idle")
                time.sleep(900)  # 15 min sleep

            else:
                time.sleep(300)

        except Exception as e:
            logger.error(f"Main loop crash: {e}")
            time.sleep(60)


# ============================
# SYSTEM GUARDIAN THREAD
# ============================

def start_guardian():
    run_system_guardian()


# ============================
# ENTRY POINT
# ============================

if __name__ == "__main__":

    logger.info("Booting GV2-EDGE")

    guardian_thread = threading.Thread(
        target=start_guardian,
        daemon=True
    )
    guardian_thread.start()

    run_edge()
