
import numpy as np


class Board:
    def __init__(self, fname):
        self.board = self.get_board_from_file(fname)
        self.height, self.width = self.board.shape
        print(self.height, self.width)

        # Game params
        self.cur_state = np.array([0, 0])
        self.end_state = np.array([self.height, self.width])
        self.invalid_move_penalty = 10
        self.win_reward = -100

    @staticmethod
    def get_board_from_file(fname):
        board = []
        for line in open(fname).readlines():
            board.append([int(n) for n in line.strip()])
        return np.array(board, dtype=np.int16)

    def is_action_valid(self, dx, dy):
        x = self.cur_state[0] + dx
        y = self.cur_state[1] + dy

        return 0 <= x < self.height and 0 <= y <= self.width

    def map_action_to_pos(self, action):
        action_map = {k: np.array(v) for k, v in {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}.items()}

        return action_map[action]

    def is_end_state(self):
        return self.cur_state == self.end_state

    def step(self, action):
        dx, dy = self.map_action_to_pos(action)
        done = False

        if not self.is_action_valid(dx, dy):
            return self.cur_state, self.invalid_move_penalty, done, self.cur_state

        else:
            self.cur_state = self.cur_state + [dx, dy]

            if self.is_end_state():
                penalty = self.win_reward
                done = True
            penalty = self.board[self.cur_state]
