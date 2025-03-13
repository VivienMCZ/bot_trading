# /src/trading_bot/utils.py

import ccxt
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

def create_binance_connection():
    # Récupérer les clés API depuis les variables d'environnement
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    # Connexion à l'API Binance avec ccxt
    exchange = ccxt.binance({
        'apiKey': api_key,
        'secret': api_secret,
    })
    
    return exchange

def fetch_current_price(exchange, symbol='BTC/USDT'):
    # Récupérer les données de marché pour le symbole
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']
