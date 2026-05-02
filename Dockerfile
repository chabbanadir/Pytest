# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install pytest
RUN pip install pytest

# Copy everything into the container
COPY . .

# Define an environment variable (can be overridden at runtime)
ENV MY_ENV_VAR="Docker Default"

# Run the script when the container launches
CMD ["python", "hello.py"]
