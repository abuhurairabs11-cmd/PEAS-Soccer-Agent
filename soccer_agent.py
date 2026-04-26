import random

class SoccerAgent:
    def __init__(self, team_id, player_id):
        self.team_id = team_id
        self.player_id = player_id
        self.position = {'x': 0, 'y': 0} # Example initial position
        self.has_ball = False

    def sense(self, environment_state):
        """ 
        Senses the current state of the environment. 
        This would involve processing information from sensors like vision, proprioception, and game state.
        
        Args:
            environment_state (dict): A dictionary containing information about the game state,
                                      e.g., ball position, other player positions, score, time.
        
        Returns:
            dict: A processed understanding of the environment relevant for decision-making.
        """
        print(f"Agent {self.team_id}-{self.player_id} sensing environment...")
        # In a real scenario, this would parse environment_state and extract relevant features.
        ball_pos = environment_state.get('ball_position', 'unknown')
        my_pos = self.position
        return {
            'ball_position': ball_pos,
            'my_position': my_pos,
            'has_ball': self.has_ball,
            'score': environment_state.get('score', {'team1': 0, 'team2': 0})
        }

    def decide_action(self, sensed_data):
        """
        Based on sensed data, decides the next action to take.
        This is where the 'brain' of the agent would be, implementing game strategy.
        
        Args:
            sensed_data (dict): The processed environment data from the `sense` method.
            
        Returns:
            dict: The chosen action, e.g., {'action': 'move', 'direction': 'forward'},
                  or {'action': 'kick', 'target': 'goal', 'power': 0.8}.
        """
        print(f"Agent {self.team_id}-{self.player_id} deciding action...")
        if sensed_data['has_ball']:
            # Simple logic: if has ball, try to score or pass
            if random.random() < 0.7: # 70% chance to try kicking
                return {'action': 'kick', 'target': 'opponent_goal', 'power': random.uniform(0.5, 1.0)}
            else:
                return {'action': 'pass', 'target': 'teammate', 'strength': random.uniform(0.3, 0.7)}
        else:
            # Simple logic: if no ball, move towards ball or open space
            if random.random() < 0.5:
                return {'action': 'move', 'direction': 'towards_ball', 'speed': random.uniform(0.1, 0.5)}
            else:
                return {'action': 'move', 'direction': 'find_open_space', 'speed': random.uniform(0.1, 0.5)}

    def act(self, action):
        """
        Executes the chosen action in the environment.
        This maps the decided action to physical actuator commands.
        
        Args:
            action (dict): The action decided by `decide_action`.
        
        Returns:
            str: A description of the executed action.
        """
        action_type = action.get('action')
        if action_type == 'move':
            direction = action.get('direction', 'unknown')
            speed = action.get('speed', 0)
            print(f"Agent {self.team_id}-{self.player_id} moving {direction} with speed {speed:.2f}.")
            # Update agent's position based on movement
            # self.position['x'] += ...
            # self.position['y'] += ...
            return f"Moved {direction}"
        elif action_type == 'kick':
            target = action.get('target', 'unknown')
            power = action.get('power', 0)
            print(f"Agent {self.team_id}-{self.player_id} kicking towards {target} with power {power:.2f}.")
            self.has_ball = False # Ball is no longer with the agent after kicking
            return f"Kicked towards {target}"
        elif action_type == 'pass':
            target = action.get('target', 'unknown')
            strength = action.get('strength', 0)
            print(f"Agent {self.team_id}-{self.player_id} passing to {target} with strength {strength:.2f}.")
            self.has_ball = False
            return f"Passed to {target}"
        else:
            print(f"Agent {self.team_id}-{self.player_id} performed unknown action: {action_type}.")
            return "Unknown action"

# Example Usage:
# Create an agent
player1 = SoccerAgent(team_id=1, player_id=7)

# Simulate an environment state
env_state = {
    'ball_position': {'x': 10, 'y': 20},
    'player_positions': {
        'team1': [{'id': 7, 'x': 5, 'y': 15, 'has_ball': True}, {'id': 10, 'x': 30, 'y': 40}],
        'team2': [{'id': 1, 'x': 50, 'y': 60}]
    },
    'score': {'team1': 0, 'team2': 0},
    'game_time': 600 # seconds remaining
}

# Update player1's state for simulation
player1.position = {'x': 5, 'y': 15}
player1.has_ball = True

# Agent senses the environment
sensed_info = player1.sense(env_state)
print(f"Sensed Info: {sensed_info}")

# Agent decides an action
chosen_action = player1.decide_action(sensed_info)
print(f"Chosen Action: {chosen_action}")

# Agent acts upon the environment
result = player1.act(chosen_action)
print(f"Action Result: {result}")

print("\n--- Simulating another turn (without ball) ---")
player1.has_ball = False # Ball passed/kicked away
env_state['ball_position'] = {'x': 15, 'y': 25} # Ball moved elsewhere

sensed_info_noball = player1.sense(env_state)
print(f"Sensed Info (no ball): {sensed_info_noball}")

chosen_action_noball = player1.decide_action(sensed_info_noball)
print(f"Chosen Action (no ball): {chosen_action_noball}")

result_noball = player1.act(chosen_action_noball)
print(f"Action Result (no ball): {result_noball}")
