from product_adv.schemas.product import ProductCreate, Product
from product_adv.repositories.product_repository import product_repository
from fastapi import HTTPException, status


class ProductService:
    def create_product(self, data: ProductCreate):
        new_product = Product(
            name=data.name,
            price=data.price,
            discount_price=data.discount_price,
            stock=data.stock,
            category=data.category,
        )
        return product_repository.save(new_product)

    def read_product_by_id(self, id: int):
        product = product_repository.find_by_id(id)
        if not product:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        # product: Product
        # return: ProductDetail에 해당하는 값

        # if product.stock:  # 없다 즉 0, "", [] => false로 처리
        #     is_soldout = False
        # else:
        #     is_soldout = True
        # # 삼항연산자.
        # is_soldout = False if product.stock else True

        return {
            "id": product.id,
            "name": product.name,
            "final_price": product.price - product.discount_price,
            "category": product.category,
            "is_soldout": False if product.stock else True,
            "stock": product.stock,
        }


product_service = ProductService()
