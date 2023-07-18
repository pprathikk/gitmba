# Use the official Python base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire web application to the working directory
COPY . .

# Expose the port that the web application will listen on
EXPOSE 5000

# Define the command to run the web application
CMD [ "python", "app.py" ]
