import pandas as pd
import os
from sqlalchemy import text, exc, create_engine


# database cred
DB_PASS = os.environ.get("POSTGRES_PASSWORD")
DB_USER = "postgres"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"

DB_NAME = "module_1"

# tables
TAXI_TB = "taxi"
ZONE_TB = "zone"


def create_database():
    try:
        engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}")

        conn = engine.connect()
        conn.execution_options(isolation_level="AUTOCOMMIT").execute(
            text(f"CREATE DATABASE {DB_NAME}")
        )
        print(f"{DB_NAME} created succesfully")
    except exc.ProgrammingError as e:
        print(e)


def df_to_table(df: pd.DataFrame, table: str):
    print(f"Loading {len(df)} records dataframe into {table}")
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    with engine.connect() as conn:
        df.to_sql(table, con=conn, index=False, if_exists="replace", schema="public")

    print(f"{len(df)} records created successfuly in {table}")


if __name__ == "__main__":
    green_taxi_df = pd.read_csv("data/green_tripdata_2019-09.csv")
    taxi_zone_df = pd.read_csv("data/taxi+_zone_lookup.csv")

    create_database()
    df_to_table(green_taxi_df, TAXI_TB)
    df_to_table(taxi_zone_df, ZONE_TB)
