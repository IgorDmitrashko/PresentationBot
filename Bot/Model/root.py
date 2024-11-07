from dataclasses import dataclass
from typing import Any


@dataclass
class Root:
    ccy: str
    base_ccy: str
    buy: str
    sale: str

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _ccy = str(obj.get("ccy"))
        _base_ccy = str(obj.get("base_ccy"))
        _buy = str(obj.get("buy"))
        _sale = str(obj.get("sale"))
        return Root(_ccy, _base_ccy, _buy, _sale)
