# Elasticsearch Curator
Elasticsearch curator container can be used to purge indices older than `RETENTION_PERIOD`.

## Build image
Clone this repo and run docker build command to build curator image.
```
git clone https://github.com/breqwatr/curator.git
cd curator
docker build . -t <image-name>:<tag>
```

## Curator container
Run this command to start curator container. It will delete indices older than `RETENTION_PERIOD` every midnight.
```
docker run -d -it --name curator \
  --network host --env ELASTICSEARCH_IP=<elasticsearch-ip> \
  --env ELASTICSEARCH_PORT=<elasticsearch-port> \
  --env RETENTION_PERIOD=<number-of-days> \
  --env ELASTICSEARCH_USER=<elasticsearch-username> \
  --env ELASTICSEARCH_PASS=<elasticsearch-password> \
  <image-name>:<tag>
  
# ELASTICSEARCH_IP:   Elasticsearch ip address. (Default=127.0.0.1)
# ELASTICSEARCH_PORT: Elasticsearch port address. (Default=9200)
# RETENTION_PERIOD:   Indices older than this number of days will be deleted. (Default=14)
# ELASTICSEARCH_USER: Elasticsearch username. Only use it if authentication is enabled on elasticsearch. (Default='')
# ELASTICSEARCH_PASS: Elasticsearch password. Only use it if authentication is enabled on elasticsearch. (Default='')
```
