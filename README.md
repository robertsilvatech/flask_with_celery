# README

## Executando o gunicorn

```
gunicorn --bind 0.0.0.0:5000 -w 4 run:app
gunicorn -c setup.py run:app
```

## Executando o celery

```
celery --app=app.celery_runner worker --loglevel=info
```