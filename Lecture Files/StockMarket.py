from abc import ABC, abstractmethod

class StockMarket(ABC):
    '''A class to define a stock market.'''
    def __init__(self, share_id, num_available, price_per_unit):
        '''(StockMarket, str, int, float) -> NoneType
        Defines a new stock market'''
        self._share_ids = share_num
        self._num_available = num_available
        self._price_per_unit = price_per_unit
        
    def buy(self, share_num, num):
        '''(StockMarket'''
        
        
        