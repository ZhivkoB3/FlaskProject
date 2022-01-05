import pandas as pd
import sqlalchemy
from decouple import config
from apscheduler.schedulers.background import BackgroundScheduler

"""
These scripts make new SQL tables and update them. The values that are added to the new tables
are the difference between two records. This is used because in the main tables
that we are writing our data is with accumulation and it is hard to wrap
your head around. Having the difference between the days is easier for analysis
and also for making reports.

The index of the tables is the "pk" and also the values are sorted by the "pk".

When updating the tables these scrips delete the old ones and replace them with a new one.
If the tables exist. If they do not exist they just create a new one.

There is a separate script for every table - water, gas, electricity, compressors.

The scripts are made with a scheduler so we can update the time how often we update
these tables. Currently they are set to 1800 seconds or 30 minutes.
"""

def update_water_database():
    database = (f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
                f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}")
    engine = sqlalchemy.create_engine(database)
    sql_data = pd.read_sql_table('water', engine)
    df = pd.DataFrame(sql_data)
    df = df.sort_values(by=['pk'])
    df[['total_m3', 'casting', 'high_pressure_casting', 'glazing', 'sorting', 'administration']] = df[
        ['total_m3', 'casting', 'high_pressure_casting', 'glazing', 'sorting', 'administration']].diff()
    df.set_index('pk', inplace=True)
    df.to_sql('Daily Water consumption', engine, if_exists='replace')
    print('Water database updated !')


def update_gas_database():
    database = (f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
                f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}")
    engine = sqlalchemy.create_engine(database)
    sql_data = pd.read_sql_table('natural_gas', engine)
    df = pd.DataFrame(sql_data)
    df = df.sort_values(by=['pk'])
    df[['total_Nm3', 'casting', 'high_pressure_casting', 'glazing', 'sorting', 'administration', 'kilns',
        'shuttle_kilns']] = df[
        ['total_Nm3', 'casting', 'high_pressure_casting', 'glazing', 'sorting', 'administration', 'kilns',
         'shuttle_kilns']].diff()
    df.set_index('pk', inplace=True)
    df.to_sql('Daily natural gas consumption', engine, if_exists='replace')
    print('Gas database updated !')


def update_electricity_database():
    database = (f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
                f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}")
    engine = sqlalchemy.create_engine(database)
    sql_data = pd.read_sql_table('electricity', engine)
    df = pd.DataFrame(sql_data)
    df = df.sort_values(by=['pk'])
    df[['total_kwh', 'casting', 'high_pressure_casting', 'glazing', 'sorting', 'administration', 'kilns',
        'shuttle_kilns']] = df[
        ['total_kwh', 'casting', 'high_pressure_casting', 'glazing', 'sorting', 'administration', 'kilns',
         'shuttle_kilns']].diff()
    df.set_index('pk', inplace=True)
    df.to_sql('Daily electricity consumption', engine, if_exists='replace')
    print('Electricity database updated !')


def update_compressors_database():
    database = (f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
                f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}")
    engine = sqlalchemy.create_engine(database)
    sql_data = pd.read_sql_table('compressors', engine)
    df = pd.DataFrame(sql_data)
    df = df.sort_values(by=['pk'])
    df[['total_kwh', 'compressor_one', 'compressor_two', 'compressor_three', 'compressor_four', 'compressor_five']] = df[
        ['total_kwh', 'compressor_one', 'compressor_two', 'compressor_three', 'compressor_four', 'compressor_five']].diff()
    df.set_index('pk', inplace=True)
    df.to_sql('Daily compressors consumption', engine, if_exists='replace')
    print('Compressors database updated !')


scheduler = BackgroundScheduler(timezone='Europe/Sofia')
scheduler.add_job(func=update_water_database, trigger='interval', seconds=1800)
scheduler.add_job(func=update_gas_database, trigger='interval', seconds=1800)
scheduler.add_job(func=update_electricity_database, trigger='interval', seconds=1800)
scheduler.add_job(func=update_compressors_database, trigger='interval', seconds=1800)
