FROM python:3.12.9-slim

WORKDIR /app

COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN uv sync --frozen --no-install-project --no-cache-dir

COPY api ./api
COPY models ./models
COPY README.md README.md
COPY src ./src

RUN uv sync --frozen --no-cache-dir

CMD ["uv", "run", "uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "8080"]
