from typing import TypeAlias, Annotated

from fastapi import Depends

from src.application.use_cases.product_use_cases.create_product import \
    CreateProductUseCase
from src.application.use_cases.product_use_cases.delete_product import \
    DeleteProductUseCase
from src.application.use_cases.product_use_cases.fetch_product import \
    FetchProductUseCase
from src.application.use_cases.product_use_cases.fetch_products import \
    FetchProductsUseCase
from src.application.use_cases.product_use_cases.update_product import \
    UpdateProductUseCase
from src.infrastructure.database.sqlalchemy.config import get_db_session
from src.infrastructure.database.sqlalchemy.repositories.product_repository import \
    ProductRepository


class ProductController:
    def __init__(
        self,
        db_connection=Depends(get_db_session)
    ):
        self.product_repository = ProductRepository(
            db_connection=db_connection
        )

    async def fetch_products(self, order_by: str = None, **filters):
        fetch_products_use_case = FetchProductsUseCase(
            product_repository=self.product_repository
        )
        return await fetch_products_use_case.execute(order_by=order_by, **filters)

    async def fetch_product(self, *, product_id: int):
        fetch_product_use_case = FetchProductUseCase(
            product_repository=self.product_repository
        )
        return await fetch_product_use_case.execute(product_id=product_id)

    async def create_product(self, *, request_data: dict):
        create_product_use_case = CreateProductUseCase(
            product_repository=self.product_repository
        )
        return await create_product_use_case.execute(request_data=request_data)

    async def update_product(self, *, product_id: int, request_data: dict):
        update_product_use_case = UpdateProductUseCase(
            product_repository=self.product_repository
        )
        return await update_product_use_case.execute(
            product_id=product_id,
            request_data=request_data
        )

    async def delete_product(self, *, product_id: int):
        delete_product_use_case = DeleteProductUseCase(
            product_repository=self.product_repository
        )
        return await delete_product_use_case.execute(product_id=product_id)


ProductControllerDep: TypeAlias = Annotated[ProductController, Depends(ProductController)]
