# System tests
The system tests are based on two kinds of analysis:
- Analysing screenshots made by the driver while no extensions and combinations of extensions are installed. Analysis is done based on captured pixels.
- Analyzing log files supplied by the browser. Log data is gathered while browsing using no installed extensions and while browsing with combinations of extensions installed.

This mechanism is based on the original integration tests implemented in thesis [Automatic testing of JavaScript Restrictor project](https://www.vut.cz/studenti/zav-prace/detail/129897). 

## How to build the image and run the container
### Linux based host
In order to run the testing you must have `docker engine` installed, NOT `Docker Desktop`. This is due to how it handles display forwarding.

Once you have build the image in the previous folder, move inside this folder and run the container using commands:
```
docker run --rm -it -v .:/usr/app/src/ --net=host --env DISPLAY=$DISPLAY --add-host=host.docker.internal:172.17.0.1 testing_system
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


### Windows host

Assuming *Docker Desktop* and a *Xserver* are running on the host, run the container using command:

```
cd testing_environment
docker run --rm -it --net=host --env DISPLAY=host.docker.internal:0.0 -v .:/usr/app/src/ testing_system
```