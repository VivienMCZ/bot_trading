import json
import os

def load_config(config_file='configs/config.json'):
    """
    Charge les paramètres de configuration depuis un fichier JSON.
    :param config_file: Le chemin vers le fichier de configuration (par défaut 'configs/config.json')
    :return: Dictionnaire contenant les paramètres du fichier JSON.
    """
    # Vérifier si le fichier existe
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Le fichier de configuration '{config_file}' n'a pas été trouvé.")
    
    # Charger les données depuis le fichier JSON
    with open(config_file) as f:
        config = json.load(f)

    # Vérification des clés nécessaires dans la configuration
    required_keys = ['symbol', 'stop_loss_percentage', 'take_profit_percentage', 'trading_volume']
    for key in required_keys:
        if key not in config:
            raise KeyError(f"Le paramètre '{key}' est manquant dans le fichier de configuration.")

    # Affichage de la configuration (optionnel)
    print(f"Configuration du trading bot : {config['symbol']}, Stop-loss : {config['stop_loss_percentage']*100}%, Take-profit : {config['take_profit_percentage']*100}%")

    return config

# Utilisation de la fonction pour charger la configuration
config = load_config()

# Exemple d'utilisation des valeurs
symbol = config['symbol']
stop_loss_percentage = config['stop_loss_percentage']
take_profit_percentage = config['take_profit_percentage']
trading_volume = config['trading_volume']
