FROM ubuntu:latest AS base
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3 python3-pip wget \
    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
    libnspr4 libnss3 lsb-release xdg-utils libxss1 libdbus-glib-1-2 libgbm1 libpci-dev libegl-dev libgtk-3-dev libvulkan1 \
    curl unzip software-properties-common
RUN pip3 install selenium webdriver-manager numpy

FROM base AS system
COPY --from=base /bin/ /bin/
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install --no-install-recommends -y \
    default-jre \
    libu2f-udev \
    xvfb
RUN pip3 install opencv-python scikit-learn nltk python-Levenshtein
WORKDIR /usr/app/src
COPY system_tests ./
RUN ["chmod", "+x", "./start_testing.sh"]
ENTRYPOINT ["/usr/app/src/start_testing.sh"]

FROM base AS integration
COPY --from=base /bin/ /bin/
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get install -y openssl
RUN pip3 install  flask flask_babel pytest pyopenssl regex ndg-httpsclient pyasn1 urllib3
WORKDIR /usr/app/src
COPY integration_tests ./
RUN ["chmod", "+x", "./start_testing.sh"]
ENTRYPOINT ["/usr/app/src/start_testing.sh"]
