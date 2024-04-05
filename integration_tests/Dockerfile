#FROM ubuntu:latest

#ARG DEBIAN_FRONTEND=noninteractive
ARG OS_TYPE


#RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
#RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'

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

#RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
#RUN apt-get install -y --fix-missing ./google-chrome-stable_current_amd64.deb

RUN  apt install -yq software-properties-common 
     #&& add-apt-repository ppa:mozillateam/ppa \
     #&& apt-get update \
     #&& apt-get install -y firefox-esr \
     #&& rm -rf /var/lib/apt/lists/*

RUN apt install openssl

RUN pip3 install selenium
RUN pip3 install flask

RUN pip3 install flask_babel

RUN pip3 install webdriver-manager

RUN pip3 install pytest

RUN pip3 install pyopenssl
RUN pip3 install output

RUN pip3 install regex
RUN pip3 install numpy

ENV DISPLAY=host.docker.internal:0.0


WORKDIR /usr/app/src
COPY testing_environment ./

RUN ["chmod", "+x", "./start_testing.sh"]

ENTRYPOINT ["/usr/app/src/start_testing.sh"]

#ENTRYPOINT ["python3", "./fingerprinting_server/run.py", ">", "log.txt"]


