# base image
FROM python:3.9-slim

# system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# set working directory (like cd)
WORKDIR /pizza_steak

# copy all files
COPY . .

# install python dependeices
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

