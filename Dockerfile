FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md LICENSE ./
COPY src ./src

RUN pip install --no-cache-dir -e . pytest

COPY samples ./samples
COPY tests ./tests

ENV PYTHONPATH=/app/src

CMD ["python", "samples/generate_samples.py"]