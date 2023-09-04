# Inspired by https://github.com/judge0/compilers/blob/master/Dockerfile

FROM ubuntu:jammy
RUN apt-get update

# setup required compilers & interpreters
RUN apt-get install -y --no-install-recommends \
    gcc g++ python3.11

# setup isolate
# TODO: setup and download to seperate image, keep only required binary.
RUN set -xe && \
    apt-get update && \
    apt-get install -y --no-install-recommends git libcap-dev make && \
    rm -rf /var/lib/apt/lists/* && \
    GIT_SSL_NO_VERIFY=true git clone https://github.com/ioi/isolate.git /tmp/isolate && \
    cd /tmp/isolate && \
    git checkout v1.10.1 && \
    make -j$(nproc) install && \
    rm -rf /tmp/*

# setup cpts
# TODO: do not keep pip in final image.
ARG CPTS_VERSION
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip && \
    python3.11 -m pip install cpts==${CPTS_VERSION}
