# SC2Sim - A StarCraft II Simulation Environment

## About
This project is a StartCraftII simulation environment for move to beacon.
It is supposed to be used as a mock-up for enhancing RL training time.

## End User Setup
You can set up this package by deploying it as a pip sdist.

```sh
https://github.com/Bonifatius94/sc2sim
cd sc2sim
pip install -e .
```

## Usage
See following example to outline the suggested usage:

```py
from sc2sim.sc2_environment import SC2Env
from sc2sim.sc2_ql_agent import QLAgent
from sc2sim.sc2_runner import SC2GameSession

def main():
    env = SC2Env()
    agent = QLAgent()
    runner = SC2GameSession(env, agent, 20000, 1000)
    runner.run()
```

*Note: The simulation environment needs to be reset on initial creation.
Otherwise the marine spawns already at the beacon.*

## Development Build and CI/CD
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
