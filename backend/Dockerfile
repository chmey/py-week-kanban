FROM python:3.8-alpine

RUN adduser -D app
WORKDIR /home/app
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install gunicorn wheel
RUN venv/bin/pip install -r requirements.txt

COPY kanweek kanweek

RUN chown -R app:app ./
USER app


EXPOSE 5000
ENTRYPOINT ["venv/bin/gunicorn", "--bind", "0.0.0.0:5000", "kanweek.app:app"]