from requests import session

from src.config import Config
from src.data.create_db import create_database
from src.data.inspect_db import inspect_db
from src.data.seed import add_hospital
from src.utils.initiate_sampling_array import initiate_sampling_array
from src.simulation.pipeline import run_single_iteration
from src.data.db import Base, engine
import src.data.models
from src.data.db import SessionLocal
from src.data.models import Hospital


def main():
    
    # Initialize the database
    create_database()   
    inspect_db()

    add_hospital()

    session = SessionLocal()

    hospitals = session.query(Hospital).all()

    for h in hospitals:
        print(h.id, h.name)

    # Initialize configuration and sampling array
    config = Config()          # Alla regler här


if __name__ == "__main__":
    main()