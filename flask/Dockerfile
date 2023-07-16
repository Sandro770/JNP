# Use the official Python 3 base image
FROM python:3

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt
RUN pip install python-dotenv


# Copy the rest of the application code to the container
COPY . .

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Copy the supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose port 5000
EXPOSE 5000

# Start supervisor to manage the processes
CMD ["/usr/bin/supervisord"]
