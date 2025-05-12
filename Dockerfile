FROM python:3.11.10-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1

RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "app/app.py"]

