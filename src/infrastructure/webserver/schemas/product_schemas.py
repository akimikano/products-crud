from pydantic import BaseModel, Extra

from src.domain.enums import ProductCategory


class Base(BaseModel):
    class Config:
        orm_mode = True
        extra = Extra.forbid


class ProductBase(Base):
    name: str
    description: str
    price: int
    category: ProductCategory


class ProductDetail(ProductBase):
    id: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass
