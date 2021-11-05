#!/usr/bin/env bash

docker run \
  --rm \
  --name mongo \
  --env MONGO_INITDB_ROOT_USERNAME=root \
  --env MONGO_INITDB_ROOT_PASSWORD=example \
  --env MONGO_INITDB_DATABASE=sample \
  --volume $(pwd)/mongodb-sample-dataset/sample_analytics:/docker-entrypoint-initdb.d \
  --publish 27017:27017 \
  mongo