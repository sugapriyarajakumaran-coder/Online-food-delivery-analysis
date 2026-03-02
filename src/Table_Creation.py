from sqlalchemy import (
    String, Integer, Float, DateTime, Column, Boolean, DECIMAL
)
from sqlalchemy.orm import declarative_base
from mysql_connection import engine

Base = declarative_base()

class Orders(Base):
    __tablename__ = "orders"

    Order_ID = Column(String(50), primary_key=True, nullable=False)
    Customer_ID = Column(String(50))
    Customer_Age = Column(Integer)
    Customer_Gender = Column(String(20))
    City = Column(String(100))
    Area = Column(String(100))
    Restaurant_ID = Column(String(50))
    Restaurant_Name = Column(String(150))
    Cuisine_Type = Column(String(100))
    Order_Date = Column(DateTime, nullable=False)

    Delivery_Time_Min = Column(Integer)
    Distance_km = Column(Float)

    # Financial Columns (Using DECIMAL for accuracy)
    Order_Value = Column(DECIMAL(10, 2))
    Discount_Applied = Column(DECIMAL(10, 2))
    Final_Amount = Column(DECIMAL(10, 2))
    Profit_Margin = Column(DECIMAL(10, 2))
    Calculated_Amount = Column(DECIMAL(10, 2))

    Payment_Mode = Column(String(50))
    Order_Status = Column(String(50))
    Cancellation_Reason = Column(String(100))
    Delivery_Partner_ID = Column(String(50))

    Delivery_Rating = Column(Integer)
    Restaurant_Rating = Column(Integer)

    Order_Day = Column(String(20))
    Peak_Hour = Column(Boolean)
    Day_Type = Column(String(20))
    Profit_Margin_Percentage = Column(Float)
    Customer_Age_Group = Column(String(50))
    Delivery_Performance = Column(String(50))


# Create table in MySQL
Base.metadata.create_all(engine)

print("✅ Orders table created successfully!")