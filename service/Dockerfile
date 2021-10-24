FROM python:3.10

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
