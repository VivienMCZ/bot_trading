# /src/data/data_loader.py

import pandas as pd
import ccxt
from utils import create_binance_connection

def load_historical_data(symbol='BTC/USDT', timeframe='1h', limit=500):
    """
    Charge les données historiques de Binance (OHLCV).
    :param symbol: Symbole de la paire de trading (ex: 'BTC/USDT')
    :param timeframe: Intervalle de temps (par exemple, '1h' pour une heure)
    :param limit: Nombre de bougies à récupérer
    :return: DataFrame contenant les données historiques
    """
    exchange = create_binance_connection()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
    
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df
