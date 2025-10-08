FROM python:3.13 

WORKDIR /app 

RUN pip install uv --no-cache-dir 

COPY pyproject.toml . 

RUN uv pip install --system .

RUN apt-get update && apt-get install -y iputils-ping netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY . /app

EXPOSE 8000

CMD ["uvicorn" , "backend.api.fastapi:app", "--app-dir", "/app", "--host", "0.0.0.0", "--port", "8000"]