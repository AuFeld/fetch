FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6
COPY requirements.txt .
RUN pip install -r requirements.txt 
COPY ./app /app
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400" ]