import numpy as np
from collections import defaultdict
import copy
from state import UltimateTTT_Move
from state import State, State_2

class MonteCarloTreeSearchNode():
    def __init__(self, state, parent=None, parent_action=None):
        self.state = state
        self.parent = parent
        self.parent_action = parent_action
        self.children = []
        self._number_of_visits = 0
        self._results = defaultdict(int)
        self._results[1] = 0
        self._results[-1] = 0
        self._untried_actions = None
        self._untried_actions = self.untried_actions()
        return

    def untried_actions(self):
        self._untried_actions = self.state.get_valid_moves
        return self._untried_actions
    
    def q(self):
        wins = self._results[1]
        loses = self._results[-1]
        return wins - loses
    
    def n(self):
        return self._number_of_visits
    
    def expand(self):
        action = self._untried_actions.pop()
        next_state = act_move_v2(self.state, action)
        child_node = MonteCarloTreeSearchNode(next_state, parent=self, parent_action=action)
        self.children.append(child_node)
        return child_node 
    
    def is_terminal_node(self):
        return self.state.game_over
    
    def rollout(self):
        current_rollout_state = copy.deepcopy(self.state)
        while not current_rollout_state.game_over:   
            possible_moves = current_rollout_state.get_valid_moves
            if len(possible_moves) == 0:
                break
            action = self.rollout_policy(possible_moves)
            current_rollout_state = act_move_v2(current_rollout_state, action)
        return current_rollout_state.game_result(current_rollout_state.global_cells.reshape(3,3))
    
    def backpropagate(self, result):
        self._number_of_visits += 1.
        self._results[result] += 1.
        if self.parent:
            self.parent.backpropagate(result)
            
    def is_fully_expanded(self):
        return len(self._untried_actions) == 0
    
    def best_child(self, c_param=0.1):
        choices_weights = [(c.q() / c.n()) + c_param * np.sqrt((2 * np.log(self.n()) / c.n())) for c in self.children]
        return self.children[np.argmax(choices_weights)]
    
    def rollout_policy(self, possible_moves):
        return possible_moves[np.random.randint(len(possible_moves))]
    
    def _tree_policy(self):
        current_node = self
        while not current_node.is_terminal_node():
            if not current_node.is_fully_expanded():
                return current_node.expand()
            else:
                if len(current_node.children) == 0:
                    break 
                current_node = current_node.best_child()
        return current_node
    
    def best_action(self):
        simulation_no = 500
        for i in range(simulation_no):
            v = self._tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        return self.best_child(c_param=1.414)

'''
    This is the move function where a new state 
    will be created. You can implement this function
    as a method of the State class. However, since I 
    am unable to modify the state.py file because of 
    the assignment requirements, I have placed the function here.
'''

def act_move_v2(state: State_2, move: UltimateTTT_Move):
    state = copy.deepcopy(state)
    if not state.is_valid_move(move):
        raise ValueError(
            "move {0} on local board is not valid".format(move)
        )
    local_board = state.blocks[move.index_local_board]
    local_board[move.x, move.y] = move.value
    
    state.player_to_move *= -1          
    state.previous_move = move
    
    if state.global_cells[move.index_local_board] == 0: # not 'X' or 'O'
        if state.game_result(local_board):
            state.global_cells[move.index_local_board] = move.value
            
    return state