FROM ubuntu:bionic
COPY image_files/ /

RUN apt-get update -y \
    && echo "export LC_ALL=C.UTF-8" >> ~/.bashrc \
    && echo "export LANG=C.UTF-8" >> ~/.bashrc \
    && apt-get install -y \
    python3 python3-pip cron\
    && pip3 install elasticsearch-curator jinja2 \
    && touch /var/log/curator.log \
    && echo "0 0 * * * root  /bin/bash /purge-old-logs.sh >> /var/log/curator.log 2>&1" > /etc/crontab

ENV \
  ELASTICSEARCH_IP='127.0.0.1' \
  ELASTICSEARCH_PORT='9200' \
  ELASTICSEARCH_USER='' \
  ELASTICSEARCH_PASS='' \
  RETENTION_PERIOD='14'

CMD /start.sh
