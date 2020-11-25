from celery import Celery
import time
import datetime

celery = Celery('hello', broker='amqp://guest:guest@127.0.0.1:5672//')
                            
@celery.task
def hello(mensagem_esperada):
    time.sleep(15)
    with open('file.txt', 'a') as file:
        file.write(f'{mensagem_esperada} - {datetime.datetime.now()}')
        print(f'{mensagem_esperada} - {datetime.datetime.now()}')