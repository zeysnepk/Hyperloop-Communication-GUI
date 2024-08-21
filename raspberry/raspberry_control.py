import smbus
import time
import struct
import socket
from mpu6050 import MPU6050
from mlx90614 import MLX90614
import json
import threading
import Motor

UDP_IP = "pc_ip" #IP address of the remote control computer
UDP_PORT = 6666 #UDP port of the remote control computer

TCP_IP = "raspberry_ip" #IP address of the Raspberry Pi 4
TCP_PORT = 3333 #TCP port of the Raspberry Pi 4

I2C_ADDRESS = 0x08 #I2C address of the Arduino board

bus = smbus.SMBus(1)  #Create I2C bus instance

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Create UDP socket

data_sensor = {"temp_1": 0.0, "temp_2": 0.0, "acc_x": 0.0, "acc_y": 0.0, "acc_z": 0.0, "roll": 0.0, "pitch": 0.0, "yaw": 0.0, "lanes": 0.0, "pos_x": 0.0, "pos_y": 0.0, "pos_z": 0.0, "speed_x": 0.0," speed_y": 0.0, "speed_z": 0.0, "watt" : 0.0}

#Send command to motor
def run_motor(command):
	try:
		Motor.motor_control(command)
	except Exception as e:
		print("Motor Error", e)
		
#Decode data via TCP for command
def start_tcp_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		server_socket.bind((TCP_IP, TCP_PORT))
		server_socket.listen(5)
	except Exception as e:
		print(f"Error: {e}")

	while True:
		try:
			client_socket, client_address = server_socket.accept()
			
			command = client_socket.recv(1024).decode('utf-8')
			run_motor(command) 

		except Exception as e:
			print(f"TCP Error: {e}")

#Read Gyro and Accel data with MPU6050 sensor		
def read_gyro(mpu, old_accel, old_gyro):
	try:
		accel_data = mpu.get_acceleration()
		gyro_data = mpu.get_rotation()
		vel_data = mpu.get_velocity()
		pos_data = mpu.get_position()
		
		filtered_accel = MPU6050.apply_low_pass_filter(accel_data, old_accel)
		filtered_gyro = MPU6050.apply_low_pass_filter(gyro_data, old_gyro)
		
		data_sensor["acc_x"] = filtered_accel['x']
		data_sensor["acc_y"] = filtered_accel['y']
		data_sensor["acc_z"] = filtered_accel['z']
		data_sensor["roll"] = filtered_gyro['x']
		data_sensor["pitch"] = filtered_gyro['y']
		data_sensor["yaw"] = filtered_gyro['z']
		data_sensor["pos_y"] = pos_data['y']
		data_sensor["pos_z"] = pos_data['z']
		data_sensor["speed_y"] = vel_data['y']
		data_sensor["speed_z"] = vel_data['z']
		
		return filtered_accel, filtered_gyro
	except Exception as e:
		print("Gyro Error: ", e)

#Read temperature data with MLX90614 sensor
def read_temp(sensor):
	try:
		temp_1 = sensor.readObjectTemperature()
		temp_2 = sensor.readAmbientTemperature()
		data_sensor["temp_1"] = temp_1
		data_sensor["temp_2"] = temp_2
	except Exception as e:
		print("Temperature Error: ", e)

#Send the data to GUI
def send_gui():
	try:
		for key, value in data_sensor.items():
			print(f"{key}: {value}") 
		print("---------------------------------")
		sock.sendto(json.dumps(data_sensor).encode("utf-8"), (UDP_IP, UDP_PORT))
	except Exception as e:
		print("Data Error", e)
		time.sleep(0.5)
  
#Unpack the float from I2C data
def read_float(data, index):
	return struct.unpack('f', bytes(data[index:index+4]))[0]

#Read the data from Arduino and update the data_sensor dictionary
def read_data():
	global data_sensor
	try:
		data = bus.read_i2c_block_data(I2C_ADDRESS, 0, 36)
		
		lanes = read_float(data, 4)
		pos_x = read_float(data, 8)
		speed_x = read_float(data, 20)
		watt = read_float(data, 32)
		
		data_sensor["lanes"] = lanes
		data_sensor["pos_x"] = pos_x
		data_sensor["speed_x"] = speed_x
		data_sensor["watt"] = watt
        
	except Exception as e:
		print("Arduino Error:", e)
        
if __name__ == "__main__":
	tcp_thread = threading.Thread(target=start_tcp_server) # Start TCP server thread in the background to handle commands from the remote control computer
	tcp_thread.daemon = True #Make the thread a daemon, meaning it will be terminated when the main program exits
	tcp_thread.start() # Start the thread
	
	mpu = MPU6050() # Initialize MPU6050 sensor
	print("Calibrating sensors. Please keep the MPU6050 still...")
	mpu.calibrate_sensors() # Start sensor calibration
	print("Calibration complete.")
	
	sensor = MLX90614() # Initialize MLX90614 sensor
	
	old_accel = {'x': 0, 'y': 0, 'z': 0}
	old_gyro = {'x': 0, 'y': 0, 'z': 0}
	while True:
		old_accel, old_gyro = read_gyro(mpu, old_accel, old_gyro) # Read gyro and accel data
		mpu.update_velocity_and_position()
		read_temp(sensor)
		read_data()
		send_gui()
		time.sleep(0.5)
