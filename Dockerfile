FROM python:3.6.1-alpine
WORKDIR /task2
ADD . /task2
RUN pip install -r requirements.txt
CMD ["python","assistant.py"]