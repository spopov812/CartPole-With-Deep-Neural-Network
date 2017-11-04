from Model import build_model
from CartPoleTrain import get_training_data
from matplotlib import pyplot as plt
import numpy as np
import gym


env = gym.make("CartPole-v0")

x_data, y_data = get_training_data()

model = build_model()
history = model.fit(x_data, y_data, epochs=100)

plt.plot(history.history['binary_accuracy'])
plt.plot(history.history['mean_squared_error'])

plt.show()

num_games_to_run = 100

scores = []

for game in range(num_games_to_run):

    observation = env.reset()
    score = 0
    done = False

    while not done:

        action = model.predict(observation.reshape(1, 4))

        if action >= .5:
            action = 1
        else:
            action = 0

        env.render()

        observation, reward, done, info = env.step(action)

        score += reward

    scores.append(score)

scores = np.array(scores)

print("Total score achieved after 100 simulations- ", scores.sum())

print("Max score achieved- ", np.max(scores))

print("Mean score- ", np.mean(scores))

print("Median score- ", np.median(scores))
