# /src/trading_bot/risk_management.py

def calculate_stop_loss(entry_price, stop_loss_percentage):
    return entry_price * (1 - stop_loss_percentage)

def calculate_take_profit(entry_price, take_profit_percentage):
    return entry_price * (1 + take_profit_percentage)

def calculate_position_size(balance, risk_percentage, stop_loss_distance):
    risk_amount = balance * risk_percentage
    position_size = risk_amount / stop_loss_distance
    return position_size
