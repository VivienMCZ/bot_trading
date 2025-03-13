import logging

# Configuration du logger
def setup_logger():
    """
    Configure et retourne un logger pour le bot de trading.
    """
    # Créer un logger avec un nom spécifique
    logger = logging.getLogger('TradingBot')
    logger.setLevel(logging.INFO)  # Niveau de log: INFO pour les messages généraux
    
    # Créer un handler pour écrire les logs dans un fichier
    file_handler = logging.FileHandler('trading_bot.log')
    file_handler.setLevel(logging.INFO)  # Niveau du handler: INFO
    
    # Créer un format pour les logs (date, niveau, message)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Ajouter le handler au logger
    logger.addHandler(file_handler)
    
    return logger

# Créer le logger global
logger = setup_logger()

# Exemple d'utilisation du logger
def log_trade_signal(signal):
    """
    Logge le signal de trading.
    """
    if signal == 1:
        logger.info("Signal d'achat détecté.")
    elif signal == -1:
        logger.info("Signal de vente détecté.")
    else:
        logger.info("Aucun signal de trading.")
