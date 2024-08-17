# Hyperloop Project

![Screenshot 2024-08-17 at 21 53 49](https://github.com/user-attachments/assets/4b38f6fa-aced-4fda-89d6-ca4fe2a4274a)
![Screenshot 2024-08-17 at 21 54 06](https://github.com/user-attachments/assets/58f95f36-507a-496d-b902-53eb0790f4d2)


Welcome to my Hyperloop project repository! This project encompasses various components and functionalities implemented for the Hyperloop competition. Below is a summary of what is included in this repository:

## Project Overview

This repository contains the complete implementation of my Hyperloop project, including:

### 1. GUI Frontend and Backend Design

- **Frontend**: The user interface design for the project, created to visualize and interact with the data.
- **Backend**: The backend code handling the logic, data processing, and communication between different components.

### 2. Raspberry Pi Functionalities

- **TCP for Braking Control**: Code to control the braking system via TCP protocol.
- **UDP for Data Transmission**: Code to send data to the interface using UDP protocol.
- **Sensor Data Reading**: Code to read data from MLX90614 (temperature sensor) and MPU6050 (gyroscope/accelerometer) sensors.

### 3. Arduino Functionalities

- **IR Sensor Data Reading**: Code to read data from the IR sensor.
- **Power Data Reading**: Code to read power data from the ACS724 sensor and send it to the Raspberry Pi via I2C protocol.

### 4. Additional Code

- **Random Data for Interface Demonstration**: Sample code with random data to showcase how the interface looks and functions.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/zeysnepk/Hyperloop_Communication.git

2. **Install Dependencies**

   Ensure you have the necessary libraries and dependencies installed for both the frontend and backend components.
   
3. **Setup Raspberry Pi**

  - Configure the Raspberry Pi for TCP and UDP communication.
  - Connect and configure the MLX90614 and MPU6050 sensors.
  - Upload the Arduino code for the IR sensor and ACS724 sensor.

4. **Run the Application**

  - Start the backend server.
  - Launch the GUI frontend.
  - Verify the communication and data handling between the Raspberry Pi and the interface.

## Files Included

- **GUI Frontend and Backend**: Includes all code and resources for the graphical user interface and backend logic.
- **Raspberry Pi Code**: Includes scripts for TCP control, UDP data transmission, and sensor reading.
- **Arduino Code**: Includes sketches for IR sensor and ACS724 power data reading.
- **Random Data Demonstration Code**: Provides sample data to illustrate the interface.

Feel free to explore the code, provide feedback, or contribute to the project!
