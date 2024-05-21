# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application files into the container
COPY . .

# Copy the offline packages into the container
COPY offline-packages /offline-packages

# Install dependencies from the offline packages
RUN pip install --no-index --find-links=/offline-packages -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Command to run the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "DjangoHUD.wsgi:application"]
