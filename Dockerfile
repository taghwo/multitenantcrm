FROM python:3.7

ENV PYTHONUNBUFFERED=1

WORKDIR /var/www/html

COPY requirements.txt /var/www/html/

RUN pip install -r requirements.txt

COPY . /var/www/html/

RUN chown -R $USER:$USER .
