from pythonProject.Repository_9.hillel_lessons.sql_postgres.sql_python_lesson.postgre.models.products_orders import Product, Order
from pythonProject.Repository_9.hillel_lessons.sql_postgres.sql_python_lesson.postgre.user_repository.products_orders_repository import ProductRepository, OrderRepository
from pythonProject.Repository_9.hillel_lessons.sql_postgres.sql_python_lesson.postgre.session import session

order_repo = OrderRepository()
product_repo = ProductRepository()

product_repo.insert_one(Product(id=1, name='coffee', price=14))
product_repo.insert_one(Product(id=2, name='tea', price=15))
product_repo.insert_one(Product(id=3, name='juice', price=16))
product_repo.insert_one(Product(id=4, name='milk', price=17))
product_repo.insert_one(Product(id=5, name='whisky', price=50))

order_repo.insert_one(Order(id=1, product_id=1, quantity=22))
order_repo.insert_one(Order(id=2, product_id=2, quantity=89))
order_repo.insert_one(Order(id=3, product_id=3, quantity=56))
order_repo.insert_one(Order(id=4, product_id=4, quantity=12))
order_repo.insert_one(Order(id=5, product_id=5, quantity=63))

result = session.query(Product, Order).join(Order).all()
for products, orders in result:
    print(products.name, products.price, orders.quantity, products.price * orders.quantity)



