#!/bin/bash


if [[ $(screen -ls | grep -c 'weather_backend') -eq 0 ]]
then
  source venv/bin/activate
  screen -S weather_backend -d -m \
    uvicorn backend.main:app --reload
  deactivate
fi
