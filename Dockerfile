FROM python:3.10.3-slim as builder

RUN apt-get update -y && apt-get install -y --no-install-recommends \
	build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.10.3-slim

WORKDIR /app

ENV PATH="/opt/venv/bin:$PATH"

CMD uvicorn main:app --host 0.0.0.0 --port 8080

COPY --from=builder /opt/venv /opt/venv

COPY . .
