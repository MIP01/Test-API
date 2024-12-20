# Gunakan base image Python yang sesuai
FROM python:3.12.3

# Set working directory di dalam container
WORKDIR /app

# Salin file requirements.txt ke working directory
COPY requirements.txt /app/

# Install dependencies dari requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh isi proyek ke dalam container
COPY . /app

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Jalankan aplikasi dengan Gunicorn
CMD ["gunicorn", "app:app"]