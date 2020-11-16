FROM python:3.8-alpine

RUN adduser -D app
WORKDIR /home/app
COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY kanweek kanweek
COPY migrations migrations
COPY kanweek.py run.py ./

ENV FLASK_APP kanweek.py

RUN chown -R app:app ./
USER app


EXPOSE 5000
ENTRYPOINT ["venv/bin/gunicorn", "--bind", "0.0.0.0:5000", "kanweek.wsgi:app"]