###################################
# Google Cloud Project SDK Docker #
###################################

# Based on...
FROM google/cloud-sdk:latest

# File Author / Maintainer
LABEL maintainer="ebelter@wustl.edu"

# Args
ARG username=ebelter

# Deps
RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
  less \
  libnss-sss \
  sudo \
  vim && \
  apt-get clean

# Upgrade Components
RUN sudo apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get --only-upgrade install -y --no-install-recommends \
  kubectl \
  google-cloud-sdk \
  google-cloud-sdk-app-engine-grpc \
  google-cloud-sdk-pubsub-emulator \
  google-cloud-sdk-app-engine-go \
  google-cloud-sdk-datastore-emulator \
  google-cloud-sdk-app-engine-python \
  google-cloud-sdk-cbt \
  google-cloud-sdk-bigtable-emulator \
  google-cloud-sdk-app-engine-python-extras \
  google-cloud-sdk-datalab \
  google-cloud-sdk-app-engine-java

# CRC
RUN DEBIAN_FRONTEND=noninteractive apt-get install gcc python-dev python-setuptools && \
  apt-get clean && \
  easy_install -U pip && \
  pip uninstall --yes crcmod && \
  pip install -U crcmod

# HL CLOUD
WORKDIR /tmp/hl-cloud/
COPY setup.py README.cli LICENSE hlcloud/ ./
COPY hlcloud/ hlcloud/
RUN pip install ./
WORKDIR /tmp/
RUN rm -rf hl-cloud/

# Cloudy User
RUN useradd -Ms /bin/bash cloudy -G staff
RUN echo "cloudy ALL=(ALL:ALL) NOPASSWD: ALL" | sudo EDITOR='tee -a' visudo
WORKDIR /home/cloudy
COPY resources/homedir ./
RUN chown -R cloudy /home/cloudy/ && \
  chgrp -R cloudy /home/cloudy/ && \
  find ./ -type d -exec chmod 755 {} \; && \
  find ./ -type f -exec chmod 644 {} \;

# ENVs and Default Command
USER cloudy
ENV HOME /home/cloudy
CMD [ /bin/bash ]