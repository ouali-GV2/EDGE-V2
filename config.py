# ============================
# GV2-EDGE GLOBAL CONFIG
# ============================

# ========= API KEYS =========

GROK_API_KEY = "YOUR_GROK_API_KEY"
FINNHUB_API_KEY = "YOUR_FINNHUB_API_KEY"

# IBKR (read-only mode)
IBKR_HOST = "127.0.0.1"
IBKR_PORT = 7497   # paper trading (7496 real)
IBKR_CLIENT_ID = 12

# Telegram
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

# ============================
# TRADING CAPITAL
# ============================

# Option 1 — Manual (recommended start)
MANUAL_CAPITAL = 1000  

# Option 2 — Auto from IBKR
USE_IBKR_CAPITAL = False  

# ============================
# RISK SETTINGS
# ============================

RISK_BUY = 0.02           # 2% risk per trade
RISK_BUY_STRONG = 0.025  # 2.5% risk per trade

MAX_OPEN_POSITIONS = 5

# ============================
# STOPS & TRAILING
# ============================

ATR_MULTIPLIER_STOP = 2.0
ATR_MULTIPLIER_TRAIL = 1.5

USE_STRUCTURE_STOP_PM = True

# ============================
# SCAN TIMING (seconds)
# ============================

FULL_UNIVERSE_SCAN_INTERVAL = 300     # 5 min
EVENT_SCAN_INTERVAL = 600             # 10 min
PM_SCAN_INTERVAL = 60                 # 1 min

# ============================
# MARKET SESSIONS (US TIME)
# ============================

PREMARKET_START = "04:00"
MARKET_OPEN = "09:30"
MARKET_CLOSE = "16:00"
AFTER_HOURS_END = "20:00"

# ============================
# UNIVERSE FILTERS
# ============================

MAX_MARKET_CAP = 2_000_000_000   # 2B small caps
MIN_PRICE = 0.5
MAX_PRICE = 20
MIN_AVG_VOLUME = 300_000

EXCLUDE_OTC = True

# ============================
# EVENT BOOST SETTINGS
# ============================

EVENT_PROXIMITY_BOOST = {
    "today": 1.5,
    "tomorrow": 1.3,
    "week": 1.1
}

EVENT_PROXIMITY_DAYS = 7  # Jours pour considérer un événement comme proche

# ============================
# MONSTER SCORE WEIGHTS (INIT)
# ============================

# Poids BASIQUES (sans patterns avancés)
DEFAULT_MONSTER_WEIGHTS = {
    "event": 0.35,        # Poids des événements (FDA, M&A, Earnings, etc.)
    "momentum": 0.20,     # Poids du momentum prix
    "volume": 0.15,       # Poids du spike de volume
    "vwap": 0.10,        # Poids de la déviation VWAP
    "squeeze": 0.10,     # Poids du squeeze (momentum/volatilité)
    "pm_gap": 0.10       # Poids du gap pre-market
}
# Note: La somme DOIT faire 1.0 pour cohérence

# Poids AVANCÉS (avec patterns + PM transition)
ADVANCED_MONSTER_WEIGHTS = {
    "event": 0.25,          # Réduit (patterns détectent mieux)
    "momentum": 0.15,       # Réduit
    "volume": 0.10,         # Maintenu
    "pattern": 0.20,        # NOUVEAU - Patterns avancés
    "pm_transition": 0.15,  # NOUVEAU - Timing PM→RTH
    "squeeze": 0.10,        # Amélioré (Bollinger)
    "vwap": 0.05           # Réduit
}
# Total = 1.0

# ============================
# PATTERN ANALYZER SETTINGS
# ============================

USE_ADVANCED_PATTERNS = True  # Activer patterns avancés
PATTERN_MIN_CANDLES = 20      # Minimum de candles pour analyse

# Seuils patterns
TIGHT_CONSOLIDATION_MAX_RANGE = 0.03  # 3% max pour consolidation tight
HIGHER_LOWS_MIN_TOUCHES = 3           # Minimum de higher lows
FLAG_PENNANT_SPIKE_THRESHOLD = 0.10   # 10% spike minimum pour flag
BOLLINGER_SQUEEZE_THRESHOLD = 0.5     # Ratio bandwidth pour squeeze

# ============================
# PM TRANSITION SETTINGS
# ============================

PM_RETEST_TOLERANCE = 0.005        # ±0.5% tolérance pour retest PM high
PM_FAKEOUT_MIN_HOLD_CANDLES = 5   # Candles minimum pour éviter fakeout
PM_STRONG_POSITION_THRESHOLD = 0.8 # Position dans range PM (80%+ = bullish)

# ============================
# AUTO TUNING
# ============================

AUTO_TUNING_ENABLED = True

TUNING_STEP = 0.02
TUNING_MIN_WEIGHT = 0.05
TUNING_MAX_WEIGHT = 0.50

# ============================
# SLIPPAGE SIMULATION (BACKTEST)
# ============================

BASE_SLIPPAGE_PCT = 0.2    # 0.2%
LOW_LIQUIDITY_SLIPPAGE = 0.5

# ============================
# LOGGING
# ============================

LOG_LEVEL = "INFO"
LOG_ROTATION_MB = 10
LOG_BACKUPS = 5

# ============================
# PERFORMANCE SAFETY
# ============================

MAX_CPU_USAGE = 85   # %
MAX_RAM_USAGE = 80   # %

# ============================
# DASHBOARD
# ============================

DASHBOARD_REFRESH_SECONDS = 5

# ============================
# BACKTEST
# ============================

BACKTEST_SLIPPAGE_ENABLED = True
BACKTEST_REALISTIC_STOPS = True

# ============================
# MISC
# ============================

DEBUG_MODE = False

# ============================
# SIGNAL THRESHOLDS
# ============================

BUY_THRESHOLD = 0.65          # Score minimum pour signal BUY
BUY_STRONG_THRESHOLD = 0.80   # Score minimum pour signal BUY_STRONG

# ============================
# PRE-MARKET SETTINGS
# ============================

PM_MIN_VOLUME = 50000         # Volume minimum en pre-market pour liquidité
