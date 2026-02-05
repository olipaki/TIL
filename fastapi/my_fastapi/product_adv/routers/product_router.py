from fastapi import APIRouter, status, Path
from product_adv.schemas.product import ProductCreate, ProductDetailResponse
from product_adv.services.product_service import product_service
from typing import Annotated

router = APIRouter(prefix="/product-adv")


# 클라이언트로부터 데이터를 입력받아서 저장하는 역할.
# 어떤 데이터를 입력받지? -> ProductCreate
@router.post("", status_code=status.HTTP_201_CREATED)
def create_product(data: ProductCreate):
    return product_service.create_product(data)


@router.get("/{id}", response_model=ProductDetailResponse)
def read_product_by_id(id: Annotated[int, Path(ge=1)]):
    return product_service.read_product_by_id(id)
