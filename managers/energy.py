from db import db
from models.energy import WaterModel
from werkzeug.exceptions import NotFound
from managers.auth import auth


class WaterManager:
    @staticmethod
    def get_all():
        return WaterModel.query.all()

    @staticmethod
    def create(water_data, data_entry_pk):
        water_data['data_entry_pk'] = data_entry_pk
        energy_data = WaterModel(**water_data)
        db.session.add(energy_data)
        db.session.commit()
        return energy_data

    @staticmethod
    def update(water_data, pk):
        water_q = WaterModel.query.filter_by(pk=pk)
        energy_data = water_q.first()
        if not energy_data:
            raise NotFound('This data is not present')
        user = auth.current_user()

        if not user.pk == energy_data.data_entry_pk:
            raise NotFound('This data is not present')

        water_q.update(water_data)
        db.session.add(energy_data)
        db.session.commit()
        return energy_data
