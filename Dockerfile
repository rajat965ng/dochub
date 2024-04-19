FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501


ENTRYPOINT ["streamlit", "run", "frontend/frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]