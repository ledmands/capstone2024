from stable_baselines3 import DQN
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor
import gymnasium as gym

MODEL_NAME = "ALE-Pacman-v5-control-v1"

loaded_model = DQN.load(MODEL_NAME)

# Retrieve the environment
eval_env = Monitor(gym.make("ALE/Pacman-v5", frameskip=1, render_mode="human", repeat_action_probability=0))


# Evaluate the policy
mean_reward, std_reward = evaluate_policy(loaded_model.policy, eval_env, n_eval_episodes=1, deterministic=True)

print(f"mean_reward={mean_reward:.2f} +/- {std_reward}")
