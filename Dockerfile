FROM python:3.13

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        gfortran \
    # Limpa o cache para reduzir o tamanho da imagem.
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml .

RUN uv pip install --system --upgrade --no-cache-dir .

COPY . .

CMD ["python", "fake_generate.py"]