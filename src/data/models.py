from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from src.data.db import Base


class Hospital(Base):
    __tablename__ = "hospitals"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    simulation_results = relationship("SimulationResult", back_populates="hospital")


class Kommun(Base):
    __tablename__ = "kommuner"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    patients = relationship("Patient", back_populates="kommun")


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True)

    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)

    kommun_id = Column(Integer, ForeignKey("kommuner.id"))

    kommun = relationship("Kommun", back_populates="patients")
    simulation_results = relationship("SimulationResult", back_populates="patient")


class TriageRule(Base):
    __tablename__ = "triage_rules"

    id = Column(Integer, primary_key=True)
    rule = Column(String, nullable=False)

    simulation_results = relationship("SimulationResult", back_populates="rule")


class Simulation(Base):
    __tablename__ = "simulations"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)

    results = relationship("SimulationResult", back_populates="simulation")


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

    simulation = relationship("Simulation", back_populates="results")
    patient = relationship("Patient", back_populates="simulation_results")
    hospital = relationship("Hospital", back_populates="simulation_results")
    rule = relationship("TriageRule", back_populates="simulation_results")

    __table_args__ = (
        Index("ix_simulation_results_simulation_id", "simulation_id"),
    )