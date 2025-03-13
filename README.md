
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
   ```

2. Créez un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur macOS/Linux
   venv\Scripts\activate     # Sur Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Créez un fichier `.env` à la racine de votre projet avec vos clés API Binance :
   ```
   BINANCE_API_KEY=VotreAPIKey
   BINANCE_API_SECRET=VotreAPISecret
   ```

### Utilisation

1. Exécutez le bot pour commencer le trading :
   ```bash
   python src/trading_bot/bot.py
   ```

### Structure du projet

```
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

### Détails des fichiers

1. **`config.json` (dans le dossier `configs/`)** : Ce fichier contient les paramètres de configuration pour le bot, tels que la paire de trading, les seuils de stop-loss et take-profit, ainsi que le volume de trading.

2. **`data_loader.py`** : Ce fichier contient la logique pour charger les données historiques (OHLCV) de Binance, nécessaires à l'analyse technique.

3. **`strategy.py`** : Ce fichier implémente la logique des stratégies de trading. Par exemple, il calcule la moyenne mobile et génère des signaux d'achat ou de vente.

4. **`bot.py`** : Le fichier principal qui exécute le bot. Il charge la configuration, récupère les données historiques, applique la stratégie et prend des décisions de trading.

5. **`config_loader.py`** : Ce fichier charge les paramètres de configuration depuis le fichier `config.json`.

6. **`utils.py`** : Contient des fonctions utilitaires, telles que la connexion à l'API Binance via `ccxt` et la récupération des prix en temps réel.

## Exécution du bot

Une fois le projet installé et configuré, vous pouvez exécuter le bot en utilisant la commande suivante :

```bash
python src/trading_bot/bot.py
```

Le bot affichera des informations sur la configuration actuelle, le prix actuel de la paire de trading et prendra des décisions de trading en fonction des signaux générés.

## Auteurs

- Vivien M. 

## License

Ce projet est sous la licence MIT.
