import random

class SoccerAgent:
    def __init__(self):
        self.ball_distance = random.randint(1, 10)

    def sense(self):
        print("Ball distance:", self.ball_distance)

    def decide(self):
        if self.ball_distance <= 2:
            return "kick"
        else:
            return "move"

    def act(self, action):
        if action == "kick":
            print("Agent kicks the ball towards goal ⚽")
        else:
            print("Agent moves towards the ball 🏃")

agent = SoccerAgent()

agent.sense()
action = agent.decide()
agent.act(action)
