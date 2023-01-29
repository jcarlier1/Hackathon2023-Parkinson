import pyautogui
from pykalman import KalmanFilter

# Initialize the Kalman filter
kf = KalmanFilter(transition_matrices=[[1, 1], [0, 1]], observation_matrices=[[1, 0]], initial_state_mean=[0, 0], initial_state_covariance=[[0, 0], [0, 0]])

def stabilize_mouse():
    # Get the current mouse coordinates
    x, y = pyautogui.position()

    # Smooth the mouse coordinates using the Kalman filter
    (smoothed_x, smoothed_y), _ = kf.filter_update([x, y])

    # Set the mouse position to the smoothed coordinates
    pyautogui.moveTo(smoothed_x, smoothed_y, duration=0.1)

while True:
    stabilize_mouse()
