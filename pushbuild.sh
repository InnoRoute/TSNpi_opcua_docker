#!/bin/bash
datum=$(date +%s)
docker build -t innoroute/tsnpi_opcua:$datum ./build/
docker push innoroute/tsnpi_opcua:$datum
#docker buildx build --push --platform linux/arm/v7  --tag innoroute/tsnpi_opcua:$datum ./build/
