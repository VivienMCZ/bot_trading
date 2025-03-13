# /src/trading_bot/bot.py

from utils import create_binance_connection, fetch_current_price

def main():
    # Créer une connexion à Binance
    exchange = create_binance_connection()
    
    # Récupérer et afficher le prix actuel
    price = fetch_current_price(exchange, 'BTC/USDT')
    print(f"Prix actuel de BTC/USDT : {price}")

if __name__ == "__main__":
    main()
