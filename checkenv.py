from stable_baselines3 import PPO
from stable_baselines3.ppo.policies import MlpPolicy
from tateti import tresEnRaya

env = tresEnRaya()
model = PPO(MlpPolicy, env, verbose=0).learn(int(50000))
