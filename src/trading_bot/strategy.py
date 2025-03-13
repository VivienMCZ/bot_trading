# /src/trading_bot/strategy.py

import pandas as pd

def calculate_moving_average(df, window=50):
    """
    Calcul de la moyenne mobile simple sur une période donnée.
    :param df: DataFrame contenant les prix historiques
    :param window: Période de la moyenne mobile (par défaut 50)
    :return: DataFrame avec la colonne 'ma' pour la moyenne mobile
    """
    df['ma'] = df['close'].rolling(window=window).mean()
    return df

def create_trading_signal(df):
    """
    Crée un signal de trading basé sur la croisement du prix avec la moyenne mobile.
    :param df: DataFrame contenant les données historiques avec la moyenne mobile
    :return: Signal d'achat (1) ou de vente (-1)
    """
    if df['close'].iloc[-1] > df['ma'].iloc[-1]:
        return 1  # Acheter
    elif df['close'].iloc[-1] < df['ma'].iloc[-1]:
        return -1  # Vendre
    else:
        return 0  # Aucune action
