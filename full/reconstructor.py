from camera import Camera
import numpy as np



class Reconstructor:

    def __init__(self):
        pass

    def triangulate(self,
                    camera1: Camera,
                    camera2: Camera,
                    point1: np.ndarray,
                    point2: np.ndarray) -> np.ndarray:
        """
        Triangulates the point from the two cameras
        :param camera1:
        :param camera2:
        :param point1: 2D point in camera1
        :param point2: 2D point in camera2
        :return: 3D point
        """
        P1 = camera1.get_camera_matrix()
        P2 = camera2.get_camera_matrix()
        # Make the points homogenous
        point1_hg = np.hstack((point1, 1))
        point2_hg = np.hstack((point2, 1))
        point3d_hg = cv2.triangulatePoints(P1, P2, point1_hg, point2_hg)

