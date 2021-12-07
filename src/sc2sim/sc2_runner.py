"""A module for running a StarCraft II simulation environment
for reinforcement learning purposes."""

from dataclasses import dataclass
from typing import Protocol
from sc2sim.sc2_environment import SC2Env, SC2State, SC2Action, SC2Experience

class SC2Agent(Protocol):
    """Representing a StarCraft II agent for playing the MoveToBeacon game"""
    def choose_action(self, state: SC2State) -> SC2Action:
        """Select an action based on the given environment state"""
        raise NotImplementedError()

    def update_model(self, exp: SC2Experience):
        """Train the model given the experience of a single step"""
        raise NotImplementedError()

@dataclass
class SC2GameSession:
    """Representing a StarCraft II game session for training agents by reinforcement techniques"""
    env: SC2Env
    agent: SC2Agent
    max_episodes: int
    max_steps_per_episode: int

    def run(self):
        """Launch a StarCraft II training session until """
        episode = 0

        while episode < self.max_episodes:
            episode_steps = 0
            self.env.reset()
            is_terminal = False
            reward_sum = 0

            while episode_steps < self.max_steps_per_episode:
                state = self.env.state
                action = self.agent.choose_action(state)
                state_after, reward = self.env.step(action)
                is_terminal = reward == 1
                self.agent.update_model(SC2Experience(
                    state, action, state_after, reward, is_terminal))
                if is_terminal:
                    self.env.reset()
                episode_steps += 1
                reward_sum += reward

            episode += 1
            print(f'episode {episode} is over! rewards: {reward_sum}, steps: {episode_steps}')
