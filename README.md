# 011_reinforcement_learning

## How Do We Define Reinforcement Learning?
Reinforcement Learning is a subfield of machine learning that teaches an agent how to choose an action from its action space, within a particular environment, in order to maximize rewards over time.

## Reinforcement Learning has four essential elements:

1. **Agent**. The program you train, with the aim of doing a job you specify.
2. **Environment**. The world, real or virtual, in which the agent performs actions.
3. **Action**. A move made by the agent, which causes a status change in the environment.
4. **Rewards**. The evaluation of an action, which can be positive or negative.

# Supervised, Unsupervised, and Reinforcement Learning: What are the Differences?
## Difference #1: Static Vs.Dynamic
The goal of supervised and unsupervised learning is to search for and learn about patterns in training data, which is quite static. RL, on the other hand, is about developing a policy that tells an agent which action to choose at each step — making it more dynamic.

## Difference #2: No Explicit Right Answer
In supervised learning, the right answer is given by the training data. In Reinforcement Learning, the right answer is not explicitly given: instead, the agent needs to learn by trial and error. The only reference is the reward it gets after taking an action, which tells the agent when it is making progress or when it has failed.

## Difference #3: RL Requires Exploration
A Reinforcement Learning agent needs to find the right balance between exploring the environment, looking for new ways to get rewards, and exploiting the reward sources it has already discovered. In contrast, supervised and unsupervised learning systems take the answer directly from training data without having to explore other answers.

## Difference #4: RL is a Multiple-Decision Process
Reinforcement Learning is a multiple-decision process: it forms a decision-making chain through the time required to finish a specific job. Conversely, supervised learning is a single-decision process: one instance, one prediction.

# Example: Controlling A Walking Robot
**Agent**: The program controlling a walking robot.
**Environment**: The real world.
**Action**: One out of four moves (1) forward; (2) backward; (3) left; and (4) right.
**Reward**: Positive when it approaches the target destination; negative when it wastes time, goes in the wrong direction or falls down.

In this final example, a robot can teach itself to move more effectively by adapting its policy based on the rewards it receives.

# Markov Chain
A Markov Chain is a stochastic model describing a sequence of possible events in which the probability of each event depends only on the state attained in the previous event. When we put the Markov Property (the probability when certain event happens because some-prior event. The next event happens related with previous neighbor state) to work in a random process, we call it a Markov Chain. 

Markov Chain, which works with _S_, a set of states, and _P_, the probability of transitioning from one to the next. It also uses the Markov Property, meaning each state depends only on the one immediately prior to it.

# Markov Decision Process (MDP)
MDP is critical for RL, because MDP defines the environment (where the agent perform the task). Markov Decision Process differs from the Markov Chain in that it brings actions into play. This means the next state is related not only to the current state itself but also to the actions taken in the current state. Moreover, in MDP, some actions that correspond to a state can return rewards. In fact, **the aim of MDP** is to train an agent to find a policy that will return the maximum cumulative rewards from taking a series of actions in one or more states.

Here’s a formulated definition, which is what you’ll probably get if you google Markov Decision Process:
![image](https://github.com/astdeww/011_reinforcement_learning/assets/38376016/240f40d8-9711-4514-a125-7eb34e3574db)

## MDP in Action: Learning with Adam
We can make this even easier to grasp with a story, using Adam as our example. As we know, this hard-working young man wants to make as much money as he can. Using the framework defined above, we can help him do just that.

![image](https://github.com/astdeww/011_reinforcement_learning/assets/38376016/5b3cea72-241c-472d-8708-912ad71c8abf)
![image](https://github.com/astdeww/011_reinforcement_learning/assets/38376016/c6cdb0f4-1884-4a39-8ef3-8df6cd3a7c61)

> When Adam’s state is Tired, he can choose one of three actions: (1) continue working, (2) go to the gym, and (3) get some sleep.

If he chooses to work, he remains in the Tired state with the certainty of getting a +20 reward. if he chooses to sleep, he has 80% of moving to the next state, Energetic, and a 20% chance of staying Tired.

If he doesn’t want to sleep, he may go to the gym and do a workout. This gives him a 50% chance of entering the Energetic state and a 50% chance of staying Tired. However, he needs to pay for the gym, so this choice results in a -10 reward.

> When Adam becomes Energetic, he can go back to work and be more efficient. From there, he has an 80% chance of getting Tired again (with a +40 reward), and a 20% chance of staying Energetic (with a +30 reward).

Sometimes, when he is Energetic, he wants to do a workout. When he exercises in this state, he has a good time and gets 100% getting Healthier. Of course, he needs to pay for it with a -10 reward.

> Once he arrives at the state Healthier, there is only one thing on his mind: earn more money by doing more work. Because he is in such a good state, he works at peak efficiency, earns a +100 reward, and keeps working until he gets tired again.

With the above information, we can train an agent aimed at helping Adam find the best policy to maximize his rewards over time. This agent will undertake a Markov Decision Process.
However, before we can do that, we need to know how to compute the cumulative reward when an action is taken in one state. That is to say, we must be able to estimate the state value.
