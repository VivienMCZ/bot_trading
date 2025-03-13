# Bot Trading

Ce projet est un bot de trading automatisé utilisant l'API Binance pour effectuer des transactions de trading sur des paires de crypto-monnaies. Le bot analyse les données historiques, applique des stratégies de trading et prend des décisions d'achat ou de vente en fonction des signaux générés.

## Fonctionnalités

- Connexion à l'API Binance pour récupérer les données de marché en temps réel.
- Chargement des données historiques (OHLCV) pour effectuer des analyses.
- Calcul des indicateurs techniques (comme les moyennes mobiles).
- Génération de signaux d'achat ou de vente en fonction de la stratégie définie.
- Passage d'ordres d'achat et de vente sur Binance en fonction des signaux.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les dépendances nécessaires et configuré vos clés API Binance.

### Installation

1. Clonez ce repository :
   ```bash
   git clone https://github.com/vivienmcz/bot_trading.git
   cd bot_trading
Créez un environnement virtuel (recommandé) :

```bash
    python -m venv venv
    source venv/bin/activate  # Sur macOS/Linux
    venv\Scripts\activate     # Sur Windows
    Installez les dépendances :

```bash
    pip install -r requirements.txt
    Créez un fichier .env à la racine de votre projet avec vos clés API Binance :

    BINANCE_API_KEY=VotreAPIKey
    BINANCE_API_SECRET=VotreAPISecret

Utilisation
Exécutez le bot pour commencer le trading :
```bash
    python src/trading_bot/bot.py
    Structure du projet
```

```bash

    vivienmcz-bot_trading/
        ├── README.md               # Documentation du projet
        ├── requirements.txt        # Liste des dépendances
        ├── .env                    # Clés API Binance (ne pas versionner)
        ├── configs/
        │   └── config.json         # Configuration du bot (paramètres de trading)
        └── src/
            ├── data/
            │   └── data_loader.py  # Chargement des données historiques
            └── trading_bot/
                ├── bot.py         # Script principal pour exécuter le bot
                ├── config_loader.py # Chargement de la configuration
                ├── strategy.py     # Stratégies de trading (indicateurs, signaux)
                └── utils.py        # Utilitaires divers (connexion Binance, etc.)
```
    Auteurs
    Vivien M. (votre nom ici)

    License
    Ce projet est sous la licence MIT.