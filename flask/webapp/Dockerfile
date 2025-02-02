# Use the official Python image from the Docker Hub with an Alpine variant
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (for compiling certain packages like Flask)
RUN apk update && apk add --no-cache gcc libffi-dev musl-dev

# Copy requirements.txt first to install dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files into the container (app.py and templates folder)
COPY app.py .
COPY templates/ ./templates/

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]