# 🚀 GV2-EDGE — Advanced Momentum & Event-Driven Trading Radar

GV2-EDGE est un système automatisé conçu pour détecter **très tôt** les top gainers small caps du marché américain (hors OTC), idéalement avant ou au tout début de leurs hausses majeures.

🎯 Objectif principal :
> Capter les mouvements explosifs (+50%, +100%, +200%) avant qu’ils ne se produisent, avec un système rapide, robuste et orienté performance réelle.

---

## 🧠 Philosophie du projet

GV2-EDGE repose sur des principes utilisés par les traders momentum professionnels :

✅ Structure du marché avant indicateurs  
✅ Momentum réel prix + volume  
✅ Catalysts concrets (news, earnings, FDA, M&A)  
✅ Pré-market comme zone clé de détection  
✅ Simplicité robuste (éviter IA lourde & overfitting)  
✅ Amélioration continue par audit réel

❌ Pas d’indicateurs inutiles  
❌ Pas de deep learning instable  
❌ Pas de complexité excessive  

---

## 📊 Fonctionnement global (vue d’ensemble)

1. Construction de l’univers small caps US  
2. Détection des événements catalyseurs  
3. Analyse sentiment & buzz  
4. Calcul des features marché  
5. Analyse des patterns structurels  
6. Scoring intelligent  
7. Confluence des signaux  
8. Génération BUY / BUY_STRONG / HOLD  
9. Gestion du risque et positions  
10. Dashboard & alertes live  
11. Audits et amélioration continue  

---

# 🧱 Briques principales

---

## 🌍 Universe Loader

Construit dynamiquement l’univers des small caps US :

• filtrage capitalisation (<2B)  
• exclusion OTC  
• volume minimum  
• prix cohérents  

Sources gratuites : Finnhub, IBKR.

📤 Sortie : `data/universe.csv`

---

## 📅 Event Hub (multi-source)

Centralise tous les catalysts importants :

✔ Earnings  
✔ FDA approvals  
✔ M&A / acquisitions  
✔ Sector news  
✔ Breaking news  
✔ Analyst actions  

Les événements sont :

• récupérés via APIs/RSS  
• nettoyés  
• normalisés  

Puis envoyés au NLP.

---

## 🧠 NLP Event Parser

Utilise Grok pour :

• extraire les tickers concernés  
• classer le type d’événement  
• estimer l’impact potentiel  
• éliminer le bruit  

📤 Sortie JSON propre pour le scoring.

---

## 📣 Social Engine

Analyse :

### X/Twitter sentiment (via Grok)
→ intérêt soudain du marché

### News buzz
→ volume anormal d’articles

Objectif : mesurer la pression d’attention.

---

## 📈 Feature Engine

Calcule les signaux marché clés :

### Momentum & volume
• gap %  
• volume spike  
• velocity  

### Pré-market
• PM high/low  
• force PM  

### Structure
• VWAP deviation  
• niveaux clés  

### Patterns
• breakouts  
• consolidations  
• compressions  
• pullbacks  
• continuations  

---

## 🧮 Monster Score

Score principal combinant :

- momentum  
- volume  
- events  
- social buzz  
- patterns  

Chaque facteur est pondéré intelligemment.

📈 Plus le score est élevé → plus forte probabilité de gros mover.

---

## 🔗 Ensemble Engine

Mesure la confluence entre :

• events  
• momentum  
• patterns  
• timing  

Renforce la conviction sur les meilleurs setups.

---

## 🚦 Signal Engine

Transforme les scores en décisions claires :

| Signal | Signification |
|-------|-------------|
| BUY_STRONG | Setup explosif |
| BUY | Setup solide |
| HOLD | Ignorer |

---

## ⚖️ Portfolio Engine

Gère automatiquement :

• taille de position (selon capital & risque)  
• stop loss dynamique (ATR/structure)  
• trailing stops  
• limite de positions ouvertes  
• protection drawdown  

---

## 📊 Dashboard Streamlit

Interface live affichant :

✔ signaux BUY / BUY_STRONG  
✔ Monster Scores  
✔ heatmaps momentum  
✔ niveaux PM/HOD/VWAP  
✔ performance  
✔ santé système  

---

## 🚨 Telegram Alerts

Envoie instantanément :

• BUY_STRONG  
• BUY  
• alertes techniques (API, crash, data)

---

## 🧪 Backtest Engine EDGE

Backtests réalistes :

• simulation timeline  
• slippage  
• liquidité  
• stops réels  

Utilisé manuellement pour éviter sur-optimisation.

---

## 📊 Weekly Deep Audit

Chaque semaine :

✔ récupère vrais top gainers US  
✔ compare avec détections EDGE  
✔ mesure :

• hit rate  
• lead time  
• movers manqués  
• patterns communs  

🎯 Sert à améliorer continuellement le système.

---

## 📈 Performance Attribution

Analyse ce qui rapporte vraiment :

• events  
• timing PM  
• patterns  
• momentum  

Permet d’optimiser intelligemment les briques.

---

## 🚨 System Guardian

Surveille :

• santé APIs  
• CPU/RAM  
• crashs  
• données invalides  

Envoie alertes Telegram en cas de problème.

---

# ⚙️ Installation rapide

```bash
git clone https://github.com/ouali-GV2/GV2-EDGE.git
cd GV2-EDGE

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
