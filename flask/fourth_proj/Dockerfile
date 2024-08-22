# Use the official Python 3.9 slim image as the base image
FROM python:3.9-slim

# Create the app directory inside the container
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the application code and requirements file into the container
COPY src/requirements.txt /app/
COPY src/ /app/src/

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the port that the application will run on
EXPOSE 5000

# Define the command to run the application
CMD ["python", "src/app.py"]
