# Use an official Python runtime as a parent image
FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8
# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install requests
RUN pip install --no-cache-dir requests

# Install ping and traceroute utilities
RUN apt-get update && \
    apt-get install -y --no-install-recommends iputils-ping traceroute && \
    rm -rf /var/lib/apt/lists/*

# Make port 5000 available to the world outside this container
EXPOSE 80

# Define environment variable to silence Flask server warning
ENV FLASK_ENV=development

# Run app.py when the container launches
CMD ["python", "app.py"]