import json

from models import WaterModel, NaturalGasModel, ElectricityModel, CompressorsModel
from tests.bases import BaseTestCase
from tests.factories import DataEntryFactory, DataAnalystFactory
from tests.helpers import generate_token, object_as_dict


class TestPostWaterDataEntry(BaseTestCase):
    """
    Test post requests for "water" database.
    Steps:
    1. Check if there are any records in DB
    2. Write into database
    3. Check if the record is uploaded to the DB
    4. Check if the record is correctly written in the DB
    5. Check if the record is correctly updated
    Use user == Data Entry
    """
    def test_post_to_water(self):
        url = '/energy/water'
        data = {
            "total_m3": 680,
            "casting": 90,
            "high_pressure_casting": 30,
            "glazing": 30,
            "sorting": 10,
            "administration": 5
        }

        data_entry = DataEntryFactory()
        token = generate_token(data_entry)
        self.headers.update({"Authorization": f"Bearer {token}"})
        water_data = WaterModel.query.all()
        assert len(water_data) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        water_data = WaterModel.query.all()
        assert len(water_data) == 1

        water_data_added = object_as_dict(water_data[0])

        assert water_data_added == {
            'pk': water_data[0].pk,
            'total_m3': water_data[0].total_m3,
            'casting': water_data[0].casting,
            'sorting': water_data[0].sorting,
            'glazing': water_data[0].glazing,
            'administration': water_data[0].administration,
            'high_pressure_casting': water_data[0].high_pressure_casting,
            'created_on': water_data[0].created_on,
            'updated_by': water_data[0].updated_by,
            'updated_on': water_data[0].updated_on,
            'user_id': water_data[0].user_id
        }

        expected_resp = {
            'pk': water_data[0].pk,
            'total_m3': water_data[0].total_m3,
            'casting': water_data[0].casting,
            'sorting': water_data[0].sorting,
            'glazing': water_data[0].glazing,
            'administration': water_data[0].administration,
            'high_pressure_casting': water_data[0].high_pressure_casting,
        }

        actual_resp = resp.json
        actual_resp.pop('created_on')
        assert resp.status_code == 201
        assert actual_resp == expected_resp


class TestPostGasDataEntry(BaseTestCase):
    """
    Test put requests for "gas" database.
    Steps:
    1. Check if there are any records in DB
    2. Write into database
    3. Check if the record is uploaded to the DB
    4. Check if the record is correctly written in the DB
    5. Check if the record is correctly updated
    Use user == Data Entry
    """
    def test_post_to_gas(self):
        url = '/energy/gas'
        data = {
            "total_Nm3": 230,
            "casting": 90,
            "high_pressure_casting": 30,
            "glazing": 30,
            "sorting": 10,
            "kilns": 100,
            "shuttle_kilns": 50,
            "administration": 5
        }

        data_entry = DataEntryFactory()
        token = generate_token(data_entry)
        self.headers.update({"Authorization": f"Bearer {token}"})
        gas_data = NaturalGasModel.query.all()
        assert len(gas_data) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        gas_data = NaturalGasModel.query.all()
        assert len(gas_data) == 1

        gas_data_added = object_as_dict(gas_data[0])

        assert gas_data_added == {
            'pk': gas_data[0].pk,
            'total_Nm3': gas_data[0].total_Nm3,
            'casting': gas_data[0].casting,
            'sorting': gas_data[0].sorting,
            'glazing': gas_data[0].glazing,
            'administration': gas_data[0].administration,
            'high_pressure_casting': gas_data[0].high_pressure_casting,
            "kilns": gas_data[0].kilns,
            "shuttle_kilns": gas_data[0].shuttle_kilns,
            'created_on': gas_data[0].created_on,
            'updated_by': gas_data[0].updated_by,
            'updated_on': gas_data[0].updated_on,
            'user_id': gas_data[0].user_id
        }

        expected_resp = {
            'pk': gas_data[0].pk,
            'total_Nm3': gas_data[0].total_Nm3,
            'casting': gas_data[0].casting,
            'sorting': gas_data[0].sorting,
            'glazing': gas_data[0].glazing,
            'administration': gas_data[0].administration,
            'high_pressure_casting': gas_data[0].high_pressure_casting,
            "kilns": gas_data[0].kilns,
            "shuttle_kilns": gas_data[0].shuttle_kilns,
        }

        actual_resp = resp.json
        actual_resp.pop('created_on')
        assert resp.status_code == 201
        assert actual_resp == expected_resp


class TestPostElectricityDataEntry(BaseTestCase):
    """
    Test put requests for "electricity" database.
    Steps:
    1. Check if there are any records in DB
    2. Write into database
    3. Check if the record is uploaded to the DB
    4. Check if the record is correctly written in the DB
    5. Check if the record is correctly updated
    Use user == Data Entry
    """

    def test_post_to_electricity(self):
        url = '/energy/electricity'
        data = {
            "total_kwh": 230,
            "casting": 90,
            "high_pressure_casting": 30,
            "glazing": 30,
            "sorting": 10,
            "kilns": 100,
            "shuttle_kilns": 50,
            "administration": 5
        }

        data_entry = DataEntryFactory()
        token = generate_token(data_entry)
        self.headers.update({"Authorization": f"Bearer {token}"})
        electricity_data = ElectricityModel.query.all()
        assert len(electricity_data) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        electricity_data = ElectricityModel.query.all()
        assert len(electricity_data) == 1

        electricity_data_added = object_as_dict(electricity_data[0])

        assert electricity_data_added == {
            'pk': electricity_data[0].pk,
            'total_kwh': electricity_data[0].total_kwh,
            'casting': electricity_data[0].casting,
            'sorting': electricity_data[0].sorting,
            'glazing': electricity_data[0].glazing,
            'administration': electricity_data[0].administration,
            'high_pressure_casting': electricity_data[0].high_pressure_casting,
            "kilns": electricity_data[0].kilns,
            "shuttle_kilns": electricity_data[0].shuttle_kilns,
            'created_on': electricity_data[0].created_on,
            'updated_by': electricity_data[0].updated_by,
            'updated_on': electricity_data[0].updated_on,
            'user_id': electricity_data[0].user_id
        }

        expected_resp = {
            'pk': electricity_data[0].pk,
            'total_kwh': electricity_data[0].total_kwh,
            'casting': electricity_data[0].casting,
            'sorting': electricity_data[0].sorting,
            'glazing': electricity_data[0].glazing,
            'administration': electricity_data[0].administration,
            'high_pressure_casting': electricity_data[0].high_pressure_casting,
            "kilns": electricity_data[0].kilns,
            "shuttle_kilns": electricity_data[0].shuttle_kilns,
        }

        actual_resp = resp.json
        actual_resp.pop('created_on')
        assert resp.status_code == 201
        assert actual_resp == expected_resp


class TestPostCompressorsDataEntry(BaseTestCase):
    """
    Test put requests for "compressors" database.
    Steps:
    1. Check if there are any records in DB
    2. Write into database
    3. Check if the record is uploaded to the DB
    4. Check if the record is correctly written in the DB
    5. Check if the record is correctly updated
    Use user == Data Entry
    """
    def test_post_to_compressors(self):
        url = '/energy/compressors'
        data = {
            "total_kwh": 200,
            "compressor_one": 20,
            "compressor_two": 30,
            "compressor_three": 100,
            "compressor_four": 30,
            "compressor_five": 20
        }

        data_entry = DataEntryFactory()
        token = generate_token(data_entry)
        self.headers.update({"Authorization": f"Bearer {token}"})
        compressors_data = CompressorsModel.query.all()
        assert len(compressors_data) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        compressors_data = CompressorsModel.query.all()
        assert len(compressors_data) == 1

        compressors_data_added = object_as_dict(compressors_data[0])

        assert compressors_data_added == {
            'pk': compressors_data[0].pk,
            'total_kwh': compressors_data[0].total_kwh,
            'compressor_one': compressors_data[0].compressor_one,
            'compressor_two': compressors_data[0].compressor_two,
            'compressor_three': compressors_data[0].compressor_three,
            'compressor_four': compressors_data[0].compressor_four,
            'compressor_five': compressors_data[0].compressor_five,
            'created_on': compressors_data[0].created_on,
            'updated_by': compressors_data[0].updated_by,
            'updated_on': compressors_data[0].updated_on,
            'user_id': compressors_data[0].user_id
        }

        expected_resp = {
            'pk': compressors_data[0].pk,
            'total_kwh': compressors_data[0].total_kwh,
            'compressor_one': compressors_data[0].compressor_one,
            'compressor_two': compressors_data[0].compressor_two,
            'compressor_three': compressors_data[0].compressor_three,
            'compressor_four': compressors_data[0].compressor_four,
            'compressor_five': compressors_data[0].compressor_five,
        }

        actual_resp = resp.json
        actual_resp.pop('created_on')
        assert resp.status_code == 201
        assert actual_resp == expected_resp

class TestPostWaterDataAnalyst(BaseTestCase):
    """
    Test put requests for "water" database.
    Steps:
    1. Check if there are any records in DB
    2. Write into database
    3. Check if the record is uploaded to the DB
    4. Check if the record is correctly written in the DB
    5. Check if the record is correctly updated
    Use user == Data Analyst
    """
    def test_post_to_water(self):
        url = '/energy/water'
        data = {
            "total_m3": 680,
            "casting": 90,
            "high_pressure_casting": 30,
            "glazing": 30,
            "sorting": 10,
            "administration": 5
        }

        data_analyst = DataAnalystFactory()
        token = generate_token(data_analyst)
        self.headers.update({"Authorization": f"Bearer {token}"})
        water_data = WaterModel.query.all()
        assert len(water_data) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        water_data = WaterModel.query.all()
        assert len(water_data) == 1

        water_data_added = object_as_dict(water_data[0])

        assert water_data_added == {
            'pk': water_data[0].pk,
            'total_m3': water_data[0].total_m3,
            'casting': water_data[0].casting,
            'sorting': water_data[0].sorting,
            'glazing': water_data[0].glazing,
            'administration': water_data[0].administration,
            'high_pressure_casting': water_data[0].high_pressure_casting,
            'created_on': water_data[0].created_on,
            'updated_by': water_data[0].updated_by,
            'updated_on': water_data[0].updated_on,
            'user_id': water_data[0].user_id
        }

        expected_resp = {
            'pk': water_data[0].pk,
            'total_m3': water_data[0].total_m3,
            'casting': water_data[0].casting,
            'sorting': water_data[0].sorting,
            'glazing': water_data[0].glazing,
            'administration': water_data[0].administration,
            'high_pressure_casting': water_data[0].high_pressure_casting,
        }

        actual_resp = resp.json
        actual_resp.pop('created_on')
        assert resp.status_code == 201
        assert actual_resp == expected_resp


class TestPostGasDataDataAnalyst(BaseTestCase):
    """
    Test put requests for "gas" database.
    Steps:
    1. Check if there are any records in DB
    2. Write into database
    3. Check if the record is uploaded to the DB
    4. Check if the record is correctly written in the DB
    5. Check if the record is correctly updated
    Use user == Data Analyst
    """
    def test_post_to_gas(self):
        url = '/energy/gas'
        data = {
            "total_Nm3": 230,
            "casting": 90,
            "high_pressure_casting": 30,
            "glazing": 30,
            "sorting": 10,
            "kilns": 100,
            "shuttle_kilns": 50,
            "administration": 5
        }

        data_analyst = DataAnalystFactory()
        token = generate_token(data_analyst)
        self.headers.update({"Authorization": f"Bearer {token}"})
        gas_data = NaturalGasModel.query.all()
        assert len(gas_data) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        gas_data = NaturalGasModel.query.all()
        assert len(gas_data) == 1

        gas_data_added = object_as_dict(gas_data[0])

        assert gas_data_added == {
            'pk': gas_data[0].pk,
            'total_Nm3': gas_data[0].total_Nm3,
            'casting': gas_data[0].casting,
            'sorting': gas_data[0].sorting,
            'glazing': gas_data[0].glazing,
            'administration': gas_data[0].administration,
            'high_pressure_casting': gas_data[0].high_pressure_casting,
            "kilns": gas_data[0].kilns,
            "shuttle_kilns": gas_data[0].shuttle_kilns,
            'created_on': gas_data[0].created_on,
            'updated_by': gas_data[0].updated_by,
            'updated_on': gas_data[0].updated_on,
            'user_id': gas_data[0].user_id
        }

        expected_resp = {
            'pk': gas_data[0].pk,
            'total_Nm3': gas_data[0].total_Nm3,
            'casting': gas_data[0].casting,
            'sorting': gas_data[0].sorting,
            'glazing': gas_data[0].glazing,
            'administration': gas_data[0].administration,
            'high_pressure_casting': gas_data[0].high_pressure_casting,
            "kilns": gas_data[0].kilns,
            "shuttle_kilns": gas_data[0].shuttle_kilns,
        }

        actual_resp = resp.json
        actual_resp.pop('created_on')
        assert resp.status_code == 201
        assert actual_resp == expected_resp


class TestPostElectricityDataAnalyst(BaseTestCase):
    """
    Test put requests for "electricity" database.
    Steps:
    1. Check if there are any records in DB
    2. Write into database
    3. Check if the record is uploaded to the DB
    4. Check if the record is correctly written in the DB
    5. Check if the record is correctly updated
    Use user == Data Analyst
    """

    def test_post_to_electricity_analyst(self):
        url = '/energy/electricity'
        data = {
                "total_kwh": 230,
                "casting": 90,
                "high_pressure_casting": 30,
                "glazing": 30,
                "sorting": 10,
                "kilns": 100,
                "shuttle_kilns": 50,
                "administration": 5
                }

        data_analyst = DataAnalystFactory()
        token = generate_token(data_analyst)
        self.headers.update({"Authorization": f"Bearer {token}"})
        electricity_data = ElectricityModel.query.all()
        assert len(electricity_data) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        electricity_data = ElectricityModel.query.all()
        assert len(electricity_data) == 1

        electricity_data_added = object_as_dict(electricity_data[0])

        assert electricity_data_added == {
            'pk': electricity_data[0].pk,
            'total_kwh': electricity_data[0].total_kwh,
            'casting': electricity_data[0].casting,
            'sorting': electricity_data[0].sorting,
            'glazing': electricity_data[0].glazing,
            'administration': electricity_data[0].administration,
            'high_pressure_casting': electricity_data[0].high_pressure_casting,
            "kilns": electricity_data[0].kilns,
            "shuttle_kilns": electricity_data[0].shuttle_kilns,
            'created_on': electricity_data[0].created_on,
            'updated_by': electricity_data[0].updated_by,
            'updated_on': electricity_data[0].updated_on,
            'user_id': electricity_data[0].user_id
        }

        expected_resp = {
            'pk': electricity_data[0].pk,
            'total_kwh': electricity_data[0].total_kwh,
            'casting': electricity_data[0].casting,
            'sorting': electricity_data[0].sorting,
            'glazing': electricity_data[0].glazing,
            'administration': electricity_data[0].administration,
            'high_pressure_casting': electricity_data[0].high_pressure_casting,
            "kilns": electricity_data[0].kilns,
            "shuttle_kilns": electricity_data[0].shuttle_kilns,
        }

        actual_resp = resp.json
        actual_resp.pop('created_on')
        assert resp.status_code == 201
        assert actual_resp == expected_resp


class TestPostCompressorsDataAnalyst(BaseTestCase):
    """
    Test put requests for "compressors" database.
    Steps:
    1. Check if there are any records in DB
    2. Write into database
    3. Check if the record is uploaded to the DB
    4. Check if the record is correctly written in the DB
    5. Check if the record is correctly updated
    Use user == Data Analyst
    """
    def test_post_to_compressors(self):
        url = '/energy/compressors'
        data = {
            "total_kwh": 200,
            "compressor_one": 20,
            "compressor_two": 30,
            "compressor_three": 100,
            "compressor_four": 30,
            "compressor_five": 20
        }

        data_analyst = DataAnalystFactory()
        token = generate_token(data_analyst)
        self.headers.update({"Authorization": f"Bearer {token}"})
        compressors_data = CompressorsModel.query.all()
        assert len(compressors_data) == 0

        resp = self.client.post(url, data=json.dumps(data), headers=self.headers)

        compressors_data = CompressorsModel.query.all()
        assert len(compressors_data) == 1

        compressors_data_added = object_as_dict(compressors_data[0])

        assert compressors_data_added == {
            'pk': compressors_data[0].pk,
            'total_kwh': compressors_data[0].total_kwh,
            'compressor_one': compressors_data[0].compressor_one,
            'compressor_two': compressors_data[0].compressor_two,
            'compressor_three': compressors_data[0].compressor_three,
            'compressor_four': compressors_data[0].compressor_four,
            'compressor_five': compressors_data[0].compressor_five,
            'created_on': compressors_data[0].created_on,
            'updated_by': compressors_data[0].updated_by,
            'updated_on': compressors_data[0].updated_on,
            'user_id': compressors_data[0].user_id
        }

        expected_resp = {
            'pk': compressors_data[0].pk,
            'total_kwh': compressors_data[0].total_kwh,
            'compressor_one': compressors_data[0].compressor_one,
            'compressor_two': compressors_data[0].compressor_two,
            'compressor_three': compressors_data[0].compressor_three,
            'compressor_four': compressors_data[0].compressor_four,
            'compressor_five': compressors_data[0].compressor_five,
        }

        actual_resp = resp.json
        actual_resp.pop('created_on')
        assert resp.status_code == 201
        assert actual_resp == expected_resp


