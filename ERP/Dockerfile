# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /ERP

# Copy the requirements file into the container
COPY requirements.txt /ERP/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /ERP/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Set environment variables to disable buffering
ENV PYTHONUNBUFFERED=1

# Run database migrations and collect static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
