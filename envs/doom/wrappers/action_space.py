import gym
from gym.spaces import Discrete, Box

from algorithms.spaces.discretized import Discretized


def doom_action_space():
    """
    Standard action space for full-featured Doom environments (e.g. deathmatch).
    TODO: crouch?
    TODO: strafe?

    This should precisely correspond to the available_buttons configuration in the .cfg file.
    This function assumes:
        MOVE_FORWARD
        MOVE_BACKWARD
        MOVE_RIGHT
        MOVE_LEFT
        SELECT_NEXT_WEAPON
        SELECT_PREV_WEAPON
        ATTACK
        SPEED
        TURN_LEFT_RIGHT_DELTA
    """
    return gym.spaces.Tuple((
        Discrete(3),  # noop, forward, backward
        Discrete(3),  # noop, move right, move left
        Discrete(3),  # noop, prev_weapon, next_weapon
        Discrete(2),  # noop, attack
        Discrete(2),  # noop, sprint
        Box(-1.0, 1.0, (1, )),
    ))


def doom_action_space_hybrid():
    return gym.spaces.Tuple((
        Discrete(3),  # noop, forward, backward
        Discrete(3),  # noop, move right, move left
        Discrete(3),  # noop, prev_weapon, next_weapon
        Discrete(2),  # noop, attack
        Discrete(2),  # noop, sprint
        Discretized(11, min_action=-10.0, max_action=10.0),  # turning using discretized continuous control
    ))


def doom_action_space_hybrid_no_weap():
    return gym.spaces.Tuple((
        Discrete(3),  # noop, forward, backward
        Discrete(3),  # noop, move right, move left
        Discrete(2),  # noop, attack
        Discrete(2),  # noop, sprint
        Discretized(11, min_action=-10.0, max_action=10.0),  # turning using discretized continuous control
    ))


def doom_action_space_no_weap():
    return gym.spaces.Tuple((
        Discrete(3),  # noop, forward, backward
        Discrete(3),  # noop, move right, move left
        Discrete(2),  # noop, attack
        Discrete(2),  # noop, sprint
        Box(-1.0, 1.0, (1, )),
    ))


def doom_action_space_discrete():
    return gym.spaces.Tuple((
        Discrete(3),  # noop, forward, backward
        Discrete(3),  # noop, move right, move left
        Discrete(3),  # noop, turn right, turn left
        Discrete(3),  # noop, prev_weapon, next_weapon
        Discrete(2),  # noop, attack
        Discrete(2),  # noop, sprint
    ))


def doom_action_space_discrete_no_weap():
    return gym.spaces.Tuple((
        Discrete(3),  # noop, forward, backward
        Discrete(3),  # noop, move right, move left
        Discrete(3),  # noop, turn right, turn left
        Discrete(2),  # noop, attack
        Discrete(2),  # noop, sprint
    ))


def doom_action_space_experimental():
    """
        MOVE_FORWARD
        MOVE_BACKWARD
        MOVE_RIGHT
        MOVE_LEFT
        SELECT_WEAPON1
        SELECT_WEAPON2
        SELECT_WEAPON3
        SELECT_WEAPON4
        SELECT_WEAPON5
        SELECT_WEAPON6
        SELECT_WEAPON7
        ATTACK
        SPEED
        TURN_LEFT_RIGHT_DELTA
    """
    return gym.spaces.Tuple((
        Discrete(3),  # noop, forward, backward
        Discrete(3),  # noop, move right, move left
        Discrete(8),  # noop, select weapons 1-7
        Discrete(2),  # noop, attack
        Discrete(2),  # noop, sprint
        Discretized(21, min_action=-12.5, max_action=12.5),  # turning using discretized continuous control
    ))
