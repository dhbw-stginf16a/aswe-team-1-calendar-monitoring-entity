#!/bin/bash

echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t asweteam1/calendar-monitor:latest -t asweteam1/calendar-monitor:$TRAVIS_TAG --label version="$TRAVIS_TAG" .
docker push asweteam1/calendar-monitor:latest
docker push asweteam1/calendar-monitor:$TRAVIS_TAG
