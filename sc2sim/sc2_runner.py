"""A module for running a StarCraft II simulation environment
for reinforcement learning purposes."""

from dataclasses import dataclass
from typing import Protocol
from time import sleep
from sc2sim.sc2_environment import SC2Env, SC2State, SC2Action, SC2Experience

RUN_INFINITE = -1

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
    _state_displayed: bool=False

    def run(self, debug: bool=False):
        """Launch a StarCraft II training session until """
        episode = 0

        def is_debug_episode():
            return debug and episode % 1000 == 0

        while episode < self.max_episodes or self.max_episodes == RUN_INFINITE:
            episode_steps = 0
            state = self.env.reset()
            if is_debug_episode():
                self._print_state(episode, 0)
            is_terminal = False
            reward_sum = 0

            while episode_steps < self.max_steps_per_episode:
                action = self.agent.choose_action(state)
                state_after, reward = self.env.step(action)
                is_terminal = reward == 1
                exp = SC2Experience(state, action, state_after, reward - 0.01, is_terminal)
                state = state_after
                self.agent.update_model(exp)
                if is_terminal:
                    state = self.env.reset()
                if is_debug_episode():
                    self._print_state(episode, reward_sum)
                episode_steps += 1
                reward_sum += reward

            episode += 1
            if not debug:
                print(f'episode {episode} is over! rewards: {reward_sum}, steps: {episode_steps}')

    def _print_state(self, episode: int, reward_sum: int):

        def clear():
            for _ in range(self.env.world_height + 4):
                print('\033[1A', end='\x1b[2K')

        def state_as_string(state: SC2State):
            out = ''
            for row in range(0, state.world_height + 1):
                for col in range(0, state.world_width + 1):
                    if (row, col) == state.marine_pos:
                        out += 'mm'
                    elif row - state.beacon_pos[0] in [-1, 0, 1] and \
                            col - state.beacon_pos[1] in [-1, 0, 1]:
                        out += 'bb'
                    else:
                        out += '..'
                out += '\n'
            return out

        def render():
            print(f"simulating after {episode} episodes, rewards: {reward_sum}")
            print()
            print(state_as_string(self.env.state))
            sleep(0.005)

        for _ in range(4):
            if self._state_displayed:
                clear()
            self._state_displayed = True
            render()
