FROM python:3.9-slim

RUN pip install \
     --index https://pypi.attakei.net/simple/ \
    pypicloud[server,dynamo,gcs] pypicloud-firestore
RUN mkdir /app
WORKDIR /app

# For Minimum demo
COPY config.ini /app/
CMD [ "pserve", "config.ini" ]
