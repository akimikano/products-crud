from src.application.exceptions import NotFound
from src.application.repositories.product_repository import IProductRepository
from src.application.use_cases.base_use_case import BaseUseCase


class FetchProductUseCase(BaseUseCase):
    def __init__(self, *, product_repository: IProductRepository):
        self.product_repository = product_repository

    async def execute(self, *, product_id: int):
        db_product = await self.product_repository.fetch_one(
            pk=product_id
        )
        if not db_product:
            raise NotFound

        return db_product
