from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:12345@localhost:3306/food_delivery_analysis")

try:
    with engine.connect() as conn:
        print("Python successfully connected to MySQL!")
except Exception as e:
    print("Connection failed")
    print(e)