FROM python:3.7

RUN pip install fastapi uvicorn

EXPOSE 80

CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "80"]
