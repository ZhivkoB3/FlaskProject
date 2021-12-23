from werkzeug.exceptions import NotFound

from db import db
from models.energy import WaterModel, NaturalGasModel
from managers.auth import auth


class WaterManager:
    @staticmethod
    def get_all():
        return WaterModel.query.all()

    @staticmethod
    def create(data, data_entry_pk):
        data['data_entry_id'] = data_entry_pk
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
    def update(data, id_):
        water_q = WaterModel.query.filter_by(pk=id_)
        water = water_q.first()
        if not water:
            raise NotFound('Data not present')
        user = auth.current_user()

        if not user.pk == water.data_entry_id:
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
        data['data_entry_id'] = data_entry_pk
        energy_data = NaturalGasModel(**data)
        db.session.add(energy_data)
        db.session.commit()
        return energy_data


