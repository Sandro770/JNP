# Use the official Python 3 base image
FROM python:3

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt
RUN pip install python-dotenv

# Copy the rest of the application code to the container
COPY . /app

# Expose port 8000
#EXPOSE 8000

# Start the Django server
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
