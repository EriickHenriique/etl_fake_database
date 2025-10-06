FROM python:3.13

WORKDIR /app

RUN pip install uv --no-cache-dir

COPY pyproject.toml .

RUN uv pip install --system . --no-deps-hash --frozen

EXPOSE 8000

CMD ["uvicorn", "backend.fastapi:app", "--host", "0.0.0.0", "--port", "8000"]