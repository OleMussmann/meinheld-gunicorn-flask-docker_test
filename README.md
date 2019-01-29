# Minimal example to run a [dash](https://dash.plot.ly/) flask app with [meinheld-gunicorn-flask-docker](https://github.com/tiangolo/meinheld-gunicorn-flask-docker)

Minimal working example to triage https://github.com/tiangolo/meinheld-gunicorn-flask-docker/issues/2.

## build
```
git clone git@github.com:OleMussmann/meinheld-gunicorn-flask-docker_test.git
cd meinheld-gunicorn-flask-docker_test
sudo docker build -t my_flask_app .
```

## run (fails)

While running a plot [dash](https://dash.plot.ly/) flask app, the app only loads in the browser if I _don't_ specify a worker type. The `entrypoint.sh` script sets it to `egg:meinheld#gunicorn_worker`. With this option the app stalls on 'Loading ...' in the browser. 

```
sudo docker run -d -p 5000:80 my_flask_app
```

## run (works)

When running gunicorn inside the container by hand - without the worker type option - it loads just fine.

```
sudo docker run -it -p 5000:80 dash bash -c "gunicorn -b 0.0.0.0:80 main:app"
```

or

```
sudo docker run -it -p 5000:80 dash bash
gunicorn -b 0.0.0.0:80 main:app
```

# Triaging [bug #2](https://github.com/tiangolo/meinheld-gunicorn-flask-docker/issues/2)
The combination of the `static_folder='assets'` option in the line
```
app = flask.Flask(__name__, static_folder='assets')
```
and the setting
```
dash_app.scripts.config.serve_locally = True
```
seem to be responsible for stalling the `meinheld` runner. Removing either of these - or both - will prevent the stalling.
