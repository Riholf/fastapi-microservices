from fastapi import FastAPI
from celery import Celery


celery_app = Celery('microservice_one', broker='localhost')
app = FastAPI()


@app.post("/createtask")
async def create_task():
    # create a task for worker_one
    return {"message": "Task created successfully"}