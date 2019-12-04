import math


def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    progress = params['progress']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # further progress down the track gets higher reward
    reward = progress

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward += 5
    elif distance_from_center <= marker_2:
        reward += 2
    elif distance_from_center <= marker_3:
        reward += 1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Penalize distance from centerline
    reward = reward - distance_from_center

    # Finish Bonus
    if progress == 100:
        reward += 10000

    # Speed Threshold
    SPEED_THRESHOLD = 0.5
    if params['speed'] < SPEED_THRESHOLD:
        reward *= 0.5

    # Distance to next waypoint
    car_x = params['x']
    car_y = params['y']
    waypoint_x = params['closest_waypoints'][0]
    waypoint_y = params['closest_waypoints'][1]

    x_len = waypoint_x - car_x
    y_len = waypoint_y - car_y
    distance = x_len**2 + y_len**2
    nxt_way_distance = math.sqrt(abs(distance))
    reward = reward - nxt_way_distance

    return float(reward)
