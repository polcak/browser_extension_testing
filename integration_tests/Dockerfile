ARG OS_TYPE

FROM ubuntu:latest


ARG DEBIAN_FRONTEND=noninteractive
RUN echo "===> Installing system dependencies..." && \
    BUILD_DEPS="curl unzip" && \
    apt-get update && apt-get install --no-install-recommends -y \
    python3 python3-pip wget \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 libgbm1 libpci-dev libegl-dev libgtk-3-dev libu2f-udev libvulkan1\
    $BUILD_DEPS \
    xvfb 

RUN  apt install -yq software-properties-common 

RUN apt install openssl

RUN pip3 install selenium
RUN pip3 install flask

RUN pip3 install flask_babel

RUN pip3 install webdriver-manager

RUN pip3 install pytest

RUN pip3 install pyopenssl
RUN pip3 install regex
RUN pip3 install numpy

RUN pip3 install ndg-httpsclient
RUN pip3 install pyasn1

RUN pip3 install urllib3

ENV DISPLAY=host.docker.internal:0.0


WORKDIR /usr/app/src
COPY testing_environment ./

RUN ["chmod", "+x", "./start_testing.sh"]

ENTRYPOINT ["/usr/app/src/start_testing.sh"]


