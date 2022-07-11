from sqlalchemy.orm import declarative_base
from sqlalchemy import INTEGER, Column, VARCHAR, ForeignKey

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(INTEGER, primary_key=True)
    name = Column(VARCHAR(20))
    price = Column(INTEGER)

    def __str__(self):
        return f'id: {self.id}, name: {self.name}, price: {self.price}'

class Order(Base):
    __tablename__ = "orders"
    id = Column(INTEGER, primary_key=True)
    product_id = Column(INTEGER, ForeignKey("products.id"))
    quantity = Column(INTEGER)

    def __str__(self):
        return f'id: {self.id}, product_id: {self.product_id}, quantity: {self.quantity}'


