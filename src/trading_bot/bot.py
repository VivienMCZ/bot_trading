import sys
import os
import ccxt

# Ajouter le répertoire 'src' au chemin d'importation
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))


from utils import create_binance_connection, fetch_current_price
from strategy import create_trading_signal, calculate_moving_average
from data.data_loader import load_historical_data
from config_loader import load_config

def main():
    # Charger la configuration
    config = load_config()
    
    # Créer une connexion à Binance
    exchange = create_binance_connection()

    # Charger les données historiques
    df = load_historical_data(symbol='BTC/USDT', timeframe='1h', limit=500)
    
    # Calculer la moyenne mobile
    df = calculate_moving_average(df, window=50)
    
    # Créer un signal de trading
    signal = create_trading_signal(df)
    
    # Récupérer le prix actuel
    price = fetch_current_price(exchange, 'BTC/USDT')
    print(f"Prix actuel de BTC/USDT : {price}")

    # Prendre une décision de trading
    if signal == 1:
        print("Signal d'achat détecté. Passer un ordre d'achat.")
        try:
            # Passer un ordre d'achat
            quantity = 0.01  # Remplacer par la quantité d'achat que tu souhaites
            order = exchange.create_market_buy_order('BTC/USDT', quantity)
            print(f"Ordre d'achat passé avec succès : {order}")
        except ccxt.BaseError as e:
            print(f"Erreur lors de la passation de l'ordre d'achat : {str(e)}")
        
    elif signal == -1:
        print("Signal de vente détecté. Passer un ordre de vente.")
        try:
            # Passer un ordre de vente
            quantity = 0.01  # Remplacer par la quantité de vente que tu souhaites
            order = exchange.create_market_sell_order('BTC/USDT', quantity)
            print(f"Ordre de vente passé avec succès : {order}")
        except ccxt.BaseError as e:
            print(f"Erreur lors de la passation de l'ordre de vente : {str(e)}")
    else:
        print("Aucun signal de trading.")

if __name__ == "__main__":
    main()