FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libaio1 \
    unzip \
    wget \
    gcc \
    build-essential

# Oracle Instant Client
RUN mkdir -p /opt/oracle && \
    cd /opt/oracle && \
    wget https://download.oracle.com/otn_software/linux/instantclient/2113000/instantclient-basiclite-linux.x64-21.13.0.0.0dbru.zip && \
    unzip instantclient-basiclite-linux.x64-21.13.0.0.0dbru.zip && \
    rm instantclient-basiclite-linux.x64-21.13.0.0.0dbru.zip && \
    echo "/opt/oracle/instantclient_21_13" > /etc/ld.so.conf.d/oracle-instantclient.conf && \
    ldconfig

ENV LD_LIBRARY_PATH="/opt/oracle/instantclient_21_13"
ENV ORACLE_HOME="/opt/oracle/instantclient_21_13"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir cx_Oracle

COPY . .

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/entrypoint.sh"]
