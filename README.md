# Run-time environment for browser extension testing

This repository contains the source code implemented as part of my master thesis at the University of Technology in Brno in 2023/2024. 

## Requirements
- [Docker](https://www.docker.com) must be installed on the host system, as well as **Docker Compose**. The **Docker Engine** must be running before building and deploying any of the containers. On Linux host machine, refrain from using *Docker Desktop*.
- In case of a **Windows host machine** you also need to install **X server** software in order to display any browser windows during the execution. None of the tests are performed in `headless` because many of the performed tests are not supported in that mode. During the developement and testing, [X410](https://x410.dev) was used. Please note on Windows you need to install *Docker Desktop*.
- For *Windows*, *Firefox* also requires *Pulseaudio* for webaudio testing. Download [Pulseaudio binaries](https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/Support/) and extract them anywhere you like. Then add the line `load-module module-native-protocol-tcp listen=0.0.0.0 auth-anonymous=1` into the `etc/pulse/default.pa` file and start *Pulseaudio* from `bin/pulseaudio.exe --use-pid-file=false -D`.
- All other individual requirements are installed into the images while building them via Docker.

---

Building either of the images from the **Dockerfile** might take several minutes based on the internet speed and host machine capacity. After the first build, build data is cached through *Docker*, so subsequent builds take very litte time, unless the cache is cleared with the `docker prune` command.

## Contents
- The `integration_testing` folder contains the code base needed to perform integration browser extension testing as described in detail in the thesis. 
- The `system_testing` folder similarly contains the code base for system testing.

## How to build
The **Dockerfile** takes advangate of multi-stage builds. The overlap of technologies is not huge so this is done in order to save space and time. 

### How to build an image and run a container for integration testing
To build the image and run the container on *Linux* host, run the following command:
```bash
docker-compose run --rm --service-ports testing_integration_linux
```
In order to build an image and run a container for integration testing on *Windows* host (assuming *Docker Desktop*, *Xserver* and *Pulseaudio* are running), use this command:
```bash
docker-compose run --rm --service-ports testing_integration_windows
```
### How to build an image and run a container for system testing
To build the image and run the container on *Linux* host, run the following command:
```bash
docker-compose run --rm --service-ports testing_system_linux
```
In order to build an image and run a container for system testing on *Windows* host (assuming *Docker Engine* is running), use this command:
```bash
docker-compose run --rm --service-ports testing_system_windows
```
If you run into privileges issues on *Linux*, try giving both `start_testing.sh` scripts execution privileges on the local machine.

```bash
sudo chmod +x ./integration_testing/start_testing.sh
sudo chmod +x ./system_testing/start_testing.sh
```
If you run into display issues, try adding *Docker* to *xhost*:
```bash
sudo xhost +local:docker
```