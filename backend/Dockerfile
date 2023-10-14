FROM python:3.10

WORKDIR /opt/sqilte_to_postgres

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt --no-cache-dir

COPY ./src .

COPY script.sh /

RUN chmod +x /script.sh

ENTRYPOINT ["/script.sh"]