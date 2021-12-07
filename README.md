# SC2Sim - A StarCraft II Simulation Environment

## About
This project is a StartCraftII simulation environment for move to beacon.
It is supposed to be used as a mock-up for enhancing RL training time.

## Usage
All build + test scripting is abstracted by a Dockerfile.
For creating the Docker image run following command:

```sh
docker build . -t "sc2-sim"
```

Now, spin up the dockerized Python app you've just built:

```sh
docker run "sc2-sim"
```

## License
This software is available under the MIT licence's terms.
