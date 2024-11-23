"""A module for launching StarCraft II reinforcement learning sessions."""

import os
from sc2sim.sc2_environment import SC2Env
from sc2sim.sc2_ql_agent import QLAgent
from sc2sim.sc2_runner import SC2GameSession, RUN_INFINITE

def main():
    """Launch the main procedure"""
    env = SC2Env(world_width=32, world_height=32)
    agent = QLAgent()
    runner = SC2GameSession(env, agent, RUN_INFINITE, 1000)
    runner.run(debug=(os.environ["HEADLESS"] != "true" if "HEADLESS" in os.environ else True))

if __name__ == '__main__':
    main()
