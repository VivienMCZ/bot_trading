# /src/trading_bot/backtester.py

import pandas as pd
from strategy import create_trading_signal

def backtest_strategy(df, initial_balance=1000):
    balance = initial_balance
    position = 0
    for i in range(1, len(df)):
        signal = create_trading_signal(df.iloc[:i+1])
        if signal == 1:  # Signal d'achat
            position = balance / df['close'].iloc[i]
            balance = 0
        elif signal == -1:  # Signal de vente
            if position > 0:
                balance = position * df['close'].iloc[i]
                position = 0
    return balance
