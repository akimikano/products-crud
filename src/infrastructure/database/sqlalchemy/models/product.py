from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum, Integer

from src.domain.enums import ProductCategory
from src.infrastructure.database.sqlalchemy.models.base_model import Base


class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String(255))
    price: Mapped[int] = mapped_column(Integer)
    category: Mapped[str] = mapped_column(Enum(ProductCategory))
