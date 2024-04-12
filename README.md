# Run-time environment for browser extension testing

This repository contains the source code implemented as part of my master thesis at the University of Technology in Brno in 2023/2024. 

## Requirements
- [Docker](https://www.docker.com) must be installed on the host system. The **Docker Engine** must be running before building and deploying any of the containers. On Linux host machine, refrain from using *Docker Desktop*.
- In case of a **Windows host machine** you also need to install **X server** software in order to display any browser windows during the execution. None of the tests are performed in `headless` because many of the performed tests are not supported in that mode. During the developement and testing, [X410](https://x410.dev) was used. The **Dockerfiles** are configured to use `DISPLAY=host.docker.internal:0.0` which is supported by X410. Please note on Windows you need to install *Docker Desktop*.
- All other individual requirements are installed into the images while building them via Docker.

---

The overlap of technologies used in both testing modes isn't very large and the environment isn't designed to defaultly run both testing modes subsequently, as the integration testing is expeced to be executed more frequently than system testing. To save space and time, both testing modes have their own **Dockerfile**.

Building either of the images from their respective **Dockerfiles** might take several minutes based on the internet speed and host machine capacity. After the first build, build data is cached through *Docker*, so subsequent builds take very litte time, unless the cache is cleared with the `docker system prune -a` command.

## Contents
- The `integration_testing` folder contains the code base needed to perform integration browser extension testing as described in detail in the thesis. It also contains the **Dockerfile** needed to build the environment image.
- The `system_testing` folder similarly contains the code base for system testing as well as a **Dockerfile**.