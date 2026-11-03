<<<<<<< HEAD
FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 5000

CMD ["python", "-m", "app.main"]
=======

# Use Python 3.13 as the base image
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependency list first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app/

# Document the application port
EXPOSE 5000

# Start the Flask application
CMD ["python", "app/main.py"]
>>>>>>> 86daa463c7aa66dc5603dfa0c0e8ea7f96c1d1c3
