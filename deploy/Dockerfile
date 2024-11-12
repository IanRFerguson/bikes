FROM python:3.10-bullseye

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "source/python/run_analytics.py"]
# CMD ["sleep", "infinity"]