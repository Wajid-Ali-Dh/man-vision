import numpy as np

def get_sensor_data():
    # Simulate IMU/encoder data (random walk)
    imu = np.random.normal(0, 0.1, 3)  # x, y, z accel
    encoder = np.random.randint(0, 100)
    return {'imu': imu, 'encoder': encoder}
