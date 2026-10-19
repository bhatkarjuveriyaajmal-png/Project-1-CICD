
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
