FROM python:3.7-slim

RUN mkdir /nxtnr

RUN pip install --upgrade pip

COPY requirements.txt /nxtnr
RUN pip3 install -r /nxtnr/requirements.txt --no-cache-dir

COPY . /nxtnr
WORKDIR /nxtnr

COPY ./entrypoint.sh /nxtnr
RUN chmod 755 entrypoint.sh
ENTRYPOINT ["/nxtnr/entrypoint.sh"]