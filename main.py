class Product:
    __id_counter = 1

    def __init__(self, name, price):
        self.__id = Product.__id_counter
        Product.__id_counter += 1
        self.__name = name
        self.__price = price

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    def __str__(self):
        return f"Product(id={self.__id}, name='{self.__name}', price={self.__price})"


class Seller:
    __id_counter = 1

    def __init__(self, name):
        self.__id = Seller.__id_counter
        Seller.__id_counter += 1
        self.__name = name
        self.__products = []
        self.__balance = 0

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def products(self):
        return self.__products

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product_id):
        self.__products = [product for product in self.__products if product.id != product_id]

    def __str__(self):
        return f"Seller(id={self.__id}, name='{self.__name}', balance={self.__balance}, products={[str(product) for product in self.__products]})"


class Customer:
    __id_counter = 1

    def __init__(self, name, balance):
        self.__id = Customer.__id_counter
        Customer.__id_counter += 1
        self.__name = name
        self.__balance = balance

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        self.__balance = balance

    def __str__(self):
        return f"Customer(id={self.__id}, name='{self.__name}', balance={self.__balance})"


class Order:
    __id_counter = 1

    def __init__(self, customer, product, seller, delivery_address):
        self.__id = Order.__id_counter
        Order.__id_counter += 1
        self.__customer = customer
        self.__product = product
        self.__seller = seller
        self.__delivery_address = delivery_address
        self.__process_order()

    @property
    def id(self):
        return self.__id

    @property
    def customer(self):
        return self.__customer

    @property
    def product(self):
        return self.__product

    @property
    def seller(self):
        return self.__seller

    @property
    def delivery_address(self):
        return self.__delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        self.__delivery_address = delivery_address

    def __process_order(self):
        if self.__customer.balance >= self.__product.price:
            self.__customer.balance -= self.__product.price
            self.__seller.balance += self.__product.price
        else:
            raise ValueError("Insufficient funds")

    def __str__(self):
        return (f"Order(id={self.__id}, customer={self.__customer.name}, product={self.__product.name}, "
                f"seller={self.__seller.name}, delivery_address='{self.__delivery_address}')")


def main():
    try:
        # Create seller
        seller_name = input("Enter seller's name: ")
        seller = Seller(seller_name)

        # Add products
        while True:
            product_name = input("Enter product name (or 'stop' to finish): ")
            if product_name.lower() == 'stop':
                break
            product_price = float(input(f"Enter price for '{product_name}': "))
            product = Product(product_name, product_price)
            seller.add_product(product)

        # Create customer
        customer_name = input("Enter customer's name: ")
        customer_balance = float(input(f"Enter balance for '{customer_name}': "))
        customer = Customer(customer_name, customer_balance)

        # Show products
        print("\nAvailable products:")
        for product in seller.products:
            print(product)

        # Create order
        product_id = int(input("Enter product ID to purchase: "))
        selected_product = None
        for product in seller.products:
            if product.id == product_id:
                selected_product = product
                break

        if selected_product is None:
            print("Product with this ID not found.")
            return

        delivery_address = input("Enter delivery address: ")
        order = Order(customer, selected_product, seller, delivery_address)

        # Display information
        print("\nOrder successfully created:")
        print(order)
        print("\nCustomer information after order:")
        print(customer)
        print("\nSeller information after order:")
        print(seller)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
