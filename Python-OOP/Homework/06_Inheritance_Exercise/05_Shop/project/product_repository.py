class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return product
        return None

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = []
        for product in self.products:
            result.append(f"{product.name}: {product.quantity}")
        return "\n".join(result)