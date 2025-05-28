# Vehicle Counting in Parking Lot

This project implements a real-time vehicle counting system using deep learning and computer vision techniques. It automatically identifies vacant and occupied parking slots from video feeds using a Convolutional Neural Network (CNN).

## Project Overview

Urban parking management is challenging due to limited space and high traffic. This system helps monitor parking lot occupancy in real-time, aiding in efficient space utilization and traffic management.

## Demo

You can download and watch the demo video here:
[Watch the video](https://youtu.be/8sRWZXne7ug)

## Approach

- **Data Collection**: Images of parking lots were collected and labeled to indicate occupied and vacant slots.
- **Model Training**: A CNN was trained on the labeled dataset to classify parking slots.
- **Real-Time Detection**: The trained model processes video feeds to detect and count vehicles in each parking slot.

## Technologies Used

- Python
- OpenCV
- TensorFlow/Keras
- NumPy

## Getting Started

### Prerequisites

- Python 3.x
- pip

### Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/sruthi7sri/Vehicle-Counting-in-Parking-Lot.git
   cd Vehicle-Counting-in-Parking-Lot
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the main script:
   ```bash
   python main.py
   ```
4. The system will process the video feed and display the parking lot with occupied and vacant slots marked.

## Project Structure
- Car Parking System Using Deep Learning.ipynb: Jupyter notebook detailing the project.
- main.py: Main script to run the vehicle counting system.
- datacollection.py: Script for collecting and labeling data.
- train_data.zip: Contains the training dataset.
- templates.zip: Contains template images for detection.
- car_test2.mp4: Sample video for testing.

## Project Goals
- Automate Parking Lot Monitoring: Detect and count vehicles in parking spaces using video surveillance and deep learning.
- Enhance Smart City Infrastructure: Integrate with smart systems for traffic control and real-time parking management.
- Improve Resource Utilization: Provide real-time feedback on parking slot availability to reduce time spent searching for parking.
- Build a Scalable Framework: Develop a reusable and scalable system adaptable to various parking lot layouts and camera feeds.

## Collaborators

- Sruthisri Venkateswaran  
- Saroja Vuluvabeeti
- Sri Sakthi

© 2025 Sruthisri Venkateswaran, Saroja Vuluvabeeti and Sri Sakthi. All rights reserved.


