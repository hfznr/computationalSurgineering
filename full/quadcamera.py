import numpy as np
from typing import List
from full.camera import Camera

class QuadCamera:
    def __init__(self,
                 index: int = 0) -> None:
        self.index = 0
        self.cameras = [Camera(id=i) for i in range(4)]


    # def open_camera(self, device = 0, width = -1, height = -1):
    #     self.cap = cv2.VideoCapture(device, cv2.CAP_V4L2)
    #     self.arducam_utils = ArducamUtils(device)
    #     # turn off RGB conversion
    #     if self.arducam_utils.convert2rgb == 0:
    #         self.cap.set(cv2.CAP_PROP_CONVERT_RGB, self.arducam_utils.convert2rgb)
    #     # set width
    #     if width != -1:
    #         self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    #         # self.cap.set(6, width)
    #     # set height
    #     if height != -1:
    #         self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    #         # self.cap.set(5, height)
    #
    #     self.fix_orientation()

    def callibrate(self,
                   callibration_frames: List[np.ndarray]) -> None:
        """
        Callibrates the cameras
        :param callibration_frames:
        :return:
        """
        for camera in self.cameras:
            camera.callibrate(callibration_frames[camera.id])