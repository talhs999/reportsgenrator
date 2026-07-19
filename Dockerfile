# Use official Python image (bullseye is very stable and has all dependencies)
FROM python:3.10-bullseye

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers and all required system dependencies automatically
RUN playwright install chromium
RUN playwright install-deps chromium

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p static/uploads static/downloads static/temp

# Expose port
EXPOSE 8000

# Start Uvicorn server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
