FROM ubuntu:latest


ARG DEBIAN_FRONTEND=noninteractive
RUN echo "===> Installing system dependencies..." && \
    BUILD_DEPS="curl unzip" && \
    apt-get update && apt-get install --no-install-recommends -y \
    python3 python3-pip wget \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 libgbm1 libpci-dev libegl-dev libgtk-3-dev libvulkan1\
    $BUILD_DEPS 

RUN apt-get update && \
    apt-get -y install default-jre 

RUN wget http://archive.ubuntu.com/ubuntu/pool/main/libu/libu2f-host/libu2f-udev_1.1.4-1_all.deb
RUN dpkg -i libu2f-udev_1.1.4-1_all.deb
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y --fix-missing ./google-chrome-stable_current_amd64.deb

RUN apt install -yq software-properties-common 

RUN pip3 install selenium
RUN pip3 install webdriver-manager
RUN pip3 install numpy

RUN pip3 install opencv-python

RUN pip3 install scikit-learn
RUN pip3 install nltk
RUN pip3 install python-Levenshtein


#ENV DISPLAY=host.docker.internal:0.0

WORKDIR /usr/app/src
COPY testing_environment ./

RUN ["chmod", "+x", "./start_testing.sh"]

ENTRYPOINT ["/usr/app/src/start_testing.sh"]





