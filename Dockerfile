FROM python:3.10-slim-buster

RUN mkdir -p /opt/app/mytown
WORKDIR /opt/app/mytown

RUN pip install poetry

COPY poetry.lock .
COPY pyproject.toml .

RUN apt update && apt install -y libpq-dev build-essential
RUN poetry export -f requirements.txt --output requirements.txt --dev
RUN pip install -r requirements.txt

COPY . .

CMD ["./scripts/wait-for-it.sh", "postgresql:5432", "--", "./run.sh"]