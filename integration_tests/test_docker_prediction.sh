#!/usr/bin/env bash

set -e

IMAGE_NAME="used-car-price-prediction"

docker build -t ${IMAGE_NAME} .

OUTPUT=$(docker run --rm ${IMAGE_NAME})

echo "$OUTPUT"

echo "$OUTPUT" | grep "Predicted price:"