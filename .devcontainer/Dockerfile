# Use official Python 3.11 image
FROM python:3.11-slim

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libproj-dev \
    proj-data \
    proj-bin \
    libgeos-dev \
    libgeos++-dev \
    libgdal-dev \
    gdal-bin \
    libcartopy-dev \
    python3-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /workspace

# Install pip & Jupyter
RUN pip install --upgrade pip && \
    pip install jupyter

# Default command
CMD ["bash"]
