FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libxft2 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

CMD ["python", "gmm.py"]
