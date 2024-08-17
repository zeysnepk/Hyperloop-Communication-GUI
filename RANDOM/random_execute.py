import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import QThread, pyqtSignal, QTimer
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from gui import Ui_MainWindow
import time
import random
import datetime
import psutil

max_temp = 100
max_power = 1000

class NetworkSpeedThread(QThread):
    speed_signal = pyqtSignal(str)
    
    def __init__(self, interval=1):
        super().__init__()
        self.interval = interval
        self._running = True
        
    def run(self):
        while self._running:
            old_value = psutil.net_io_counters()
            time.sleep(self.interval)
            new_value = psutil.net_io_counters()

            recv = new_value.bytes_recv - old_value.bytes_recv

            self.speed_signal.emit(f"{recv / self.interval / 1024:.2f} KB")
    
    def stop(self):
        self._running = False

                    
class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = figure.add_subplot(111)
        figure.set_facecolor('#323232') 
        figure.subplots_adjust(left=0.05, right=0.98, top=0.80, bottom=0.20)
        super(MplCanvas, self).__init__(figure)
                    
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        self.setWindowTitle("HYPERUSH")
        
        self.create_lists()
        
        self.main.label_info.setText("")
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.data_convert)
        
        self.start_time = time.time()
        
        self.main.pushButton_start.clicked.connect(self.start)
        self.main.pushButton_stop.clicked.connect(self.stop)
        self.main.pushButton_go.clicked.connect(self.go)
        self.main.pushButton_back.clicked.connect(self.back)
        
        self.label_time_timer = QTimer()  
        self.label_time_timer.timeout.connect(self.update_time_label)
        self.elapsed_time = 0
        
        self.network_thread = NetworkSpeedThread()
        self.network_thread.speed_signal.connect(self.update_network_speed)

        
    def update_time_label(self):
        self.elapsed_time = int(time.time() - self.start_time) 
        self.main.label_time.setText(str(self.elapsed_time))
        
        
    def update_network_speed(self, speed):
        self.main.label_data_speed.setText(speed)
        
    def start(self):
        self.main.label_stat.setStyleSheet("font:700 30pt \"Chakra Petch\";\n"
"color: rgb(50,205,50);")
        self.main.label_stat.setText("ON")
        
        self.start_time = time.time()  
        self.label_time_timer.start(1000) 
        
        self.timer.start(1000)
        
        self.network_thread.start()
    
    def stop(self):
        self.main.label_stat.setStyleSheet("font:700 30pt \"Chakra Petch\";\n"
"color: rgb(148, 17, 0);")
        self.main.label_stat.setText("OFF")
        
        self.label_time_timer.stop()
        self.timer.stop()
        
        self.network_thread.stop()
        self.network_thread.wait()
        
    
    def go(self):
        pass
    
    def back(self):
        pass
        
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
        
    def data_convert(self):
        try:
            self.x_pos.append(random.randint(1, 100))
            self.y_pos.append(random.randint(1,100))
            self.z_pos.append(random.randint(1, 100))
        
            self.x_speed.append(random.randint(1, 10))
            self.y_speed.append(random.randint(1, 10))
            self.z_speed.append(random.randint(1, 10))
        
            self.x_acc.append(random.randint(1, 5))
            self.y_acc.append(random.randint(1, 5))
            self.z_acc.append(random.randint(1, 5))
        
            self.x_ori.append(random.randint(1, 360))
            self.y_ori.append(random.randint(1, 360))
            self.z_ori.append(random.randint(1, 360))
        
            self.temp_1 = random.randint(1, max_temp)
            self.temp_2 = random.randint(1, max_temp)
            self.power = random.randint(1, max_power)
            
            self.battery_percentage = (self.power / max_power) * 100
        
            self.time.append(time.time() - self.start_time)
        
            self.draw_graph(self.main.graph_position, self.time, self.x_pos, self.y_pos, self.z_pos, "Position (m)")
            self.draw_graph(self.main.graph_speed, self.time, self.x_speed, self.y_speed, self.z_speed, "Velocity (m/s)")
            self.draw_graph(self.main.graph_acc, self.time, self.x_acc, self.y_acc, self.z_acc, "Acceleration (m/s²)")
            self.draw_graph(self.main.graph_ori, self.time, self.x_ori, self.y_ori, self.z_ori, "Orientation (°)")
        
            self.main.label_position.setText(f"X --> {self.x_pos[-1]:.2f} cm\nY --> {self.y_pos[-1]:.2f} cm\nZ --> {self.z_pos[-1]:.2f} cm")
            self.main.label_speed.setText(f"X --> {self.x_speed[-1]:.2f} m/s\nY --> {self.y_speed[-1]:.2f} m/s\nZ --> {self.z_speed[-1]:.2f} m/s")
            self.main.label_acc.setText(f"X --> {self.x_acc[-1]:.2f} m/s²\nY --> {self.y_acc[-1]:.2f} m/s²\nZ --> {self.z_acc[-1]:.2f} m/s²")
            self.main.label_ori.setText(f"X --> {self.x_ori[-1]:.2f}\nY --> {self.y_ori[-1]:.2f}\nZ --> {self.z_ori[-1]:.2f}")
        
            self.draw_temp()
            self.main.label_temp.setText(f"T1 : {self.temp_1:.2f} °C\nT2 : {self.temp_2:.2f} °C")
        
            self.draw_power()
            self.main.label_watt.setText(f"{self.power:.2f} W")
            self.main.label_watt_2.setText(f"{self.power:.2f} W")
            
            self.main.label_date.setText(datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S"))
            
            self.main.label_battery.setText(f"{self.battery_percentage:.2f}%")
        except IndexError as e:
            print(f"Data Format Error: {e}")
        
        
    def draw_graph(self, frame, t, y1, y2, y3, title):
        graph = MplCanvas(frame, width=5, height=4, dpi=100)
        
        graph.axes.plot(t, y1, color='red',label='X')
        graph.axes.plot(t, y2, color='green',label='Y')
        graph.axes.plot(t, y3, color='blue',label='Z')
        
        if len(t) > 5:
            graph.axes.set_xlim(t[-5], t[-1])  
            
        elif len(t) == 1:
            graph.axes.set_xlim(0, 1) 
        else:
            graph.axes.set_xlim(t[0], t[-1])
        
        graph.axes.set_facecolor('#323232') 
        graph.axes.set_title(title, color='white')
        legend = graph.axes.legend(loc='upper right')
            
        for label in graph.axes.get_xticklabels() + graph.axes.get_yticklabels():
            label.set_color('white')
        
        layout = frame.layout()
        
        for i in reversed(range(layout.count())):
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
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())     
    
        
        
        
