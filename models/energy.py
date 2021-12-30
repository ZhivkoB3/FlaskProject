from sqlalchemy import func
from sqlalchemy.ext.declarative import declared_attr
from db import db


class BaseEnergyModel(db.Model):
    __abstract__ = True

    pk = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, server_default=func.now())
    updated_on = db.Column(db.DateTime, onupdate=func.now())

    @declared_attr
    def data_entry_id(self):
        return db.Column(db.Integer, db.ForeignKey('users.pk'))

    @declared_attr
    def updated_by(self):
        return db.Column(db.Integer, db.ForeignKey('users.pk'))


class CompressorsModel(BaseEnergyModel):
    __tablename__ = "compressors"
    total_kwh = db.Column(db.Integer, nullable=False)
    compressor_one = db.Column(db.Integer, nullable=False)
    compressor_two = db.Column(db.Integer, nullable=False)
    compressor_three = db.Column(db.Integer, nullable=False)
    compressor_four = db.Column(db.Integer, nullable=False)
    compressor_five = db.Column(db.Integer, nullable=False)


class ElectricityModel(BaseEnergyModel):
    __tablename__ = 'electricity'
    total_kwh = db.Column(db.Integer, nullable=False)
    casting = db.Column(db.Integer, nullable=False)
    high_pressure_casting = db.Column(db.Integer, nullable=False)
    glazing = db.Column(db.Integer, nullable=False)
    sorting = db.Column(db.Integer, nullable=False)
    kilns = db.Column(db.Integer, nullable=False)
    shuttle_kilns = db.Column(db.Integer, nullable=False)
    administration = db.Column(db.Integer, nullable=False)


class NaturalGasModel(BaseEnergyModel):
    __tablename__ = 'natural_gas'
    total_Nm3 = db.Column(db.Integer, nullable=False)
    casting = db.Column(db.Integer, nullable=False)
    high_pressure_casting = db.Column(db.Integer, nullable=False)
    glazing = db.Column(db.Integer, nullable=False)
    sorting = db.Column(db.Integer, nullable=False)
    kilns = db.Column(db.Integer, nullable=False)
    shuttle_kilns = db.Column(db.Integer, nullable=False)
    administration = db.Column(db.Integer, nullable=False)


class WaterModel(BaseEnergyModel):
    __tablename__ = 'water'
    total_m3 = db.Column(db.Integer, nullable=False)
    casting = db.Column(db.Integer, nullable=False)
    high_pressure_casting = db.Column(db.Integer, nullable=False)
    glazing = db.Column(db.Integer, nullable=False)
    sorting = db.Column(db.Integer, nullable=False)
    administration = db.Column(db.Integer, nullable=False)
