import json

# Charger les paramètres du fichier de configuration
with open('configs/config.json') as f:
    config = json.load(f)

# Accéder aux paramètres de configuration
symbol = config['symbol']
stop_loss_percentage = config['stop_loss_percentage']
take_profit_percentage = config['take_profit_percentage']
trading_volume = config['trading_volume']

print(f"Configuration du trading bot : {symbol}, Stop-loss : {stop_loss_percentage*100}%, Take-profit : {take_profit_percentage*100}%")
