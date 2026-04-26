# Gesture-Based Robot Control with Confirmation and Cancellation Mechanism

## Overview
This project presents a gesture-based robot control system using real-time webcam input. The system allows users to control a robot using simple hand gestures in an intuitive and safe manner. It focuses on improving Human-Robot Interaction by making control more natural and user-friendly.

## Key Features
- Real-time hand gesture detection using webcam  
- Finger counting for command input  
- Confirmation mechanism using right-hand fist  
- Cancellation mechanism using open palm  
- Stability and cooldown to reduce false triggering  
- Pre-recorded robot operations for execution  

## System Workflow
1. Webcam captures live video input  
2. System detects hand and counts fingers  
3. Gesture is mapped to a predefined robot command  
4. System waits for confirmation gesture  
5. Robot executes the action after confirmation  

## HRI Concept
This system follows the Human-Robot Interaction loop:
- Perception → Webcam detects hand  
- Intention Recognition → Gesture interpretation  
- Decision Making → Confirm or cancel  
- Action → Robot execution  
- Feedback → Visual output to user  

## Technologies Used
- Python  
- Webcam  
- Computer Vision (Hand Tracking)  
- HRI Simulation Environment  

## Implementation Details
The system is implemented using Python in a simulation environment. It processes webcam frames in real time to detect gestures and trigger robot operations. A rule-based approach is used for mapping gestures to actions. Stability and cooldown mechanisms are applied to improve accuracy and prevent repeated triggering.

## Results
- Accurate gesture detection under normal lighting conditions  
- Smooth and real-time robot response  
- Reduced false triggering due to confirmation mechanism  
- Reliable interaction between user and robot  

## Limitations
- Performance depends on lighting conditions  
- Limited number of gestures supported  
- Accuracy may reduce if hands are not clearly visible  

## Future Improvements
- Use machine learning for advanced gesture recognition  
- Improve performance in low lighting conditions  
- Add support for more gestures  
- Deploy the system on a real robotic arm  

## Project Demo
This project demonstrates a complete Human-Robot Interaction system using gesture-based control with confirmation and cancellation mechanisms.

## Author
Kaushik Roshan Elangovan
