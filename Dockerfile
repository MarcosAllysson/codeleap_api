FROM python:3.12-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc python3-dev libpq-dev musl-dev libc-dev gettext netcat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh

EXPOSE 8000

# CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "./entrypoint.sh"]