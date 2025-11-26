FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn uvicorn

# Copy all project files
COPY . .

# EXPOSE port
EXPOSE 8000

# Gunicorn command with 1 Uvicorn worker
CMD ["gunicorn", "main:app", \
     "--workers", "1", \
     "--worker-class", "uvicorn.workers.UvicornWorker", \
     "--bind", "0.0.0.0:8000"]
