from sqlalchemy import Column, DateTime, Integer, String, Float

from .db import Base


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    kommun_id = Column(Integer, ForeignKey("kommuner.id"))


class Kommun(Base):
    __tablename__ = "kommuner"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    # "akut" | "akademiskt"

    latitude = Column(Float)
    longitude = Column(Float)


class TriageRule(Base):
    __tablename__ = "triage_rules"

    id = Column(Integer, primary_key=True)
    rule = Column(String, nullable=False)


class SimulationResult(Base):
    __tablename__ = "simulation_results"

    id = Column(Integer, primary_key=True)

    simulation_id = Column(Integer, ForeignKey("simulations.id"))

    patient_id = Column(Integer, ForeignKey("patients.id"))
    hospital_id = Column(Integer, ForeignKey("hospitals.id"))
    rule_id = Column(Integer, ForeignKey("triage_rules.id"))

    patient_to_acute = Column(Integer)
    acute_to_academic = Column(Integer)
    patient_to_academic = Column(Integer)

    category = Column(String)
    time_seconds = Column(Integer)

    __table_args__ = (
        Index("ix_simulation_results_simulation_id", "simulation_id"),
    )

class Simulation(Base):
    __tablename__ = "simulations"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)
    created_at = Column(DateTime)