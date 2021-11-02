# Python base image
FROM python:3.8-slim

# Where the API server lives
WORKDIR /app/

# Install required dependencies
COPY requirements/inference.txt /app/requirements.txt
RUN pip install -r ./requirements.txt

# API related files
COPY ./src/inference/ /app/ 
COPY ./src/training/model.pickle /app/src/training/model.pickle

# Container port on which the server will be listening
EXPOSE 5000

# Launch flask app
ENTRYPOINT python app.py
