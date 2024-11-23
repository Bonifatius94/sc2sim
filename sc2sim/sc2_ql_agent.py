"""A module containing a simple QL agent implementation for
playing the StarCraft II MoveToBeacon game"""

from typing import Dict, Tuple
from dataclasses import dataclass, field
from math import atan2, pi
import numpy as np
from sc2sim.sc2_environment import SC2State, SC2Experience, SC2Action

@dataclass
class QLAgent:
    """Representing a QL agent for playing the StarCraft II MoveToBeacon game"""
    alpha: float=0.01
    start_epsilon: float=1.0
    min_epsilon: float=0.1
    epsilon_decay_steps=500*500
    gamma: float=0.99
    model: Dict[int, np.ndarray] = field(default_factory=dict)
    action_space: int=8
    step: int=0

    def choose_action(self, state: SC2State) -> SC2Action:
        """Select an action based on the given environment state"""
        self.step += 1
        enc_state = QLAgent._encode_state(state)
        if not enc_state in self.model:
            self._init_state(enc_state)
        q_values = self.model[enc_state]
        best_action = np.argmax(q_values)
        explore = np.random.uniform() < self.epsilon
        return np.random.randint(self.action_space) if explore else best_action

    def update_model(self, exp: SC2Experience):
        """Train the model given the experience of a single step"""
        enc_state_before = QLAgent._encode_state(exp.state_before)
        enc_state_after = QLAgent._encode_state(exp.state_after)
        if not enc_state_after in self.model:
            self._init_state(enc_state_after)
        q_0 = self.model[enc_state_before][exp.action]
        q_1 = np.max(self.model[enc_state_after])
        q_est = 0.0 if exp.is_terminal else self.gamma * q_1
        q_new = q_0 + self.alpha * (exp.reward + q_est - q_0)
        self.model[enc_state_before][exp.action] = q_new

    @property
    def epsilon(self):
        """Retrieve the step's exploration rate (epsilon)"""
        return max(0, (self.start_epsilon - self.min_epsilon) * \
            (1 - self.step / self.epsilon_decay_steps)) + self.min_epsilon

    @staticmethod
    def _encode_state(state: SC2State) -> int:

        def state_as_vector(state: SC2State) -> Tuple[float, float]:
            dx = state.beacon_pos[0] - state.marine_pos[0]
            dy = state.beacon_pos[1] - state.marine_pos[1]
            return dx, dy

        def direction_of_vector_in_rad(vec: Tuple[float, float]) -> float:
            return atan2(vec[1], vec[0]) + pi

        def discretize_angle(angle_rad: float, num_sectors: int) -> int:
            return int(angle_rad / (2*pi) * num_sectors) % num_sectors

        return discretize_angle(
            direction_of_vector_in_rad(state_as_vector(state)),
            num_sectors=32
        )

    def _init_state(self, state: Tuple[int, int]):
        self.model[state] = np.random.uniform(size=self.action_space)
