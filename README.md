## Introduction

Computational Surgineering is designed to bridge the gap between computational techniques and practical surgical applications.
This project aims to provide tools, libraries, and frameworks to assist in the real time surgical tool detection with mobile application. Our goal is to enhance the precision, safety, and outcomes of surgical interventions through the integration of computational methods.

In this project main goal is to show real time position of surgical tool using quadcam(arducam) that is connected to jetson Nano board.

## Features
- **Calibration Matrix Finder:** First extrinsic and intricsic parameters are found.
- **Red and Green Color:** Color detection to detect the tool position.
- **3D point Detection:** Frameworks for simulating surgical interventions and predicting outcomes.
- **Network Connection:** TCP Connection in local network. It can be connected from local devices in network. Just be sure that port 5555 is not used for other purposes.
- **3D Location Simulation:** Analytical tools for post-operative outcomes and procedural optimizations.
  

## Getting Started

- **SurgicalToolDetection:** This is the iOS application that shows real time location of detected surgical tool.
- **separated_files:** This folder has initial developments that contains main functions used in the project. You can reach each function seperately.
  For example:
  - camera calibraion functions(new_calibration.py),
  - calibration results(stereo_calibration_data.npy/txt),
  - point detector(point_detector.py),
  - real time triangulation and plotter (real_time_3d_plotter.py),
  - video recorder,
  - example tcp code, etc
- **Calibration using matlab:** To get better calibration result matlab is used. Please check: https://github.com/arnaucr24/Surgical_Instrument_Tracking_CS
- **surgical-tracking-last-version:** This folder contains latest version of the code with oop version. Also this part contains bundle adjustment, latest matlab calibration results, and tcp connection. You can check: https://github.com/ouazzmoh/surgical-tracking

#### How does it work ?

* Runs main part and tcp part as subprogram. So that they can work parallel.
Main Part
* Instanciate the cameras and start the recording, and the video capturers
* Calibrate for intrinsic and extrinsic parameters
* Instanciate the detector of the instrument `src/detector_red.py`
* Instanciate the reconstructor `src/reconstructor.py`
* Detect and reconstruct to get the points in 3d
* Saves 3d coordinates in mean_points.txt
TCP Part
* Reads 3d points from mean_points.txt
* Send 3d position using tcp.
* All local devices can connect and listen 3d position from device using ip:192.168.0.57 and port:5555

To run :
`python run.py`


### Prerequisites

Before you begin, ensure you have met the following requirements:
For application: XCode ide. 
For hardware: Jetson Nano board, Quadcam(Arducam), jetson nano kernel, imx477 driver.
        Check this links: 
        - https://developer.nvidia.com/embedded/downloads/archive
        - https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write
        - https://docs.arducam.com/Nvidia-Jetson-Camera/Multi-Camera-CamArray/quick-start/


### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hfznr/computationalSurgineering.git
