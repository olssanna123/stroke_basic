from src.data.db import engine
from src.data.models import Base

def create_database():
    Base.metadata.create_all(engine)
    print("Databas skapad.")