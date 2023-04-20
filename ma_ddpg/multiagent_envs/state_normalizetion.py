import numpy as np


class StateNormalization(object):
    def __init__(self):
        pass

    def state_normal(self, state):
        self.high_state = []
        if len(state) == 4:
            self.high_state = np.append(self.high_state, [100, 100, 100])
            self.high_state = np.append(self.high_state, 500000)
            self.low_state = np.zeros(4)  # state 包括：uav的坐标，uav的能量
        elif len(state) == 2:
            self.high_state = np.append(self.high_state, 1e7)
            self.high_state = np.append(self.high_state, 1e3)
            self.low_state = np.zeros(2)  # state 包括：ue的需求（data_size/cpu_task）

        return state / (self.high_state - self.low_state)
