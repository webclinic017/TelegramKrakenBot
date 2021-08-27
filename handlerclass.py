# Enum for workflow handler
from enum import Enum, auto
class WorkflowEnum(Enum):
    TRADE_BUY_SELL = auto()
    TRADE_CURRENCY = auto()
    TRADE_SELL_ALL_CONFIRM = auto()
    TRADE_PRICE = auto()
    TRADE_VOL_TYPE = auto()
    TRADE_VOLUME = auto()
    TRADE_VOLUME_ASSET = auto()
    TRADE_CONFIRM = auto()
    ORDERS_CLOSE = auto()
    ORDERS_CLOSE_ORDER = auto()
    PRICE_CURRENCY = auto()
    VALUE_CURRENCY = auto()
    BOT_SUB_CMD = auto()
    CHART_CURRENCY = auto()
    TRADES_NEXT = auto()
    FUNDING_CURRENCY = auto()
    FUNDING_CHOOSE = auto()
    WITHDRAW_WALLET = auto()
    WITHDRAW_VOLUME = auto()
    WITHDRAW_CONFIRM = auto()
    SETTINGS_CHANGE = auto()
    SETTINGS_SAVE = auto()
    SETTINGS_CONFIRM = auto()
    #ttcode
    ALERTON_OK = auto()
    ALERTON_CHEK = auto()
    ALERT_ACTIVE = auto()
    ALERT_NEW_REMOVE_ALL = auto()
    ALERT_CURRENCY = auto()
    ALERT_CONFIRM = auto()
    ALERT_PRICE = auto()
    ALERTS_CLOSE = auto()
    ALERTS_CLOSE_ALLS = auto()
    ALERTS_CLOSE_ALERT = auto()
    
# Enum for keyboard buttons
class KeyboardEnum(Enum):
    BUY = auto()
    SELL = auto()
    VOLUME = auto()
    ALL = auto()
    YES = auto()
    NO = auto()
    CANCEL = auto()
    CLOSE_ORDER = auto()
    CLOSE_ALL = auto()
    UPDATE_CHECK = auto()
    UPDATE = auto()
    RESTART = auto()
    SHUTDOWN = auto()
    NEXT = auto()
    DEPOSIT = auto()
    WITHDRAW = auto()
    SETTINGS = auto()
    API_STATE = auto()
    MARKET_PRICE = auto()
    #ttcode
 
    NEW_ALERT = auto()
    NEW_ALERT_UP = auto()
    NEW_ALERT_DOWN = auto()
    REMOVE_ALERT = auto()
    REMOVE_ALL_ALERTS = auto()
    ALL_ALERT = auto()
    VIEW_ALL_ALERTS = auto()
    CONFIRM_ALERT = auto()

    CLOSE_ALERT  = auto()
    CLOSE_ALL_ALERTS = auto()
    #CLOSE_ALL = auto()
    def clean(self):
        return self.name.replace("_", " ")