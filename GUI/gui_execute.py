import sys
import socket
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from design import Ui_MainWindow
import time, json
import datetime
import psutil

UDP_IP = "pc_ip" #IP address of the remote controlcomputer
UDP_PORT = 6666  #UDP port of the remote control computer

TCP_IP = "raspberry_ip" #IP address of the Raspberry Pi 4
TCP_PORT = 3333 #TCP port of the Raspberry Pi 4

max_temp = 50 
max_power = 100

class NetworkSpeedThread(QThread):
	speed_signal = pyqtSignal(str) #Signal for network speed
    
	def __init__(self, interval=1):
		super().__init__()
		self.interval = interval #seconds
		self._running = True #running continuously until stopped by stop() method
        
	def run(self):
		while self._running: 
			old_value = psutil.net_io_counters() #value of network speed starting point
			time.sleep(self.interval)
			new_value = psutil.net_io_counters() #value of network speed ending point
			recv = new_value.bytes_recv - old_value.bytes_recv #amount of network speed increase
			self.speed_signal.emit(f"{recv / self.interval / 1024:.2f} KB") #sending network speed by signal
    
	def stop(self):
		self._running = False #stopping the thread

class SocketThread(QThread):
	data_received = pyqtSignal(str) #signal for received data via UDP
    
	def __init__(self):
		super().__init__()
		self._running = True

	def run(self):
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock: #starting UDP socket
			sock.bind((UDP_IP, UDP_PORT))  #set the IP and port for UDP socket
			sock.settimeout(1)  #set socket timeout to prevent blocking indefinitely when no data received

		while self._running:
			try:
				data, addr = sock.recvfrom(1024) #receive data from the capsule control computer
				data = data.decode("utf-8") #decode received data from UTF-8
				self.data_received.emit(data) #sending received data by signal
			except socket.timeout:
			continue
			except Exception as e:
			print("UDP error", e)
			
	def stop(self):
		self._running = False
		self.wait() #continuously waiting for data until stopped by stop() method

class MplCanvas(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100): #Initialize MPL Canvas
		figure = Figure(figsize=(width, height), dpi=dpi) #Create a plot on MPL Canvas
		self.axes = figure.add_subplot(111)  #Add axes to MPL Canvas
		figure.set_facecolor('#323232')   #Set the background color of MPL Canvas
		figure.subplots_adjust(left=0.05, right=0.98, top=0.80, bottom=0.20) #Adjust the size of MPL Canvas
		super(MplCanvas, self).__init__(figure)  #Draw MPL Canvas on the screen
                    
class Main(QMainWindow):
	def __init__(self):
		super().__init__() #Inherit from QMainWindow
		
		self.main = Ui_MainWindow()  #Load necessary features from UI file
		self.main.setupUi(self)  #Initialize the UI screen
		self.setWindowTitle("HYPERUSH") #Set the window title
		
		self.create_lists() #Function for data structures
		
		self.main.label_info.setText("") 
		
		self.socket_thread = SocketThread()  #Start SocketThread for UDP
		self.socket_thread.data_received.connect(self.data_convert)  #Connecting the emitted signal to the function
		
		self.start_time = time.time() #Start time
		
		self.main.pushButton_start.clicked.connect(self.start)  #Connect the start button to the start function
		self.main.pushButton_stop.clicked.connect(self.stop) #Connect the stop button to the stop function
		self.main.pushButton_go.clicked.connect(self.go) #Connect the go button to the go function
		self.main.pushButton_back.clicked.connect(self.back) #Connect the back button to the back function
		
		self.label_time_timer = QTimer()   #Start the timer
		self.label_time_timer.timeout.connect(self.update_time_label) #Call the timer frequently
		
		self.network_thread = NetworkSpeedThread() #Start NetworkSpeedThread for network speed
		self.network_thread.speed_signal.connect(self.update_network_speed)  #Call the network speed frequently
        
	def komut_gonder_tcp(self, RPI_IP, RPI_PORT, command):
		try:
			client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Start TCP socket
			client_socket.connect((TCP_IP, TCP_PORT)) #Connect to TCP socket
			
			client_socket.send(command.encode('utf-8')) #Encode and send the command with utf-8
		except Exception as e:
			print("TCP Error:", e)
        
	def update_time_label(self):
		self.elapsed_time = int(time.time() - self.start_time)  #Variable that keeps track of time
		self.main.label_time.setText(str(self.elapsed_time)) #Display time on screen

        
	def update_network_speed(self, speed):
		self.main.label_data_speed.setText(speed) #Display network speed on screen
        
	def start(self):
		self.main.label_stat.setStyleSheet("font:700 30pt \"Chakra Petch\";\n"
		"color: rgb(50,205,50);") 
		self.main.label_stat.setText("ON")
		
		self.start_time = time.time()  
		self.label_time_timer.start(1000) #Start the timer
		self.socket_thread.start() #Start UDP socket
		self.network_thread.start() #Start network speed
		
		self.komut_gonder_tcp(TCP_IP, TCP_PORT, 'B')  #Send Start command to Raspberry
    
	def stop(self):
		self.main.label_stat.setStyleSheet("font:700 30pt \"Chakra Petch\";\n"
		"color: rgb(148, 17, 0);")
		self.main.label_stat.setText("OFF")
		
		self.label_time_timer.stop()  #Stop the timer
		
		self.socket_thread.stop()  #Stop UDP socket
		
		self.network_thread.stop()  #Stop network speed
		self.network_thread.wait() #Continue to extract data from the remote computer
		
		
		self.komut_gonder_tcp(TCP_IP, TCP_PORT, 'D') #Send Stop command to Raspberry
        
	def go(self):
		self.komut_gonder_tcp(TCP_IP, TCP_PORT, 'F') #Send Forward command to Raspberry

	def back(self):
		self.komut_gonder_tcp(TCP_IP, TCP_PORT, 'A') #Send Backward command to Raspberry
        
	def create_lists(self):
		self.x_pos = []
		self.y_pos = []
		self.z_pos = []
		
		self.x_speed = []
		self.y_speed = []
		self.z_speed = []
		
		self.x_acc = []
		self.y_acc = []
		self.z_acc = []
		
		self.x_ori = []
		self.y_ori = []
		self.z_ori = []
		
		self.time = []
		
		self.battery_percentage = 0
        
	def data_convert(self, data):
		try:
			data = json.loads(data)  #Convert JSON string to dict
			#In this section, relevant data is taken and added to the list
			self.x_pos.append(float(data["pos_x"]))
			self.y_pos.append(float(data["pos_y"]))
			self.z_pos.append(float(data["pos_z"]))
			
			self.x_speed.append(float(data["speed_x"]))
			self.y_speed.append(float(data["speed_y"]))
			self.z_speed.append(float(data["speed_z"]))
			
			self.x_acc.append(float(data["acc_x"]))
			self.y_acc.append(float(data["acc_y"]))
			self.z_acc.append(float(data["acc_z"]))
			
			self.x_ori.append(float(data["roll"]))
			self.y_ori.append(float(data["pitch"]))
			self.z_ori.append(float(data["yaw"]))
			
			self.temp_1 = float(data["temp_1"])
			self.temp_2 = float(data["temp_2"])
			self.power = float(data["watt"])
			
			lanes = float(data["lanes"])
			self.main.label_serit.setText(str(lanes))
			
			self.battery_percentage = (self.power / max_power) * 100 #set battery percentage
			
			self.time.append(time.time() - self.start_time) 
			
			#Draw graphs with incoming data
			self.draw_graph(self.main.graph_position, self.time, self.x_pos, self.y_pos, self.z_pos, "Konum (cm)")
			self.draw_graph(self.main.graph_speed, self.time, self.x_speed, self.y_speed, self.z_speed, "Hız (m/s)")
			self.draw_graph(self.main.graph_acc, self.time, self.x_acc, self.y_acc, self.z_acc, "İvme (m/s²)")
			self.draw_graph(self.main.graph_ori, self.time, self.x_ori, self.y_ori, self.z_ori, "Yönelim ()")
			
			self.main.label_position.setText(f"X --> {self.x_pos[-1]:.2f} cm\nY --> {self.y_pos[-1]:.2f} cm\nZ --> {self.z_pos[-1]:.2f} cm")
			self.main.label_speed.setText(f"X --> {self.x_speed[-1]:.2f} m/s\nY --> {self.y_speed[-1]:.2f} m/s\nZ --> {self.z_speed[-1]:.2f} m/s")
			self.main.label_acc.setText(f"X --> {self.x_acc[-1]:.2f} m/s²\nY --> {self.y_acc[-1]:.2f} m/s²\nZ --> {self.z_acc[-1]:.2f} m/s²")
			self.main.label_ori.setText(f"X --> {self.x_ori[-1]:.2f}\nY --> {self.y_ori[-1]:.2f}\nZ --> {self.z_ori[-1]:.2f}")
			
			self.draw_temp() #temperature display on the graph
			self.main.label_temp.setText(f"T1 --> {self.temp_1} °C\nT2 --> {self.temp_2:.2f} °C") 
			
			self.draw_power() #power display on the graph
			self.main.label_watt.setText(f"{self.power:.2f} W") 
			self.main.label_watt_2.setText(f"{self.power:.2f} W")
			
			self.main.label_date.setText(datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")) #date and time display
			
			self.main.label_batarya.setText(f"{self.battery_percentage:.2f}%") #battery display on the graph
            
		except Exception as e:
			print(f"Data Error: {e}")     
        
	def draw_graph(self, frame, t, y1, y2, y3, title):
		graph = MplCanvas(frame, width=5, height=4, dpi=100) #Clear the previous graph
		
		graph.axes.plot(t, y1, color='red',label='X') 
		graph.axes.plot(t, y2, color='green',label='Y')
		graph.axes.plot(t, y3, color='blue',label='Z')
        
		if len(t) > 5:
			graph.axes.set_xlim(t[-5], t[-1])  
            
		elif len(t) == 1:
        		graph.axes.set_xlim(0, 1) 
        	else:
            		graph.axes.set_xlim(t[0], t[-1])
        
		graph.axes.set_facecolor('#323232') #Dark grey background
		graph.axes.set_title(title, color='white') #White title
		legend = graph.axes.legend(loc='upper right') #Right-upper legend
            
		for label in graph.axes.get_xticklabels() + graph.axes.get_yticklabels(): #Change text color to white
        		label.set_color('white')
        
		layout = frame.layout() #Clear the previous layout
        
		for i in reversed(range(layout.count())): #Delete all previous widgets
        		widget = layout.itemAt(i).widget()
        		if widget is not None:
        			widget.setParent(None)
        
		layout.addWidget(graph)
        
	def draw_temp(self):
		base_style =("#frame_t1{\n"
		"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:{STOP_1} rgba(69, 150, 255, 255), stop:{STOP_2} rgba(255, 255, 255, 0));\n"
		"}")
		
		temp_progress_p1 = self.temp_1 / max_temp
		temp_progress_p2 = self.temp_2 / max_temp
		
		stop_1_p1 = str(temp_progress_p1 - 0.001)
		stop_2_p1 = str(temp_progress_p1)
		
		stop_1_p2 = str(temp_progress_p2 - 0.001)
		stop_2_p2 = str(temp_progress_p2)

		if temp_progress_p1 > 0.008 * max_temp and temp_progress_p2 > 0.008 * max_temp:
			new_style_p1 = base_style.replace("{STOP_1}", stop_1_p1).replace("{STOP_2}", stop_2_p1).replace("rgba(69, 150, 255, 255)", "rgba(216, 82, 55, 255)")
			new_style_p2 = base_style.replace("{STOP_1}", stop_1_p2).replace("{STOP_2}", stop_2_p2).replace("frame_t1", "frame_t2").replace("rgba(69, 150, 255, 255)", "rgba(216, 82, 55, 255)")
			self.main.frame_full.setStyleSheet("""#frame_full{
			background-color: rgba(216, 82, 55, 255);
			border-radius:22px
			}""")
            
		else:
			new_style_p1 = base_style.replace("{STOP_1}", stop_1_p1).replace("{STOP_2}", stop_2_p1)
			new_style_p2 = base_style.replace("{STOP_1}", stop_1_p2).replace("{STOP_2}", stop_2_p2).replace("frame_t1", "frame_t2")
			self.main.frame_full.setStyleSheet("""#frame_full{
			background-color: rgb(69, 150, 255);
			border-radius:22px
			}""")
			
			self.main.frame_t1.setStyleSheet(new_style_p1)
			self.main.frame_t2.setStyleSheet(new_style_p2)

        
	def draw_power(self):
		base_style =("#frame_power{\n"
		"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 255, 255, 0), stop:{STOP_2} rgba(69, 150, 255, 255));\n"
		"border-radius:90px\n"
		"}")
		
		watt_pressure = float((max_power-self.power) / (max_power))
		
		stop_1 = str(watt_pressure - 0.001)
		stop_2 = str(watt_pressure)
		
		new_style = base_style.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)
		
		self.main.frame_power.setStyleSheet(new_style)
        
if __name__ == "__main__":
		app = QApplication(sys.argv) #Start the QApplication
		main = Main() #Start the interface
		main.show()  #Show the screen
		sys.exit(app.exec_()) #Exit the screen
