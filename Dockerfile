FROM tiangolo/meinheld-gunicorn-flask:python3.6

COPY ./app /app

RUN pip install dash dash-html-components
