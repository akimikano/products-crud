from dataclasses import dataclass
from typing import Optional


@dataclass
class ProductEntity:
    id: Optional[int]
    name: str
    description: str
    price: int
    category: str
