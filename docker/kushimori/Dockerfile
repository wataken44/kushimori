FROM wataken44/ubuntu-latest-sshd
LABEL maintainer "wataken44"

ENV DOCKER "YES"
ENV LANG C.UTF-8

RUN set -xe \
    && apt update -y \
    && apt dist-upgrade -y \
    && apt install -y git-core

RUN set -xe \
    && apt update \
    && apt install -y lsb-release curl gnupg python3.7

RUN set -xe \
    && echo "deb http://packages.cloud.google.com/apt cloud-sdk-$(lsb_release -c -s) main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && apt update \
    && apt install -y google-cloud-sdk google-cloud-sdk-app-engine-python google-cloud-sdk-app-engine-python-extras google-cloud-sdk-datastore-emulator


USER ubuntu

RUN set -xe \
    && cd /home/ubuntu/ \
    && git clone https://github.com/wataken44/kushimori
    
USER root

EXPOSE 22
CMD  service ssh start && tail -f /dev/null
