import numpy as np
from MCTS import MonteCarloTreeSearchNode

def select_move(cur_state, remain_time):
    root = MonteCarloTreeSearchNode(state = cur_state)
    selected_node = root.best_action()
    return selected_node.parent_action
