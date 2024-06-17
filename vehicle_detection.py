import cv2
from darkflow.net.build import TFNet
import os
import math
from datetime import datetime
import openpyxl

def get_base_time_from_excel():
    # Read the Excel file
    wb = openpyxl.load_workbook('./predicted_traffic.xlsx')
    sheet = wb.active
    
    # Get the current date and time
    current_datetime = datetime.now()
    
    # Extract current date and hour
    current_date_dd_mm_yyyy = current_datetime.strftime('%d-%m-%Y')
    current_date_yyyy_mm_dd = current_datetime.strftime('%Y-%m-%d')
    current_hour = current_datetime.strftime('%H:00:00')
    
    # Combine date and hour for comparison
    current_datetime_combined_dd_mm_yyyy = current_date_dd_mm_yyyy + ' ' + current_hour
    current_datetime_combined_yyyy_mm_dd = current_date_yyyy_mm_dd + ' ' + current_hour
    
    # Find the row in the Excel sheet corresponding to the current hour
    base_time = 10  # Default base time is 10 if not found in the Excel
    for row in sheet.iter_rows(values_only=True):
        if row[0] == current_datetime_combined_dd_mm_yyyy or row[0] == current_datetime_combined_yyyy_mm_dd:
            base_time = row[1]
            break
    
    # Close the workbook
    wb.close()
    
    return int(base_time)


class TrafficSignal:
    def __init__(self, lanes_per_direction):
        self.lanes_per_direction = lanes_per_direction
        self.max_green_time = 60
        self.green_time = [30] * lanes_per_direction
        self.yellow_time = [3] * lanes_per_direction

    def update_signal_timings(self, vehicle_counts):
        for lane in range(self.lanes_per_direction):
            green_time = self.calculate_green_time(vehicle_counts[lane])
            self.green_time[lane] = min(self.max_green_time, green_time)
            self.yellow_time[lane] = min(5, self.green_time[lane] // 10)

    def calculate_green_time(self, num_cars):
        base_time = get_base_time_from_excel()
        base_time = base_time/6
        weight_factor = 0.01
        max_weighted_time = 60
        weighted_time = base_time + (max_weighted_time - base_time) * (1 - math.exp(-weight_factor * num_cars))
        return weighted_time

    def print_signal_timings(self):
        print("Signal Timings:")
        for lane in range(self.lanes_per_direction):
            print(f"Lane {lane + 1}: Green - {self.green_time[lane]} sec, Yellow - {self.yellow_time[lane]} sec")


options = {
    'model': './cfg/yolo.cfg',
    'load': './bin/yolov2.weights',
    'threshold': 0.3
}
lanes_per_direction = 1
signal = TrafficSignal(lanes_per_direction)

tfnet = TFNet(options)

def detectVehicles(frame):
    global tfnet, signal
    
    result = tfnet.return_predict(frame)
    
    vehicle_count = 0
    for vehicle in result:
        label = vehicle['label']
        if label in ["car", "bus", "bike", "truck", "rickshaw"]:
            vehicle_count += 1
    
    vehicle_counts =[vehicle_count, vehicle_count, vehicle_count, vehicle_count]
    signal.update_signal_timings(vehicle_counts)
    signal.print_signal_timings()
    
    for vehicle in result:
        label = vehicle['label']
        if label in ["car", "bus", "bike", "truck", "rickshaw"]:
            top_left = (vehicle['topleft']['x'], vehicle['topleft']['y'])
            bottom_right = (vehicle['bottomright']['x'], vehicle['bottomright']['y'])
            frame = cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 3)
            frame = cv2.putText(frame, label, top_left, cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
    
    cv2.imshow("Traffic Detection", frame)
    cv2.waitKey(1)

def processVideo(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        detectVehicles(frame)
        
    cap.release()
    cv2.destroyAllWindows()

video_path = './traffic.mp4'
processVideo(video_path)