from src.application.repositories.product_repository import IProductRepository
from src.application.use_cases.base_use_case import BaseUseCase
from src.domain.entities.product_entity import ProductEntity


class CreateProductUseCase(BaseUseCase):
    def __init__(self, *, product_repository: IProductRepository):
        self.product_repository = product_repository

    async def execute(self, request_data: dict):
        product = ProductEntity(
            id=None,
            **request_data
        )

        await self.product_repository.save_one(entity=product)
        await self.product_repository.save_changes()
        return product
