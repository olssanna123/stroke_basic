from src.data.db import SessionLocal
from src.data.models import Hospital

def add_hospital():

    session = SessionLocal()

    hospital = Hospital(
        name="Sahlgrenska",
        latitude=57.6848,
        longitude=11.9594,
    )

    session.add(hospital)
    session.commit()

    print("Hospital sparat")