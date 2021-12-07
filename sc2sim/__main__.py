"""A module for launching StarCraft II reinforcement learning sessions."""

from sc2sim.sc2_environment import SC2Env
from sc2sim.sc2_ql_agent import QLAgent
from sc2sim.sc2_runner import SC2GameSession

def main():
    """Launch the main procedure"""
    env = SC2Env()
    agent = QLAgent()
    runner = SC2GameSession(env, agent, 20000, 1000)
    runner.run()

if __name__ == '__main__':
    main()
