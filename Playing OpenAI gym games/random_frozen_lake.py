import gym
from gym.envs.registration import register
import msvcrt

# MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

def getkey():
    keyInput=msvcrt.getch().decode('utf-8').lower()
    if keyInput=='a':
        return LEFT
    elif keyInput=='s':
        return DOWN
    elif keyInput=='d':
        return RIGHT
    elif keyInput=='w':
        return UP
    else:
        return -1


# Register FrozenLake with is_slippery False
register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False}
)

env=gym.make('FrozenLake-v3')
#env=gym.logger.set_level(40)
env.render()  # Show the initial board

while True:
    # Choose an action from keyboard
    action = getkey()
    if action==-1:
        print("Game aborted")
        break

    action = getkey()
    state, reward, done, info = env.step(action)
    env.render()  # Show the board after action
    print("State: ", state, "Action: ", action, "Reward: ", reward, "Info: ", info)

    if done:
        print("Finished with reward", reward)
        break