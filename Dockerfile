FROM python:3.10-alpine

WORKDIR /app

COPY . /app

COPY dev_requirements.txt ./
RUN pip install --upgrade pip && pip install --no-cache-dir -r dev_requirements.txt

CMD ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]
