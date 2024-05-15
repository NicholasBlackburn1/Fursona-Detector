# Use the official TensorFlow Docker image as the base image
FROM tensorflow/tensorflow:latest-gpu

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to the system path
ENV PATH="${PATH}:/root/.poetry/bin"


# Set working directory
WORKDIR /app

# Copy only the poetry files first to leverage Docker layer caching
COPY poetry.lock pyproject.toml /app/

# Install dependencies
CMD ["/root/.poetry/bin/poetry", "install",  "--no-root --no-interaction"]

# Copy the rest of the application code
COPY . /app

# Specify the command to run on container start
CMD ["/root/.poetry/bin/poetry", "run", "python3 random_model.py"]