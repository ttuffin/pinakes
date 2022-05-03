FROM docker.io/postgres:13-alpine

ARG SOURCE_ROOT_CA=root.crt
ARG SOURCE_CERT_FILE=server.crt
ARG SOURCE_CERT_KEY=server.key

ENV CERT_PATH="/etc/ssl_config/"

RUN mkdir ${CERT_PATH}

ADD --chown=postgres:postgres *.crt ${CERT_PATH}
ADD --chown=postgres:postgres *.key ${CERT_PATH}

RUN chmod -R 0600 ${CERT_PATH}*
