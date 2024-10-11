from sqlalchemy import desc, asc

from src.application.repositories.product_repository import IProductRepository
from src.domain.entities.product_entity import ProductEntity
from src.infrastructure.database.sqlalchemy.models import ProductModel
from src.infrastructure.database.sqlalchemy.repositories.base_repository import \
    BaseAsyncRepository


class ProductRepository(BaseAsyncRepository, IProductRepository):
    model = ProductModel

    @staticmethod
    def to_entity(db_instance: ProductModel):
        return ProductEntity(
            id=db_instance.id,
            name=db_instance.name,
            description=db_instance.description,
            price=db_instance.price,
            category=db_instance.category
        )

    def query(self, order_by: str = None, **filters):
        query = super().query(**filters)

        if order_by == "price":
            query = query.order_by(asc(ProductModel.price))
        if order_by == "-price":
            query = query.order_by(desc(ProductModel.price))
        else:
            query = query.order_by(desc(ProductModel.id))

        return query

    async def fetch_many(self, order_by: str = None, **filters):
        query = self.query(order_by=order_by, **filters)
        result = await self.db_connection.execute(query)
        db_instances = result.scalars().all()
        return [self.to_entity(db_instance) for db_instance in db_instances]
