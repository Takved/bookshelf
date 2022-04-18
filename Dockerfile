# 
FROM python:3.10-slim

# 
WORKDIR /code

# 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN pip install fastapi fastapi-sqlalchemy pydantic alembic asyncpg uvicorn

# 
COPY ./app/* /code/

# 
ENV PYTHONPATH "${PYTHONPATH}:/code"


