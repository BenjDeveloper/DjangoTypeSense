# Dockerfile
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy all the project files into the container
COPY ./src /app

# Copy requirements.txt into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command to wait for db and start Django
CMD ["sh", "-c", "python wait_for_db.py && python manage.py runserver 0.0.0.0:8000"]


