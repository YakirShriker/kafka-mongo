FROM python:3.6
ADD . .
#COPY requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "./producer.py" ]