FROM python:3.12

WORKDIR /app/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN ["chmod", "+x", "./deployment/scripts/start.sh"]

ENTRYPOINT ["bash", "./deployment/scripts/start.sh"]
