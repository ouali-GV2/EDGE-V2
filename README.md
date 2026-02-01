# 🚀 GV2-EDGE — Advanced Momentum & Event-Driven Trading System

![Version](https://img.shields.io/github/v/tag/ouali-GV2/GV2-EDGE?label=version)
![Audit](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ouali-GV2/GV2-EDGE/main/data/audit_status.json)
![API Health](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/ouali-GV2/GV2-EDGE/main/data/api_health.json)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Status](https://img.shields.io/badge/status-production--ready-brightgreen)

---

## 🎯 Objectif

GV2-EDGE est un système automatisé conçu pour détecter **très tôt** les top gainers small caps US (hors OTC) avant leurs hausses majeures.

Il combine :

• momentum réel  
• catalysts multi-sources  
• analyse pré-market  
• scoring intelligent  
• risk management pro  

👉 Objectif final : maximiser le rendement réel tout en contrôlant le risque.

---

## 🧠 Philosophie

GV2-EDGE privilégie :

✅ simplicité robuste  
✅ vitesse d’exécution  
✅ données concrètes  
✅ amélioration continue  

et évite :

❌ IA lourde instable  
❌ overfitting  
❌ complexité inutile  

---

## 🧱 Architecture globale

Universe Loader ↓ Event Hub + NLP Grok ↓ Social Sentiment & News Buzz ↓ Feature Engine (Momentum, PM, VWAP, Patterns) ↓ Monster Score (scoring principal) ↓ Ensemble Engine (confluence multi-facteurs) ↓ Signal Engine (BUY / BUY_STRONG / HOLD) ↓ Portfolio Engine (risk & sizing) ↓ Dashboard + Telegram Alerts

En parallèle :

• Monitoring technique (System Guardian)  
• Weekly Deep Audits  
• Backtests manuels réalistes  
• Performance Attribution  

---

# 📦 Briques détaillées

### 🌍 Universe Loader
Construit l’univers dynamique small caps US via Finnhub/IBKR.  
Exclut OTC, filtre liquidité.

---

### 📅 Event Hub (multi-source)
Détecte :

✔ Earnings  
✔ FDA  
✔ M&A  
✔ Sector news  
✔ Analyst actions  
✔ Breaking news  

Avec parsing NLP Grok + boost par proximité.

---

### 🧠 NLP Event Parser
Extraction intelligente :

• tickers concernés  
• type d’event  
• impact estimé  

---

### 📣 Social Engine
- Sentiment X/Twitter (via Grok)  
- Buzz news  

Objectif : mesurer l’intérêt soudain du marché.

---

### 📈 Feature Engine

Calcule :

• gap %  
• volume spike  
• momentum velocity  
• VWAP deviation  
• pre-market levels  
• breakout & pullback patterns  

---

### 🧮 Monster Score

Score principal combinant :

momentum + volume + events + social + patterns  

avec boosts intelligents.

---

### 🔗 Ensemble Engine

Mesure la confluence des signaux pour renforcer la conviction.

---

### 🚦 Signal Engine

| Signal | Description |
|-------|------------|
| BUY_STRONG | Opportunité majeure |
| BUY | Opportunité solide |
| HOLD | Ignorer |

---

### ⚖️ Portfolio Engine

• position sizing automatique  
• stops dynamiques  
• trailing stops  
• protection drawdown  

---

### 📊 Dashboard Streamlit

Affiche :

✔ signaux live  
✔ scores & heatmaps  
✔ niveaux PM/HOD  
✔ performance  
✔ santé système  

---

### 🚨 Telegram Alerts

• BUY_STRONG instantané  
• BUY  
• alertes techniques  

---

### 🧪 Backtest Engine EDGE

Simulation réaliste :

• timeline  
• slippage  
• liquidité  
• delays  

Utilisé manuellement.

---

### 📊 Weekly Deep Audit

Compare :

EDGE detections vs vrais top gainers US  

Analyse :

• hit rate  
• lead time  
• patterns manqués  

---

### 📈 Performance Attribution

Mesure impact de chaque brique :

• events  
• timing PM  
• patterns  
• scoring  

---

### 🚨 System Guardian

Surveille :

• APIs  
• CPU/RAM  
• crash  
• données invalides  

Envoie alertes Telegram.

---

# ⚙️ Installation rapide

git clone https://github.com/ouali-GV2/GV2-EDGE.git
cd GV2-EDGE

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

Configurer :
nano config.py

▶️ Lancer en manuel

python main.py --session pm

📊 Lancer dashboard

streamlit run dashboards/streamlit_dashboard.py

⏱️ Mode production

Voir :

guide déploiement serveur
checklist cron
checklist maintenance

📅 Workflow recommandé 
Chaque jour

✔ laisser scanner tourner
✔ suivre alertes
✔ consulter dashboard

Chaque semaine

✔ weekly audit
✔ analyse patterns
Chaque mois

✔ backtest manuel
✔ ajustements légers

⚠️ Règles importantes

• ne pas sur-optimiser
• ne pas ajouter features inutiles
• toujours mesurer impact réel

📈 Objectif de performance

EDGE vise :

👉 capter tôt gros movers
👉 rendement progressif élevé
👉 drawdowns contrôlés
Pas de promesses irréalistes.

🏁 Conclusion

GV2-EDGE est un radar momentum & catalysts professionnel conçu pour:

✔ détecter tôt
✔ rester rapide
✔ évoluer proprement
Sans complexité inutile.
