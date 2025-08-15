# Use Python base image
FROM python:3.11-slim

# Install netcat for database connection checking
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Make entrypoint script executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Collect static files (optional for APIs)
RUN python manage.py collectstatic --noinput --settings=credit_approval.settings || true

# Set entrypoint
ENTRYPOINT ["/entrypoint.sh"]

# Run server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]