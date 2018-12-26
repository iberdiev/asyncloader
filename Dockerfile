# asyncloader
# Version: 1.0

FROM python:3.5
RUN mkdir /asyncloader
WORKDIR /asyncloader
ADD . /asyncloader/
RUN pip install -r requirements.txt

