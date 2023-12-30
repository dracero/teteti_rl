from tateti import tresEnRaya

env = tresEnRaya()

from stable_baselines3 import PPO, A2C, DQN
from stable_baselines3.common.env_util import make_vec_env

# Instantiate the env
vec_env = make_vec_env(tresEnRaya, n_envs=1)

# Train the agent
model = PPO("MlpPolicy", env, verbose=1).learn(5000)

# Test the trained agent
# using the vecenv
obs = vec_env.reset()
vec_env = tresEnRaya('human')
n_steps = 20
for step in range(n_steps):
    action, _ = model.predict(obs, deterministic=True)
    print(f"Step {step + 1}")
    print("Action: ", action)
    obs, reward, terminated, truncated, info = vec_env.step(action)
    print("obs=", obs, "reward=", reward, "done=", terminated)
    vec_env.render()
    if terminated:
        # Note that the VecEnv resets automatically
        # when a done signal is encountered
        print("Goal reached!", "reward=", reward)
        break
