# /src/trading_bot/strategy.py

import pandas as pd
import pandas_ta as ta

def calculate_moving_average(df, window=50):
    df['ma'] = df['close'].rolling(window=window).mean()
    return df

def calculate_rsi(df, window=14):
    df['rsi'] = ta.rsi(df['close'], length=window)
    return df

def calculate_macd(df):
    df['macd'], df['macd_signal'], df['macd_hist'] = ta.macd(df['close'])
    return df

def create_trading_signal(df):
    if df['close'].iloc[-1] > df['ma'].iloc[-1]:
        return 1  # Acheter
    elif df['close'].iloc[-1] < df['ma'].iloc[-1]:
        return -1  # Vendre
    else:
        return 0  # Aucune action
