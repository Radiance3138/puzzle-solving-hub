# Stage 1: Base build stage
FROM python:3.14-slim-bookworm AS builder
 
# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 
ENV PATH="/root/.local/bin/:$PATH"

# Set the working directory
WORKDIR /app

RUN apt-get update && apt-get install -y curl

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Upgrade pip and install dependencies
RUN pip install --upgrade pip 
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency files and install (uv sync will read pyproject.toml)
COPY pyproject.toml uv.lock ./
 
# Install Python dependencies
RUN uv sync --locked
 
# Stage 2: Development stage
FROM python:3.14-slim-bookworm

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Set the working directory
WORKDIR /app

# Install runtime system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.14/site-packages/ /usr/local/lib/python3.14/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --from=builder /bin/uv /usr/local/bin/uv

# Copy application code
COPY . .
 
# Expose the application port
EXPOSE 8000

# Default command to run the Django server
CMD ["uv", "run", "manage.py", "runserver", "0.0.0.0:8000"]