FROM tiangolo/meinheld-gunicorn-flask:python3.6

COPY ./app /app
COPY ./Pipfile /
COPY ./Pipfile.lock /

RUN pip install pipenv
RUN pipenv install --system --deploy
