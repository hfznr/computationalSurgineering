import time
import cv2
import json
import os
from datetime import datetime
import argparse
from arducam_camera import MyCamera
from utils import ArducamUtils
import numpy as np
from point_detector import PointDetector


class VideoRecorder:
    def __init__(self, num_cameras, videos_directory='./scenes/', device=0, width=1920, height=1080):
        self.num_cameras = num_cameras
        self.videos_directory = videos_directory
        self.device = device
        self.width = width
        self.height = height
        self.point_detector = PointDetector()

    def write_camera_params(self, fmt, filename):
        result = json.dumps(fmt, sort_keys=True, indent=4, separators=(',', ':'))
        fName = filename.replace('.mp4', '_params.txt')
        with open(str(fName), 'w') as f:
            f.write(result)

    def parse_cmdline(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-d', '--device', default=0, type=int, nargs='?',
                            help='/dev/videoX default is 0')
        parser.add_argument('--width', type=lambda x: int(x, 0), default=-1,
                            help="set width of image")
        parser.add_argument('--height', type=lambda x: int(x, 0), default=-1,
                            help="set height of image")

        args = parser.parse_args()
        return args

    def open_camera(self):
        camera = MyCamera()
        print("Open camera...")
        camera.open_camera(self.device, self.width, self.height)
        (width, height) = camera.get_framesize()
        print(f"Current resolution: {width}x{height}")
        return camera, width, height

    def initialize_video_writers(self, fmt, scale):
        image_width = int(fmt['width'] * scale)
        image_height = int(fmt['height'] * scale)

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writers = [
            cv2.VideoWriter(self.videos_directory + f'camera_{i}_recording.mp4', fourcc, 20.0, (image_width // self.num_cameras, image_height))
            for i in range(self.num_cameras)
        ]

        return video_writers

    def capture_and_write_frames(self, camera, video_writers, image_width, image_height):
        while cv2.waitKey(1) != ord('q'):
            frame = camera.get_frame()
            frame = cv2.resize(frame, (image_width, image_height))

            # Detect red objects in the frame and get the centers
            frame_with_red_detection, red_centers = self.point_detector.detect_red_objects(frame)

            # Split the frame into four parts
            frames_split = [frame_with_red_detection[:, i * (image_width // self.num_cameras): (i + 1) * (image_width // self.num_cameras)] for i in range(self.num_cameras)]

            # Print the coordinates of the centers of red points
            for i, center in enumerate(red_centers):
                print(f"Camera {i + 1} - Red Point Coordinates: ({center[0]}, {center[1]})")

            for i in range(self.num_cameras):
                cv2.imshow(f"Arducam {i}", frames_split[i])
                video_writers[i].write(frames_split[i])  # Write the frame to the video


    def close_camera_and_release_writers(self, camera, video_writers):
        camera.close_camera()

        for writer in video_writers:
            writer.release()  # Release the video writer

        print("Close camera...")

    def main(self):
        args = self.parse_cmdline()

        try:
            camera, width, height = self.open_camera()

            fmt = {
                'device': args.device,
                'width': width,
                'height': height,
            }

            scale = 1280.0 / fmt['width']
            fmt['scale'] = scale

            video_writers = self.initialize_video_writers(fmt, scale)

            self.capture_and_write_frames(camera, video_writers, int(fmt['width'] * scale), int(fmt['height'] * scale))

            self.close_camera_and_release_writers(camera, video_writers)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    recorder = VideoRecorder(num_cameras=4)  # Adjust the number of cameras as needed
    recorder.main()