import pandas as pd
import sqlalchemy
from decouple import config
from apscheduler.schedulers.background import BackgroundScheduler



def update_water_database():
    database = (f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
               f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}")
    engine = sqlalchemy.create_engine(database)
    sql_data = pd.read_sql_table('water', engine)
    df = pd.DataFrame(sql_data)
    df = df.sort_values(by=['pk'])
    df[['total_m3', 'casting', 'high_pressure_casting', 'glazing', 'sorting', 'administration']] = df[['total_m3', 'casting', 'high_pressure_casting', 'glazing', 'sorting', 'administration']].diff()
    df.set_index('pk', inplace=True)
    df.to_sql('Daily Water consumption', engine, if_exists='replace')
    print('DataBase updated !')



scheduler = BackgroundScheduler(timezone='Europe/Sofia')
scheduler.add_job(func=update_water_database, trigger='interval', seconds=900)



