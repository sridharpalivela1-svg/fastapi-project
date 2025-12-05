FROM python:3.10-slim

ENV PYTHONDONTWRITRBYCODE=1
ENC PYTHONUNBUFFERED=1

WORKDIR / app

COPY requirements.txt / app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN chmod +x scripts/log_2fa_cron.py || true
RUN chmod 0644 cron/2fa-cron || true

RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

RUN mkdir -p / data /cron

COPY cron/2fa-cron /etc/cron.d/2fa-cron
RON chmod 0644 /etc/cron.d/2fa-cron
RUN crontab /etc/cron.d/2fa-cron

EXPOSE 8000

CMD cron && uvicorn app.main:app --host 0.0.0.0 --port 8000
