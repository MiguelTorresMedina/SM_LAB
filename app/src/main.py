from fastapi import FastAPI, HTTPException

import app.src.load as load
import app.src.extraction as extraction
import app.src.serve as serve # Importando la función de serve.py para ejecutar consultas

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Extracción de los datasets 1, 4 y 5
    datasets_to_extract = ['dataset_1', 'dataset_4', 'dataset_5']
    for dataset in datasets_to_extract:
        print(f"Extrayendo {dataset}...")
        extraction.extract_data_set(dataset)

    # Carga de los datasets 1, 3a, 3b, 4 y 5 en la base de datos
    datasets_to_load = ['dataset_1', 'dataset_3a', 'dataset_3b', 'dataset_4', 'dataset_5']
    for dataset in datasets_to_load:
        print(f"Cargando {dataset} en la base de datos...")
        load.to_db(dataset)

    # Limpieza de los datasets 1, 3a, 3b, 4 y 5
    for dataset in datasets_to_load:
        print(f"Limpiando {dataset}...")
        load.clean_dataset(dataset)

    # Generar el dataset final tras la limpieza
    print("Generando el dataset final...")
    load.generate_dataset_final()

@app.get("/dataset_final/filter")
async def filter_dataset(column: str, value: str):
    # Lista de columnas permitidas para evitar inyecciones SQL
    #allowed_columns = ['columna1', 'columna2', 'columna3']

    #if column not in allowed_columns:
    #    raise HTTPException(status_code=400, detail="Filtro no permitido")

    data = serve.get_filtered_data(column, value)
    return data.to_dict(orient='records')

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de procesamiento de datasets."}

# Aquí puedes agregar más endpoints si es necesario
