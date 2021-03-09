from celery import Celery

celery_app = Celery('worker_one', broker='localhost')


@app.task
def do_something():
    # your code
    return {"message": "Success"}


if __name__ == '__main__':
    os.system('celery -A worker_one worker --loglevel=DEBUG')

