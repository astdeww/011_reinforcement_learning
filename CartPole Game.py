import gym
env = gym.make("CartPole-v1")  # creates a CartPole environment
observation = env.reset()  # initializes the status parameters
for _ in range(1000):
    env.render()  # shows the game
action = env.action_space.sample()  # your agent here (this takes random actions) -> prompts an action with a policy that is ‘random’
observation, reward, done, info = env.step(action)  # the action is taken and the environment gives four returns
if done:  # if the game is done; restart it
    observation = env.reset()
env.close()

"""
  *  Observation: Parameters of the game status. Different games return different parameters. In CartPole, there are four in total. The second parameter is the angle of the pole.
  *  Reward: The score you get after taking this action.
  *  Done: Game over or not over.
  *  Info: Extra debug information. It could be cheating.
"""
