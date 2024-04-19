FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 8501

ENTRYPOINT ["poetry", "run", "streamlit", "run", "frontend/frontend/app.py"]