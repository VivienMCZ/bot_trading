# /tests/test_bot.py

import unittest
import pandas as pd
from src.data.data_loader import load_historical_data
from src.trading_bot.strategy import create_trading_signal
from src.trading_bot.utils import fetch_current_price
from src.trading_bot.logger import setup_logger

class TestTradingBot(unittest.TestCase):
    
    def test_load_historical_data(self):
        """
        Teste la fonction de chargement des données historiques.
        """
        # Charger les données historiques pour la paire BTC/USDT
        df = load_historical_data(symbol='BTC/USDT', timeframe='1h', limit=10)
        
        # Vérifier que le DataFrame n'est pas vide
        self.assertFalse(df.empty, "Le DataFrame est vide.")
        
        # Vérifier que les colonnes attendues sont présentes
        self.assertIn('timestamp', df.columns, "La colonne 'timestamp' est absente.")
        self.assertIn('open', df.columns, "La colonne 'open' est absente.")
        self.assertIn('high', df.columns, "La colonne 'high' est absente.")
        self.assertIn('low', df.columns, "La colonne 'low' est absente.")
        self.assertIn('close', df.columns, "La colonne 'close' est absente.")
        self.assertIn('volume', df.columns, "La colonne 'volume' est absente.")

    def test_create_trading_signal(self):
        """
        Teste la création d'un signal de trading basé sur la moyenne mobile.
        """
        # Simuler des données pour tester la stratégie
        data = {
            'timestamp': ['2025-03-13 10:00', '2025-03-13 11:00', '2025-03-13 12:00'],
            'close': [50000, 50500, 51000]
        }
        df = pd.DataFrame(data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])

        # Appliquer la stratégie (moyenne mobile)
        df = create_trading_signal(df)
        
        # Vérifier que le signal est correct
        self.assertIn('signal', df.columns, "La colonne 'signal' est absente.")
        
        # Tester si le signal est 1 (acheter) ou -1 (vendre)
        self.assertIn(df['signal'].iloc[-1], [1, -1, 0], "Le signal de trading est incorrect.")

    def test_fetch_current_price(self):
        """
        Teste la fonction qui récupère le prix actuel de la crypto-monnaie.
        """
        # Simuler une connexion à l'API Binance et récupérer le prix
        mock_exchange = None  # Remplacer par une connexion réelle ou un mock
        price = fetch_current_price(mock_exchange, 'BTC/USDT')
        
        # Vérifier que le prix est un nombre
        self.assertIsInstance(price, (int, float), "Le prix doit être un nombre.")
        
if __name__ == "__main__":
    unittest.main()
