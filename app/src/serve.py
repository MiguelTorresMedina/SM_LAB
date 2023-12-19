# serve.py
import pandas as pd
from sqlalchemy import create_engine, text
from config import config

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
