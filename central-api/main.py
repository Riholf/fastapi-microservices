from fastapi import FastAPI

app = FastAPI()


@app.post("/microserviceone")
async def call_microservice_one():
    # call to microservice 1
    return {"message": "Success"}