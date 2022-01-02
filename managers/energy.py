from werkzeug.exceptions import NotFound

from db import db
from models.energy import WaterModel, NaturalGasModel, ElectricityModel, CompressorsModel


class WaterManager:
    @staticmethod
    def get_all():
        return WaterModel.query.all()

    @staticmethod
    def create(data, data_entry_pk):
        data['user_id'] = data_entry_pk
        energy_data = WaterModel(**data)
        db.session.add(energy_data)
        db.session.commit()
        return energy_data

    @staticmethod
    def delete(id_):
        water_q = WaterModel.query.filter_by(pk = id_)
        water = water_q.first()
        if not water:
            raise NotFound('Data not present')

        db.session.delete(water)
        db.session.commit()

    @staticmethod
    def update(data, id_, data_entry_pk):
        data['user_id'] = data_entry_pk
        water_q = WaterModel.query.filter_by(pk=id_)
        water = water_q.first()
        if not water:
            raise NotFound('Data not present')

        water_q.update(data)
        db.session.add(water)
        db.session.commit()
        return water


class GasManager:
    @staticmethod
    def get_all():
        return NaturalGasModel.query.all()

    @staticmethod
    def create(data, data_entry_pk):
        data['user_id'] = data_entry_pk
        energy_data = NaturalGasModel(**data)
        db.session.add(energy_data)
        db.session.commit()
        return energy_data

    @staticmethod
    def delete(id_):
        gas_q = NaturalGasModel.query.filter_by(pk = id_)
        gas = gas_q.first()
        if not gas:
            raise NotFound('Data not present')

        db.session.delete(gas)
        db.session.commit()


    @staticmethod
    def update(data, id_, data_entry_pk):
        data['updated_by'] = data_entry_pk
        gas_q = NaturalGasModel.query.filter_by(pk=id_)
        gas = gas_q.first()
        if not gas:
            raise NotFound('Data not present')

        gas_q.update(data)
        db.session.add(gas)
        db.session.commit()
        return gas


class ElectricityManager:
    @staticmethod
    def get_all():
        return ElectricityModel.query.all()

    @staticmethod
    def create(data, data_entry_pk):
        data['user_id'] = data_entry_pk
        energy_data = ElectricityModel(**data)
        db.session.add(energy_data)
        db.session.commit()
        return energy_data

    @staticmethod
    def delete(id_):
        electricity_q = ElectricityModel.query.filter_by(pk=id_)
        electricity = electricity_q.first()

        if not electricity:
            raise NotFound('Data not present')

        db.session.delete(electricity)
        db.session.commit()

    @staticmethod
    def update(data, id_, data_entry_pk):
        data['user_id'] = data_entry_pk
        electricity_q = ElectricityModel.query.filter_by(pk=id_)
        electricity = electricity_q.first()
        if not electricity:
            raise NotFound('Data not present')

        electricity_q.update(data)
        db.session.add(electricity)
        db.session.commit()
        return electricity

class CompressorsManager:
    @staticmethod
    def get_all():
        return CompressorsModel.query.all()

    @staticmethod
    def create(data, data_entry_pk):
        data['user_id'] = data_entry_pk
        energy_data = CompressorsModel(**data)
        db.session.add(energy_data)
        db.session.commit()
        return energy_data

    @staticmethod
    def delete(id_):
        compressors_q = CompressorsModel.query.filter_by(pk=id_)
        compressors = compressors_q.first()

        if not compressors:
            raise NotFound('Data not present')

        db.session.delete(compressors)
        db.session.commit()

    @staticmethod
    def update(data, id_, data_entry_pk):
        data['updated_by'] = data_entry_pk
        compressors_q = CompressorsModel.query.filter_by(pk=id_)
        compressors = compressors_q.first()

        if not compressors:
            raise NotFound('Data not present')

        compressors_q.update(data)
        db.session.add(compressors)
        db.session.commit()
        return compressors




