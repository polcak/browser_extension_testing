# Integration testing
## Contents
Integration testing consists of three main parts:
- The emulation of a user visiting a site that creates users browser fingerprint. This user could be using either Google Chrome or Mozilla Firefox to access said webpage. They could have no extension or a combination of extensions installed. 
- A server implementing known techniques used to calculate users fingerprint. The server runs continuously inside the container and gathers data once the simulated client visits its webpage. This data is stored into a JSON file. 
- After relevant data is gathered by the fingerprinting server and stored in s JSON file, it is compared against the expected results.

Script `start_testing.sh` is run immediately after creating and executing the container from a Docker image. By default the server is deployed and its outputs are logged into the `server.log` file. The client is initiated using the command:
```
python3 start.py ./example_configs/client.json ./example_configs/server.json
```
The configuration files to be used can be changed. The script also executes integration testing after the data is gathered.
