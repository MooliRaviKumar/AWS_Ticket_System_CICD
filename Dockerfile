# 1. Base Image
FROM python:3.12-slim

# 2. Environment Config
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Working Directory
WORKDIR /app

# 4. Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    && apt-get clean

# 5. Copy dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy project files
COPY . .

# 7. Collect static files (optional for production)
RUN python manage.py collectstatic --noinput

# 8. Expose port
EXPOSE 8000

# 9. Run with Gunicorn
CMD ["gunicorn", "support_app.wsgi:application", "--bind", "0.0.0.0:8000"]
