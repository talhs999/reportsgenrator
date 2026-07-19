FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for WeasyPrint and Playwright
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget gnupg \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    libcairo2 \
    libffi-dev \
    libgdk-pixbuf2.0-0 \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers and its OS dependencies
RUN playwright install chromium
RUN apt-get update && playwright install-deps chromium && rm -rf /var/lib/apt/lists/*

COPY . .

RUN mkdir -p static/uploads static/downloads static/temp

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
