import serial
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import keyboard
angle = []

def main():
    port = input("Please enter the port: ")
    ser = serial.Serial("COM3",115200,timeout=2)
    flag = False

    plt.ion()
    while not(flag):
        b = ser.readline().decode("utf-8").strip()
        print(b)
        try:
            b = round(float(b),2)
        except Exception as e:
            print('unable to float b, due to ',e)
        angle.append(b)
        plt.plot(angle,'o')
        plt.pause(0.001)
        plt.ioff() # close window
        flag = keyboard.is_pressed("q")


if __name__ == "__main__":    
        main()  


