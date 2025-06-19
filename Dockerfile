FROM python:3.11.9-alpine3.19

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install build dependencies for compiling some Python packages (e.g. pandas, lxml)
RUN apk update && \
    apk add --no-cache gcc musl-dev libffi-dev && \
    rm -rf /var/cache/apk/*

COPY requirements.txt requirements.txt
COPY requirements-dev.txt requirements-dev.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY app app
COPY main.py main.py
COPY .env.example .env.example
COPY pyproject.toml pyproject.toml

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "main:app"]
