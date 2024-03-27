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

- **SurgicalToolDetection:** 
- **separated_files:** 
- **Calibration using matlab:** To get better calibration result matlab is used. Please check: https://github.com/arnaucr24/Surgical_Instrument_Tracking_CS
- **separated_files:** 

#### How does it work ?



* Instanciate the cameras and start the recording, and the video capturers
* Calibrate for intrinsic and extrinsic parameters
* Instanciate the detector of the instrument `src/detector_red.py`
* Instanciate the reconstructor `src/reconstructor.py`
* Detect and reconstruct to get the points in 3d

To run :
`python run.py`


### Prerequisites

Before you begin, ensure you have met the following requirements:



### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hfznr/computationalSurgineering.git
