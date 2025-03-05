from time import time
import pandas as pd
from sqlalchemy import engine
import argparse


def converter_dt(data: pd.DataFrame, columns_to_datetime: list[str]) -> pd.DataFrame:
    """
    Converte as colunas `['lpep_pickup_datetime', 'lpep_dropoff_datetime']`
    em colunas de datas
    
    :param data_in: Dados com colunas de datas não-convertidas
    :return data_out: Dados com colunas de datas convertidas
    """
    for col in columns_to_datetime:
        data[col] = pd.to_datetime(data[col])
    return data


# ['lpep_pickup_datetime', 'lpep_dropoff_datetime']


def main(params):
    columns_to_datetime = params.columns_to_datetime
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    filename = params.filename

    con = engine.create_engine(
        f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}')
    con.connect()

    init_df = pd.read_csv(filename, nrows=0)
    init_df = converter_dt(init_df, columns_to_datetime)
    init_df.to_sql(db, con=con, if_exists='replace')

    # pd.read_csv('taxi_zone_lookup.csv', nrows=10)
    df = pd.read_csv(filename,
                    chunksize=10000, iterator=True)

    while True:

        try:
            t0 = time()
            commit_df = next(df)
            commit_df = converter_dt(commit_df, columns_to_datetime)
            commit_df.to_sql(db, con=con, if_exists='append')
            t1 = time()

            delta_t = t1 - t0
            print(
                f"Chunk completa. Levou {delta_t:0.2f}s para concluir operação")

        except StopIteration:
            print('Dados inseridos. Operação concluída')
            break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--columns_to_datetime', '-c', type=str,
                        help='Columns to convert to datetime', nargs='*')
    parser.add_argument('--user', '-u', type=str,
                        help='User of Database')
    parser.add_argument('--password', '-k', type=str,
                        help='Password for database')
    parser.add_argument('--host', type=str,
                        help='host of Database')
    parser.add_argument('--port', '-p', type=str,
                        help='Port of Database')
    parser.add_argument('--db', type=str,
                        help='Database name')
    parser.add_argument('--filename', '-f', type=str,
                        help='name of file')
    main(parser.parse_args())
