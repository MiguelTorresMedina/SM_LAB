# serve.py
import pandas as pd
import psycopg2
import psycopg2.extras as extras
from sqlalchemy import create_engine, text
from app.src.config import config

def query_db(query, parameters=None):
    """
    Ejecuta una consulta específica en la base de datos y devuelve el resultado.
    """
    params = config()
    engine_string = f"postgresql+psycopg2://{params['user']}:{params['password']}@{params['host']}:{params['port']}/{params['database']}"
    engine = create_engine(engine_string)

    with engine.connect() as conn:
        result = pd.read_sql(text(query), conn, params=parameters)
    return result

def get_filtered_data(column, value):
    query = text("SELECT * FROM dataset_final WHERE " + column + " = :value")
    parameters = {"value": value}
    return query_db(query, parameters)