# Integration testing

This folder contains the code base for integration testing of privacy enhancing extensions. Much of the code base was taken from the [**PETInspector project**](https://github.com/tadatitam/pet-inspector) conducted as part of a 2019 paper called [Evaluating Anti-Fingerprinting Privacy Enhancing Technologies](https://www1.icsi.berkeley.edu/~mct/pubs/www19.pdf). The fingerprinting server was originally created by Pierre Laperdrix in 2016 as [Fingerprint Central](https://github.com/plaperdr/fp-central). Analysis engine was completely omitted in the thesis and instead replaced by a new mechanism designed to test the expected results against retrieved results. This mechanism is based on the original integration tests implemented in thesis [Automatic testing of JavaScript Restrictor project](https://www.vut.cz/studenti/zav-prace/detail/129897). The original project also allowed users to test in different OS settings, although by the time of writing this thesis, this feature no longer worked at all. Due to this and the nature of Docker virtualization, it has been removed entirely. A **Dockerfile** is also included in this folder.

The original code base has been heavily modified to take advantage of a feature implemented by [Selenium](https://www.selenium.dev) in 2022 called [Selenium Manager](https://www.selenium.dev/documentation/selenium_manager/). Some of the new features include:
- The ability to perform tests with multiple extensions installed. This includes different combinations of available extensions. 
- Testing using different available browser versions for both Google Chrome and Mozilla Firefox.
- Several new techniques intended to test the extension's ability to block or alter data retrieved by the server.
- Performing client-side testing.


Please note that this tool does not serve as an evaluation of a browsers extension's ability to protect against fingerprinting. This tool was designed as a way for users and developers to see and analyze the extension's behavior in a controlled, deterministic and transparent settings while also giving them the ability to see how multiple installed extensions affect each other and their outputs. It does not accurately represent the reality of fingerprinting servers, it only simulates their behavior.

## How to build the image and run the container
### Linux based host
In order to run the testing you must have `docker engine` installed, NOT `Docker Desktop`. This is due to how it handles display forwarding.

Currently you must keep the envirnoment setting commented out inside the *Dockerfile* while building on Linux host.
```
#ENV DISPLAY=host.docker.internal:0.0
```

Assuming you have installed `docker engine` correctly and it is running, build the image using this command:
```
docker build -t IMAGE_NAME .
```
Once you have build the image, move inside the `testing_environment` folder and run the container using commands:
```
cd testing_environment
docker run --rm -it -v .:/usr/app/src/ --net=host --env DISPLAY=$DISPLAY --add-host=host.docker.internal:172.17.0.1 IMAGE_NAME
```
This will create a mounted volume so all the output files will persist even after the container is deleted. The output files will be stored in the `fingerprinting_server/outputs` folder.

If you run into privileges issues, try giving `start_testing.sh` execution privileges on the local machine.

```
sudo chmod +x start_testing.sh
```
If you run into display issues, try adding *Docker* to *xhost*:
```
sudo xhost +local:docker
```

Note that currently this process is done manually right now but will be made easier using scripts once the testing is done.

### Windows host
For *Window* host, uncomment the environment variable set up in the *Dockerfile*.

```
ENV DISPLAY=host.docker.internal:0.0
```

Assuming *Docker Desktop* and a *Xserver* are running on the host, build the image using this command:
```
docker build -t IMAGE_NAME .
```
Run the container using commands:
```
cd testing_environment
docker run --rm -it -v .:/usr/app/src/ IMAGE_NAME
```