FROM python:3.7

COPY serve.py weatherpi/ ./

RUN pip install fastapi uvicorn sqlalchemy

EXPOSE 80

CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "80"]
