from fastapi import FastAPI
from extraction import extract_data_set, to_db
from load import clean_dataset, generate_dataset_final

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    # Extracción de los datasets 1, 4 y 5
    datasets_to_extract = ['dataset_1', 'dataset_4', 'dataset_5']
    for dataset in datasets_to_extract:
        print(f"Extrayendo {dataset}...")
        extract_data_set(dataset)

    # Carga de los datasets 1, 3a, 3b, 4 y 5 en la base de datos
    datasets_to_load = ['dataset_1', 'dataset_3a', 'dataset_3b', 'dataset_4', 'dataset_5']
    for dataset in datasets_to_load:
        print(f"Cargando {dataset} en la base de datos...")
        to_db(dataset)

    # Limpieza de los datasets 1, 3a, 3b, 4 y 5
    for dataset in datasets_to_load:
        print(f"Limpiando {dataset}...")
        clean_dataset(dataset)

    # Generar el dataset final tras la limpieza
    print("Generando el dataset final...")
    generate_dataset_final()

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de procesamiento de datasets."}

# Aquí puedes agregar más endpoints para servir los datos o realizar otras operaciones
