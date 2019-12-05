import math


def reward_function(params):
    """
    Example of rewarding the agent to follow center line
    """

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']
    waypoints = params['waypoints']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Penalize distance from centerline
    reward = reward - distance_from_center

    # Finish Bonus
    if progress == 100:
        reward += 10000

    # Speed Threshold
    speed_threshold = 0.5
    if params['speed'] < speed_threshold:
        reward *= 0.5

    # Distance to next waypoint
    car_x = params['x']
    car_y = params['y']
    waypoint_x = waypoints[params['closest_waypoints'][1]][0]
    waypoint_y = waypoints[params['closest_waypoints'][1]][1]

    x_len = waypoint_x - car_x
    y_len = waypoint_y - car_y
    distance = x_len**2 + y_len**2
    nxt_way_distance = math.sqrt(distance)
    distance_reward = 1 - nxt_way_distance**0.05

    reward = reward * distance_reward

    return float(reward)