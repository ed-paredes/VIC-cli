FROM    python:3.9-slim

RUN apt-get -qq update && \ 
    pip install --upgrade pip && \
    apt-get -qq install -y wget && \
    mkdir /etc/dataset
ENV DIR=/etc/dataset
# RUN  export DATE=`date "+%Y%m%d"` && wget -q https://analisi.transparenciacatalunya.cat/api/views/irki-p3c7/rows.csv -O ${DIR}/vaccinations_${DATE}.csv
COPY . /vic
WORKDIR /vic
RUN pip install -e .