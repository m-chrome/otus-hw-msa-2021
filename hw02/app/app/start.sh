# Run migrations
alembic upgrade head

# Run server
uvicorn main:app --host 0.0.0.0 --port 80
