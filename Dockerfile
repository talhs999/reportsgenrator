FROM python:3.10-slim-bookworm

WORKDIR /app

# Install system dependencies for WeasyPrint and general use
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    gnupg \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libcairo2 \
    libffi-dev \
    libgdk-pixbuf-2.0-0 \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright Chromium and its OS dependencies
RUN playwright install chromium && playwright install-deps chromium

COPY . .

RUN mkdir -p static/uploads static/downloads static/temp

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
