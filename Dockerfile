FROM python:3.8-slim

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY file.txt /
COPY ./app /app/
COPY run.py /
COPY setup.py /

ENTRYPOINT gunicorn -c setup.py run:app