class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        prod_file = open(self.__file_name, 'r')
        products = prod_file.read()
        prod_file.close()
        return products

    def add(self, product):
        prod_file = open(self.__file_name, 'a')
        list_of_prod = self.get_products()

        if str(product) not in list_of_prod:
            prod_file.write(str(product) + '\n')
        else:
            print(f'Продукт {product.name} уже есть в магазине')
        prod_file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Rabbit',2.56,'Meat')
print(p2)  # __str__

s1.add(p1)
s1.add(p2)
s1.add(p3)
s1.add(p4)
print(s1.get_products())