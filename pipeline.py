from time import time
import pandas as pd
from sqlalchemy import engine

def converter_dt(data:pd.DataFrame) -> pd.DataFrame:
    """
    Converte as colunas `['lpep_pickup_datetime', 'lpep_dropoff_datetime']`
    em colunas de datas
    
    :param data_in: Dados com colunas de datas não-convertidas
    :return data_out: Dados com colunas de datas convertidas
    """
    for col in columns_to_date_time:
        data[col] = pd.to_datetime(data[col])
    return data

columns_to_date_time = [
    'lpep_pickup_datetime', 'lpep_dropoff_datetime']

engine = engine.create_engine(
    'postgresql+psycopg2://admin:admin@host.docker.internal:5432/ny_taxi')
engine.connect()

init_df = pd.read_csv('green_tripdata_2019-10.csv', nrows=0)
init_df = converter_dt(init_df)
init_df.to_sql('ny_taxi', con=engine, if_exists='replace')


# pd.read_csv('taxi_zone_lookup.csv', nrows=10)
df = pd.read_csv('green_tripdata_2019-10.csv', chunksize=10000, iterator=True)

while True:

    try:
        t0 = time()

        commit_df = next(df)
        commit_df = converter_dt(commit_df)
        commit_df.to_sql('ny_taxi', con=engine, if_exists='append')

        t1 = time()
        delta_t = t1 - t0
        print(f"Chunk completa. Levou {delta_t:0.2f}s para concluir operação")

    except StopIteration:
        print('Dados inseridos. Operação concluída')
        break
