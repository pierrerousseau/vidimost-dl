FROM python:3.10

WORKDIR /code

COPY ./settings/requirements.txt /code/app/settings/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/app/settings/requirements.txt

COPY . /code/app

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
