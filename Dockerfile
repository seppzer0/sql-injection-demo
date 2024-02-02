FROM debian:bookworm-slim

WORKDIR /app
COPY . /app

# install packages
RUN \
    apt update && \
    apt install -y \
        postgresql \
        nano \
        neovim \
        gcc \
        g++ \
        cmake \
        python3 \
        python3-pip
RUN python3 -m pip install psycopg --break-system-packages

USER postgres
CMD service postgresql start && psql -f db.sql && python3 /app/cmd.py
