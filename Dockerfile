FROM python:3.8-slim

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y \
curl

COPY ./app/. .

CMD [ "python", "index.py" ]