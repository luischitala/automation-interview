# Use the official Python Slim image as the base image
FROM python:3.9-slim

# Install necessary packages to build psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install FastAPI, Uvicorn, and psycopg2 dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire FastAPI application to the container
COPY . .

# Expose port 5000 (assuming your FastAPI app is running on this port)
EXPOSE 5000

# Start the FastAPI application using Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
