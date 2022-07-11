from pythonProject.Repository_9.hillel_lessons.sql_postgres.sql_python_lesson.postgre.session import session
from pythonProject.Repository_9.hillel_lessons.sql_postgres.sql_python_lesson.postgre.models.products_orders import Product, Order

class ProductRepository:
    def __init__(self):
        self.__session = session

    def insert_one(self, product: Product):
        self.__session.add(product)
        self.__session.commit()

class OrderRepository:
    def __init__(self):
        self.__session = session

    def insert_one(self, order: Order):
        self.__session.add(order)
        self.__session.commit()

