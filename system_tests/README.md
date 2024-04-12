# System tests
The system tests are based on two kinds of analysis:
- Analysing screenshots made by the driver while no extensions and combinations of extensions are installed. Analysis is done based on captured pixels.
- Analyzing log files supplied by the browser. Log data is gathered while browsing using no installed extensions and while browsing with combinations of extensions installed.

This mechanism is based on the original integration tests implemented in thesis [Automatic testing of JavaScript Restrictor project](https://www.vut.cz/studenti/zav-prace/detail/129897). 

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
This will create a mounted volume so all the output files will persist even after the container is deleted. The output files will be stored in the `data` folder.

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
docker run --rm -it -v --net=host .:/usr/app/src/ IMAGE_NAME