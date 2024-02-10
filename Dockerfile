FROM postgres:16.1-alpine3.19

WORKDIR /app
COPY . /app

# install packages;
# NOTE: NeoVim is added for convenience.
RUN \
    apk update && \
    apk add \
        nano \
        neovim \
        python3 \
        py3-pip
RUN python3 -m pip install psycopg --break-system-packages

# prepare postgresql
USER postgres
RUN \
    chmod 0700 /var/lib/postgresql/data &&\
    initdb /var/lib/postgresql/data &&\
    echo "host all  all    0.0.0.0/0  md5" >> /var/lib/postgresql/data/pg_hba.conf &&\
    echo "listen_addresses='*'" >> /var/lib/postgresql/data/postgresql.conf &&\
    pg_ctl start && \
    psql -f db.sql && \
    pg_ctl stop

CMD pg_ctl start > /dev/null && python3 /app/cmd.py
