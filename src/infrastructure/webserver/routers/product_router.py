from typing import List, Annotated, TypeAlias, Optional

from fastapi import APIRouter, Query
from fastapi import status

from src.controllers.product_controller import ProductControllerDep
from src.domain.enums import ProductCategory
from src.infrastructure.webserver.dependencies import IntPath
from src.infrastructure.webserver.schemas.product_schemas import ProductDetail, \
    ProductCreate, ProductUpdate

router = APIRouter()


CategoryQuery: TypeAlias = Annotated[
    Optional[str],
    Query(
        default_factory=lambda: None,
        regex=f"^({'|'.join([c.value for c in ProductCategory])})$",
        description=f"Should be in list: {[c.value for c in ProductCategory]}"
    )
]
SortQuery: TypeAlias = Annotated[Optional[str], Query(default_factory=lambda: None)]


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[ProductDetail]
)
async def get_products(
    product_controller: ProductControllerDep,
    category: CategoryQuery,
    sort: SortQuery,
):
    return await product_controller.fetch_products(order_by=sort, category=category)


@router.get(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductDetail
)
async def get_product(
    product_controller: ProductControllerDep,
    product_id: IntPath,
):
    return await product_controller.fetch_product(product_id=product_id)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductDetail
)
async def create_product(
    product_controller: ProductControllerDep,
    request_data: ProductCreate
):
    return await product_controller.create_product(
        request_data=request_data.dict()
    )


@router.put(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductDetail
)
async def update_product(
    product_controller: ProductControllerDep,
    product_id: IntPath,
    request_data: ProductUpdate
):
    return await product_controller.update_product(
        product_id=product_id,
        request_data=request_data.dict()
    )


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_product(
    product_controller: ProductControllerDep,
    product_id: IntPath,
):
    return await product_controller.delete_product(
        product_id=product_id,
    )
