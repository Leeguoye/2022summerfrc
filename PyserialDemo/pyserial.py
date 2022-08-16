import serial
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import keyboard
angle = []

def main():
    port = input("Please enter the port: ")
    ser = serial.Serial("COM3",115200,timeout=2)
    while True:
        if ser.in_waiting >= 0:
            b = ser.readline().decode("utf-8")
            print(b)
            angle.append(b)
            plt.plot(angle,'o')
        elif keyboard.is_pressed("q"):      
            plt.show() 
            break       




if __name__ == "__main__":    
        main()  


