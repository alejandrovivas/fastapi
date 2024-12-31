# from fastapi import FastAPI, File, UploadFile
# from celery.result import AsyncResult
# from celery_config import celery_app
# import logging
# import multiprocessing as mp
# from tasks import process_csv
# import os
# import uuid

# logger = logging.getLogger('uvicorn.error')
# logger.setLevel(logging.DEBUG)
#
# app = FastAPI()
#
# chunk_size = 3
# num_processes = mp.cpu_count()
#
# @app.post("/upload-csv/")
# async def upload_csv(file: UploadFile = File(...)):
#     try:
#         unique_id = uuid.uuid4()
#         output_dir = f"/fastAPI/docs/{unique_id}"
#         os.makedirs(output_dir, exist_ok=True)
#         # Create a file path
#         file_location = f"{output_dir}/data.csv"
#
#         # Copy file content in a file on server
#         with open(file_location, 'wb') as destination:
#             destination.write(file.file.read())
#
#         logger.debug(f"File saved to {file_location}")
#
#         #execute async task to proccess csv
#         result = process_csv.delay(file_location, output_dir)
#
#         #  Response
#         return {"message": "The file is being processed", "task_id": result.task_id}
#     except Exception as e:
#         return {"message": str(e)}
#
# @app.get("/processed-csv/{task_id}")
# async def processed_csv(task_id: str):
#     task_result = AsyncResult(task_id, app=celery_app)
#     logger.debug(f"{task_result}")
#     if task_result.state == 'PENDING':
#         return {"message": "The task is being processed1", "task_id": task_id}
#     elif task_result.state == 'FAILURE':
#         return {"message": "There was an error processing the file"}
#     else:
#         return {"message": f"The task was processed you can download the file at {task_result.info}"}

from fastapi import FastAPI
# from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = 'Learning FastAPI'
app.version = '0.0.1'

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]

@app.get("/", tags=['Home'])
def home():
    return "Hello World"

@app.get("/movies", tags=['Movies'])
def get_movies():
    return movies

@app.get("/movies/{id}", tags=['Movies'])
def get_movies(movie_id: int):
    for movie in movies:
        if movie['id'] == movie_id:
            return movie

    return movies

@app.get("/movies/", tags=['Movies by Category'])
def get_movies_by_category(category: str):
    for movie in movies:
        if movie['category'] == category:
            return movie

    return movies