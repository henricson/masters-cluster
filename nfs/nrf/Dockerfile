# Use an official Python runtime as a parent image
FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1
# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]