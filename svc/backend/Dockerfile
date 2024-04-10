FROM python:3.10-bullseye

WORKDIR /app
ADD requirements.txt ./
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --no-cache -r requirements.txt

COPY . ./
CMD ["python", "app.py"]