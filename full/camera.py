import numpy as np
from typing import List

class Camera:
    def __init__(self,
                 id : int,
                 K : np.ndarray = None,
                 R : np.ndarray = None,
                 T : np.ndarray = None,
                 callibration_frame: np.ndarray = None,
                 currrent_frame : np.ndarray = None) -> None:
        self.id = id
        self.K = K
        self.R = R
        self.T = T
        self.callibration_frame = callibration_frame
        self.current_frame = currrent_frame

    def get_camera_matrix(self) -> np.ndarray:
        # TODO : Check and debug with this
        return self.K @ np.hstack((self.R, self.T))

    def callibrate(self,
                   callibration_frame: np.ndarray) -> None:
        """
        Callibrates the camera using the callibration_frame
        :return:
        """
        # TODO : Check if it is more optimal to store the callibration picture or keep it as a parameter
        pass

