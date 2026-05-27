FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    gnupg \
    chromium \
    chromium-driver

ENV PATH="/usr/bin/chromedriver:$PATH"

CMD ["pytest", "--html=report.html", "--self-contained-html"]