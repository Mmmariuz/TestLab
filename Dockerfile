# Bruk offisiell Python image
FROM python:3.11-slim

# Sett arbeidsmappe
WORKDIR /app

# Kopier nødvendige filer
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopier resten av prosjektet
COPY . .

# Eksponer porten Flask bruker
EXPOSE 5000

# Start appen
CMD ["python", "app.py"]
