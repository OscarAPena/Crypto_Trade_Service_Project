# Mock the kraken API

from pydantic import BaseModel
from datetime import datetime
from typing import List

class Trade(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """ 
    pair:str
    price:float
    volume:float
    timestamp: datetime
    timestamp_ms: int  

class KrakenMockAPI:
    def __init__(self, pair:str):
        self.pair = pair

    def get_trades(self) -> List(Trade):
        """Returns a list of mock trades made a small change to check.

        Args:
            self (_type_): 

        Returns:
            _type_: List of trades
        """
        mock_trades=[
            Trade(air=self.pair, price=0.5117, volume=40.0, timestamp=datetime(2023,9,25,7,49,37,708706), timestamp_ms=1000),
            Trade(pair=self.pair, price=0.5317, volume=40.0, timestamp=datetime(2023,9,25,7,49,37,708706), timestamp_ms=1000)
                  ]
        

        return mock_tades