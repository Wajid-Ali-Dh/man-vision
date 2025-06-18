def make_decision(defect_scores, sensor_data, threshold=0.5):
    """
    Determines the system action based on defect detection scores and sensor data.

    Args:
        defect_scores (list or np.ndarray): Confidence scores for detected defects.
        sensor_data (dict): Dictionary containing sensor readings (e.g., 'encoder').
        threshold (float): Confidence threshold for defect detection.

    Returns:
        str: System status, one of 'RUNNING', 'PAUSE', or 'CORRECT'.
    """
    if any(score > threshold for score in defect_scores):
        if sensor_data['encoder'] % 2 == 0:
            return 'PAUSE'
        else:
            return 'CORRECT'
    return 'RUNNING'
