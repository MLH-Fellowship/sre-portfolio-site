FROM python:3.8-slim-buster

RUN mkdir /myportfolio
COPY requirements.txt /myportfolio
WORKDIR /myportfolio
RUN pip3 install -r requirements.txt

COPY . /myportfolio

CMD ["gunicorn", "wsgi:app", "-w 4", "-b 0.0.0.0:5000"]