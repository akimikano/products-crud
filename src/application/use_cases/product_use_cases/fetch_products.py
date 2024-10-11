from src.application.exceptions import NotFound
from src.application.repositories.product_repository import IProductRepository
from src.application.use_cases.base_use_case import BaseUseCase


class FetchProductsUseCase(BaseUseCase):
    def __init__(self, *, product_repository: IProductRepository):
        self.product_repository = product_repository

    async def execute(self, order_by: str = None, **filters):
        return await self.product_repository.fetch_many(order_by=order_by, **filters)
