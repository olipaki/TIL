from product_adv.schemas.product import Product


class ProductRepository:
    def __init__(self):
        # 데이터베이스 연결
        self.products = []
        self.product_id = 0

    def save(self, new_product: Product):
        self.product_id += 1
        new_product.id = self.product_id

        self.products.append(new_product)

        return new_product

    def find_by_id(self, id: int):
        for product in self.products:
            # 해당하는 id가 있는 경우에는 post를 return.
            if product.id == id:
                return product
        return None


product_repository = ProductRepository()
