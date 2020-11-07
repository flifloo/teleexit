from db import Base
from sqlalchemy import Column, Integer, String, Date


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    birth_city = Column(String)
    address = Column(String)

    def __init__(self, id: int):
        self.id = id
