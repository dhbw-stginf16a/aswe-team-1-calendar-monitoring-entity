FROM python:3.6

LABEL maintainer="Thore Kruess"

RUN pip install pipenv

RUN pipenv install --deploy --system

COPY . /app

WORKDIR /app

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:application"]
