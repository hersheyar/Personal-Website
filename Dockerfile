# Dockerfile for Django

# Base image
FROM python:3.10-slim

# Set environment vars
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && pip install whitenoise

# Copy project files
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port for EC2 with Route 53
EXPOSE 8080

# Default command
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8080"]
