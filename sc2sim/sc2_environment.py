"""A module implementing a 'rather fast' StarCraft II simulation
environment designed for reinforcement learning purposes"""

from dataclasses import dataclass, field
from enum import IntEnum
from typing import Tuple
import numpy as np

class SC2Action(IntEnum):
    """Representing an action where the agent walks into a single
    or a combination of the 4 canonical directions top, bot, right, left"""
    TOP_LEFT = 0
    TOP = 1
    TOP_RIGHT = 2
    LEFT = 3
    RIGHT = 4
    BOT_LEFT = 5
    BOT = 6
    BOT_RIGHT = 7

@dataclass
class SC2State:
    """Representing a discrete state of the StarCraft II environment"""

    marine_pos: Tuple[int, int] = field(default=(0, 0))
    beacon_pos: Tuple[int, int] = field(default=(1, 1))
    world_width: int=128
    world_height: int=128

@dataclass
class SC2Experience:
    """Representing a StarCraft II experience related to a single game step"""
    state_before: SC2State
    action: SC2Action
    state_after: SC2State
    reward: int
    is_terminal: bool

@dataclass
class SC2Env:
    """Representing a StartCraft II simulation environment."""
    world_width: int = 128
    world_height: int = 128
    norm_marine_pos: Tuple[int, int] = field(default=(0, 0))
    norm_beacon_pos: Tuple[int, int] = field(default=(1, 1))

    @property
    def state(self):
        """Retrieve the environment state"""
        return SC2State(self.marine_pos, self.beacon_pos,
            self.world_width, self.world_height)

    @property
    def marine_pos(self):
        """Retrieve the marine's position"""
        return self.norm_marine_pos

    @property
    def beacon_pos(self):
        """Retrieve the beacon's position"""
        return self.norm_beacon_pos

    def step(self, action: SC2Action) -> Tuple[SC2State, float]:
        """Apply a single step to the StarCraft II simulation environment
        and return the next state and reward observed"""
        x_diff, y_diff = SC2Env._get_move_diffs(action)
        self._apply_move_diffs(x_diff, y_diff)
        return self.state, self._get_reward()

    def reset(self) -> SC2State:
        """Reset the StarCraft II simulation environment and return the new state"""
        self._spawn_beacon_randomly()
        return self.state

    @staticmethod
    def _get_move_diffs(action: SC2Action) -> Tuple[int, int]:
        # determine move directions
        move_left = action in [SC2Action.TOP_LEFT, SC2Action.LEFT, SC2Action.BOT_LEFT]
        move_right = action in [SC2Action.TOP_RIGHT, SC2Action.RIGHT, SC2Action.BOT_RIGHT]
        move_top = action in [SC2Action.TOP_LEFT, SC2Action.TOP, SC2Action.TOP_RIGHT]
        move_bot = action in [SC2Action.BOT_LEFT, SC2Action.BOT, SC2Action.BOT_RIGHT]

        # combine x / y diffs
        x_diff = -1 if move_left else (1 if move_right else 0)
        y_diff = -1 if move_bot else (1 if move_top else 0)
        return x_diff, y_diff

    def _apply_move_diffs(self, x_diff: int, y_diff: int):
        marine_x = self.norm_marine_pos[0] + x_diff
        marine_y = self.norm_marine_pos[1] + y_diff
        marine_x = max(min(marine_x, self.world_width), 0)
        marine_y = max(min(marine_y, self.world_height), 0)
        self.norm_marine_pos = (int(marine_x), int(marine_y))

    def _get_reward(self) -> float:
        return 1.0 if self._is_marine_at_target() else 0.0

    def _is_marine_at_target(self) -> bool:
        same_x = self.norm_beacon_pos[0] - self.norm_marine_pos[0] in [-1, 0, 1]
        same_y = self.norm_beacon_pos[1] - self.norm_marine_pos[1] in [-1, 0, 1]
        return same_x and same_y

    def _spawn_marine_randomly(self):
        # spawn marine randomly
        new_x = np.random.randint(0, self.world_width + 1)
        new_y = np.random.randint(0, self.world_height + 1)
        self.norm_marine_pos = (new_x, new_y)

    def _spawn_beacon_randomly(self):
        # spawn beacon randomly
        new_x = np.random.randint(1, self.world_width)
        new_y = np.random.randint(1, self.world_height)
        self.norm_beacon_pos = (new_x, new_y)

        # repeat the spawn if the marine is already in the target
        if self._is_marine_at_target():
            self._spawn_beacon_randomly()
