# Run-time environment for browser extension testing

This repository contains the source code implemented as part of my master thesis at the University of Technology in Brno in 2023/2024. 

## Requirements
- [Docker](https://www.docker.com) must be installed on the host system. The **Docker Engine** must be running before building and deploying any of the containers. On Linux host machine, refrain from using *Docker Desktop*.
- In case of a **Windows host machine** you also need to install **X server** software in order to display any browser windows during the execution. None of the tests are performed in `headless` because many of the performed tests are not supported in that mode. During the developement and testing, [X410](https://x410.dev) was used. Please note on Windows you need to install *Docker Desktop*.
- For *Windows*, *Firefox* also requires *Pulseaudio* for webaudio testing. Download [Pulseaudio binaries](https://www.freedesktop.org/wiki/Software/PulseAudio/Ports/Windows/Support/) and extract them anywhere you like. Then add the line `load-module module-native-protocol-tcp listen=0.0.0.0 auth-anonymous=1` into the `etc/pulse/default.pa` file and start *Pulseaudio* from `bin/pulseaudio.exe`.
- All other individual requirements are installed into the images while building them via Docker.

---

Building either of the images from the **Dockerfile** might take several minutes based on the internet speed and host machine capacity. After the first build, build data is cached through *Docker*, so subsequent builds take very litte time, unless the cache is cleared with the `docker system prune -a` command.

## Contents
- The `integration_testing` folder contains the code base needed to perform integration browser extension testing as described in detail in the thesis. 
- The `system_testing` folder similarly contains the code base for system testing.

## How to build
The **Dockerfile** takes advangate of multi-stage builds. The overlap of technologies is not huge so this is done in order to save space and time. 

### How to build an image for integration testing
In order to build an image so you can run the container for integration testing, use this command:
```
docker build --tag=testing_integration --target=integration .
```
You can replace `testing_integration` with any container name representing integration testing container.
### How to build an image for system testing
Similarly to integration testing, you can build the image using command:
```
docker build --tag=testing_system --target=system . 
```
You can replace `testing_system` with any container name representing system testing container.