from sqlalchemy import inspect
from src.data.db import engine

def inspect_db():   
    inspector = inspect(engine)
    print(inspector.get_table_names())