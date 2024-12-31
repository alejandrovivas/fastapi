FROM python:3.12

ENV PYTHONUNBUFFERED = 1

WORKDIR /fastAPI

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

EXPOSE 9000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9000", "--reload"]